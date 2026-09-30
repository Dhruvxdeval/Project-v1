# Project-v1
Student - post 12th /jee - companion TILL job/goal.
---

# Project-v1

Student career companion for students after Class 12 (PCM first). The student states a career destination. The AI returns 2-3 realistic pathways to that SAME destination. The AI never chooses the career.

## Folders
- `prompts/` - roadmap prompt (frozen: `roadmap_prompt_v3_5.txt`)
- `schema/` - `student_profile.schema.json` (input), `roadmap_output.schema.json` (output), `roadmap_output.sample.json` (example output from Test 009)
- `tools/validate_roadmap.py` - checks raw model output against the schema and banned phrases
- `tests/` - raw model outputs, saved unedited

## Check an output
`pip install jsonschema` then `python3 tools/validate_roadmap.py tests/test_009_raw.json`

## Status
Prompt V3.5 frozen after Test 009 (raw output, unedited, validator PASS). Next: UI (Aniket) and backend (Gagan) integrate against the schema and sample.

## Known issues (not blocking)
- Some milestone projects are worded as if an internship already happened ("Contributed code to an internship project"). Fix in a later prompt version.
- PATH_B (B.Sc) packs production skills (APIs, orchestration, monitoring) into one final year.
- The validator only checks structure and banned words. A human still reads every test output.
