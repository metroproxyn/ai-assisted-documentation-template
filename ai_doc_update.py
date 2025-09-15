## NOTE: THis file contains a minimal script (pseudo-code). Needs to be modified for your specific case.

import openai, os, subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")

# get diff from last commit
diff = subprocess.check_output(["git", "diff", "HEAD^", "HEAD"]).decode("utf-8")

prompt = f"""
You are a senior technical writer.
Given this git diff, suggest updates to the documentation.
Format as Markdown with file paths, updated text blocks, and a summary.
Diff:
{diff}
"""

resp = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3
)

# Save output to file so PR action can include it
with open("AI_DOC_UPDATE.md", "w") as f:
    f.write(resp["choices"][0]["message"]["content"])