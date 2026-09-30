"""Usage: python3 validate_roadmap.py <raw_output.json>
Step 1: strict JSON schema validation. Step 2: banned-phrase lint (business rules 12,13,14,16,21,24)."""
import json, re, sys
from jsonschema import Draft202012Validator

BANNED = r"government|govt|state[- ]level|state college|state[- ]run|flexible|hybrid|self-paced|extra (weekly )?(hours|time)|will provide|ensures?\b|guarantee|exact (route|skills)|job-ready|master sql|advanced (python|ml)|apply in year|scholarship|low[- ]tuition|placement rate|cheaper|cost[- ]effective|affordable|financially (suitable|viable)|subsidi[sz]ed|public (institution|university|college)|state universit(y|ies)|\bmaster(y|ing)?\b(?!'s)|advanced level|merit-based|manageable|large-scale"

raw = open(sys.argv[1]).read()
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    sys.exit(f"FAIL: not valid JSON ({e})")
import os
schema = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "schema", "roadmap_output.schema.json")))
errs = list(Draft202012Validator(schema).iter_errors(data))
for p in data.get("paths", []) if isinstance(data, dict) else []:
    ed = p.get("education", {})
    for k in ("degree", "branch"):
        if re.search(r"/|\bor\b", str(ed.get(k, "")), re.I):
            print("RULE3 FAIL:", p.get("path_id"), k, "holds more than one value:", ed.get(k))
            errs.append(1)
    ms = p.get("milestones", [])
    if ms and not re.search(r"target", (ms[-1].get("phase","")+ms[-1].get("focus","")), re.I):
        print("RULE22 FAIL:", p.get("path_id"), "last milestone is not target-role preparation")
        errs.append(1)
for e in errs:
    if e == 1: continue
    print("SCHEMA FAIL:", list(e.path), e.message)
hits = [(m.group(0), raw[max(0, m.start()-60):m.end()+40].replace("\n", " ")) for m in re.finditer(BANNED, raw, re.I)]
for h, ctx in hits:
    print(f"PHRASE FAIL: '{h}' ... {ctx}")
print("RESULT:", "PASS" if not errs and not hits else "FAIL")
sys.exit(1 if errs or hits else 0)
