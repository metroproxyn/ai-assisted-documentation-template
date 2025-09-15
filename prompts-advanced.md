# Advanced Prompts – AI for Technical Writing

The collection of the advanced prompts moves beyond basic drafting and editing. Here, you will find prompts designed for those, who are tasked with optimizing entire workflows, ensuring impeccable quality, and leading the strategic integration of AI into the documentation lifecycle. 

This refined set of prompts demonstrates not just the ability to use AI, but to do so strategically, with an eye for quality, efficiency, and collaboration—exactly the skills a Senior Technical Writer needs to showcase.

---

## 1. Research & Analysis

**1.1. Generate User Questions**
 

Act as a technical writer. Based on the following product description: "[Insert product description]". Generate a list of 10-15 questions a complete beginner might have when first encountering the user interface. Group the questions into logical categories such as "Setup & Configuration," "Basic Operations," and "Troubleshooting."


**1.2. Identify Target Audience & Pain Points**
 

The product is designed for [describe product purpose]. Define three distinct user personas for this product. For each persona, describe their:
1. **Primary goal:** What they want to achieve.
2. **Technical proficiency:** Beginner, Intermediate, Expert.
3. **Biggest pain point:** Their main challenge or frustration.
4. **Key question:** The one question they need answered to be successful.


**1.3. Analyze Competitor Documentation**
 

Analyze the structure and content of the following competitor's documentation page: [Insert URL]. Provide a brief analysis that includes:
*   **Overall structure:** How is the information organized?
*   **Tone & style:** Is it formal, conversational, or technical?
*   **Strengths:** What do they do well (e.g., examples, visuals, clarity)?
*   **Gaps & opportunities:** What is missing or could be improved? Suggest one thing we could do better.


**1.4. Verify Accuracy & Identify Gaps**
 

You are a technical writer reviewing a draft for factual accuracy and completeness.
**Text to review:** [Insert text]
**Source of truth (API Spec/Product Description):** [Insert description or link]

Analyze the text and provide your findings in a table with the following columns:
*   **Claim in Text:** Quote the specific sentence or claim.
*   **Matches Source?:** Yes / No / Requires Clarification.
*   **Hallucination Risk:** Low / Medium / High.
*   **Recommended Action:** What needs to be done (e.g., "Remove," "Rephrase to [suggestion]," "Clarify with SME").


---

### **2. Drafting & Writing**

**2.1. Draft a User Guide Section**
 

Write a draft for a user guide section for the function: "[Function Name]". Use ONLY the information provided within the <context></context> tags. Do not add information not present in the context.

**Requirements:**
*   **Style:** Use clear, imperative language ("Click the button," not "You should click the button").
*   **Structure:**
    1.  **Introduction:** One paragraph summarizing the function.
    2.  **Prerequisites:** A bulleted list of any required setup or prior steps.
    3.  **Instructions:** A numbered list of steps to perform the core task.
    4.  **Example:** A sample of the expected output or result.

[Detailed function description, API parameters, screenshots, etc., go here]


**2.2. Create a "Getting Started" Guide Outline**
 

Create a detailed outline for a "Getting Started" guide for [Product Name]. The audience is a non-technical end-user. The outline should include:
*   **Title:** Getting Started with [Product Name]
*   **Objective:** A single sentence stating the guide's goal.
*   **Sections:** 4-5 main sections (H2 headings).
*   **Subsections:** 2-3 subsections (H3 headings) for each main section.
*   **Appendix:** Suggest any necessary appendices (e.g., FAQ, Troubleshooting).


**2.3. Draft an API Method Documentation**
 

Write comprehensive documentation for the following API method. Structure it as follows:

**Method:** `[Method Name]`
**Endpoint:** `[API Endpoint URL]`
**Description:** [Briefly describe what this method does]

**Parameters:**
*   Create a table with columns: `Parameter`, `Type`, `Required`, `Description`.

**Request Example:**
Provide a clear JSON example of a request body.

**Response Example:**
Provide a clear JSON example of a successful response.

**Error Codes:**
*   List the most common HTTP error codes (e.g., 400, 404, 500) and their possible meanings in this context.


---

### 3. Editing & Improvement

**3.1. Improve Readability & Clarity**
 

Improve the readability and clarity of the following text. Apply these specific edits:
1.  **Sentence Length:** Break down long sentences (target: under 25 words).
2.  **Jargon:** Replace complex jargon with simpler terms where possible without losing meaning.
3.  **Voice:** Convert passive voice to active voice.
4.  **Structure:** Add subheadings (H3 or H4) to improve scannability.

After revising the text, provide a brief summary of the changes you made and why.

**Text to improve:** [Insert text]


**3.2. Adapt Tone for Different Audiences**
 

Rewrite the following technical paragraph for three different audiences. Preserve the core information but adapt the tone, detail, and language.

**Original Text:** [Insert text]

**Version 1: For Executives/Business Users**
*   Focus: High-level benefits and outcomes.
*   Avoid: Technical jargon, code, and implementation details.

**Version 2: For Developers/Engineers**
*   Focus: Technical specifics, code examples, parameters, and system interactions.
*   Language: Can use appropriate technical terms.

**Version 3: For End-Users**
*   Focus: Simple, step-by-step instructions on what to do and what to expect.
*   Language: Clear, conversational, and action-oriented.


---

### 4. Code Documentation & Explanation

**4.1. Explain a Complex Code Block**
 

Act as a developer explaining code to a technical writer. Explain the purpose and function of the following code block in plain English. Structure your explanation as follows:
1.  **Overall Purpose:** What does this code do in the context of the application?
2.  **Step-by-Step Logic:** Walk through the key steps the code performs.
3.  **Key Variables/Parameters:** Explain what the most important variables are for.
4.  **Dependencies:** Note any other parts of the system it relies on.

**Code:** [Insert code snippet]


---

### **5. Localization & Translation**

**5.1. Check Localization Quality**
 

You are assisting with the localization of documentation. Review the following source text and its translation for cultural appropriateness, technical accuracy, and natural flow.

**Source (English):**
[Insert English text]

**Translation (Russian):**
[Insert Russian translation]

Provide feedback on:
1.  **Technical Accuracy:** Does the translation correctly convey all technical terms and instructions?
2.  **Idioms & Cultural References:** Are there any phrases that would not make sense to a native speaker? Suggest neutral alternatives.
3.  **Readability:** Does the translated text sound natural and fluent?


---

### 6. Process & Collaboration

**6.1. Draft an Email to an SME (Subject Matter Expert)**
 

Draft a polite and professional email to a Subject Matter Expert (SME) to request a review of your documentation draft. The email should:
*   Be concise and respectful of their time.
*   Clearly state the document/topic you need reviewed ([Insert Topic]).
*   Specify the exact type of feedback you need (e.g., "Please verify the technical accuracy of the steps in section 2.3").
*   Propose a realistic deadline for their review ([Insert Date]).
*   Offer to answer any questions they might have.


**6.2. Create a Documentation Review Checklist**
 

Create a comprehensive checklist for peer reviews or SME reviews of technical documentation. The checklist should include categories for:
*   **Accuracy:** Does the content match the product/spec?
*   **Completeness:** Are all necessary topics covered? Are there missing steps?
*   **Clarity & Readability:** Is the language clear and concise?
*   **Style Guide Adherence:** Does it follow the company's style guide (e.g., tone, terminology)?
*   **Formatting:** Is the structure and formatting correct?
Provide the checklist in a clear, bulleted format.
