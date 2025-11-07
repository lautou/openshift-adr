Here is a structured and refined version of your meta-prompt.

This "meta-prompt" is designed to be given to me (Gemini) to generate the final, optimized NotebookLM prompt you need. It logically organizes all your requirements, constraints, and specific instructions (like the update logic and formatting) into a clear, actionable request.

---

### **Refined Meta-Prompt for Gemini**

**Attachments (Assume these are provided):**

1.  `AD ID prefix dictionary` (Contains prefixes like OCP-BM, GITOPS, etc.)
2.  `AD agreeing parties dictionary` (Contains roles like "Platform Engineering," "Security," etc.)
3.  `GITOPS AD example` (The current AD file for GITOPS)
4.  `OCP-BM AD example` (The current AD files for OCP-BM)

**Your Role:** I am a Red Hat Consulting Architect.

**My Goal:** I need to create and maintain an Architecture Decision (AD) repository for designing OCP / ODF / RHOAI. I use NotebookLM to manage this process.

**My Task:**
Generate a **single, repeatable prompt for NotebookLM** that I can use to review my existing ADs. The prompt must adhere to all constraints listed below.

**Context (Uploaded in NotebookLM):**

- Latest documentation PDFs for:
  - OpenShift Container Platform (OCP)
  - OpenShift Data Foundation (ODF)
  - OpenShift Logging
  - OpenShift GitOps
  - OpenShift Pipelines
  - Red Hat OpenShift AI Self-Managed (RHOAI)
- The `AD ID prefix dictionary`
- The `AD agreeing parties dictionary`

**AD Structure Reference:**

- **ID:** Unique, using a prefix from the dictionary (e.g., `OCP-BM-01`).
- **Title:** A concise title.
- **Issue:** The architectural question being addressed.
- **Assumptions:** Context/conditions for the AD's relevance (e.g., "The environment is disconnected."). Must be present, even if `N/A`.
- **Alternatives:** At least two or more options.
- **Justification:** Rationale for each alternative.
- **Implication:** Consequences of choosing each alternative.
- **Agreeing Parties:** A list of roles from the dictionary.

---

### **Requirements for the Generated NotebookLM Prompt**

Create a NotebookLM prompt that instructs it to perform the following analysis, respecting these strict rules:

**1. Character Limit:**

- The _entire_ generated prompt must be **under 2000 characters**.

**2. Scope & Focus:**

- **Only** analyze ADs with the prefixes **OCP-BM** and **GITOPS**, based on the provided example files.
- Ignore all other AD prefixes (like ODF, RHOAI, etc.) for this analysis.

**3. Core Task & Output Logic:**

- You will review the provided `OCP-BM AD example` and `GITOPS AD example` files against the latest documentation in your sources.
- For each AD, you must determine if it needs to be **Created**, **Updated**, or **Removed**.
- Your output must be synthetic, showing _only_ the required changes.

**4. Specific Logic for "Update":**

- The provided AD examples contain _all_ sections (ID, Title, Issue, Assumptions, Alternatives, Justification, Implication, Agreeing Parties).
- When an AD needs an **Update**, you must _only_ list the specific sections that require modification.
- **Crucially:** If you review an existing AD (like `OCP-BM-01`) and find **no changes** are needed based on the latest docs, you MUST explicitly state:
  `**OCP-BM-01: [Title]**`
  `* No updates required.`
- Do NOT reprint the AD's existing content if no update is needed.

**5. Specific Logic for "Create":**

- If new features or changes in the source documents warrant a **new** AD, generate it.
- New AD IDs must use a two-digit format (e.g., `OCP-BM-XX` or `GITOPS-XX`). Do not use three-digit IDs.
- You must generate _all_ required fields: ID, Title, Issue, Assumptions (use `N/A` if none), Alternatives (at least 2), Justification (for each), Implication (for each), and Agreeing Parties (from the dictionary).

**6. Specific Logic for "Remove":**

- If an AD is obsolete (e.g., based on a deprecated feature), recommend its **Removal**.
- State the reason clearly:
  `**[AD ID]: [Title]**`
  `* Action: Remove`
  `* Reason: [Briefly explain why, e.g., "Feature is deprecated in OCP X.X"]`

**7. Content & Accuracy:**

- Ensure no ADs mention or recommend deprecated features (unless marking for removal).
- Any feature identified as "Technology Preview" in the sources must be explicitly flagged with **(TP)** in the AD text if it is not already.

**8. Formatting Requirements:**

- Strictly follow this format for all fields: `**[Field Name]:** [Text]`.
  - Example: `**Assumptions:** The environment is disconnected.`
- When listing alternatives, justifications, etc., use bullet points.
- **Inject a blank line between bullet list items** to ensure clear, readable formatting in the output.
- Keep the AD ID and Title intact and together (e.g., `**OCP-BM-02: Title of AD**`) when reporting updates.
- Do not mix content from different ADs.

**9. Repeatability:**

- The prompt must be designed to be robust and repeatable, minimizing hallucinations or deviations when re-run after a context refresh in NotebookLM.
