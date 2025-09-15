# Prompt Repository — AI for Technical Writing

This file contains reusable prompts I use on my position of Technical Writer to automate and optimize documentation workflows.

---

## 1. Generate API Reference from OpenAPI

```text
System: You are a senior technical writer.  
User: Given the following OpenAPI spec: <paste>, generate a complete API reference page including:  
- Overview  
- Endpoint summary  
- Parameters table (name | type | required | description | example)  
- Request/Response examples (JSON)  
- Error codes  
- Notes & related endpoints  
Also list 5 follow-up questions to clarify with developers.
```

## 2. Convert Raw Data to Markdown Table

```text
Convert the following list into a Markdown table with columns: Parameter | Type | Default | Description | Example.  
Group parameters by category and mark required ones with "✓".
```

## 3. Rewrite for Different Audiences

```text
Rewrite this paragraph for a beginner developer audience.  
- Use active voice  
- Max sentence length: 18 words  
- Keep code blocks unchanged  
- Tone: concise, friendly, professional
```

## 4. Auto-Update Documentation (PR Draft)

```text
Given this git diff: <diff>, identify affected documentation pages and produce a PR description that includes:  
- Summary of code changes  
- Suggested doc updates (with file paths)  
- Checklist for verification  
Output as Markdown for GitHub PR.
```

## 5. Summarize Complex Technical Sources
   
```text
Summarize the following documents into:  
- TL;DR (3 bullets)  
- 5 key takeaways  
- Potential pitfalls to document  
- Proposed outline for a 1500-word guide
```

## 6. Style & Readability Check

```text
Analyze the following text for readability:  
- Highlight passive voice  
- Simplify complex sentences  
- Ensure tone matches our style guide  
- Suggest improvements in Plain English
```
