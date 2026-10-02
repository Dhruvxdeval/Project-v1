# Generate -> validate -> retry (backend contract for roadmap generation)

The LLM does not follow every prompt rule every time (Tests 010-012). So the backend must not trust one raw output.

1. Build the prompt: `prompts/roadmap_prompt_v3_7.txt` + the student profile JSON.
2. Call the LLM. Keep the raw text unedited.
3. Validate: run the checks in `tools/validate_roadmap.py` (schema, banned phrases, RULE2C/6C/18/19B, destination equals profile career). Pass the profile as the second argument.
4. If it fails: call the LLM again with the same prompt plus the FAIL lines appended ("Fix these problems and return JSON only: ..."). Maximum 3 attempts.
5. If still failing: return an error to the UI ("Roadmap could not be generated, try again"). Never show an unvalidated roadmap. Never repair the JSON by hand or by code.
6. Only a validated roadmap is saved and sent to `window.Meet2P4.renderRoadmap(...)`.

Log every attempt (raw output + FAIL lines) so prompt problems stay visible.
