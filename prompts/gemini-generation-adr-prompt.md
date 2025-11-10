You are Gemini, my helpful AI assistant.

I am a Red Hat Consulting Architect. My goal is to maintain an Architecture Decision Records (ADR) repository for my OCP designs using NotebookLM.

We have already completed a long troubleshooting process and established a final, reliable workflow. I need you to regenerate the two (2) final, generic prompts we created, based on the key lessons we learned.

**ADR Structure Reference (This is what I need in my files):**

- **ID:** Unique, using a prefix (e.g., `GITOPS-01`).
- **Title:** A concise title.
- **Architectural Question:** The core question the ADR answers.
- **Issue or Problem:** The problem statement.
- **Assumption:** Context/conditions (can be `N/A`).
- **Alternatives:** At least two options.
- **Justification:** The "why choose it?" for each alternative.
- **Implications:** The "consequence/risk" for each alternative.
- **Decision:** ` #TODO: Document the decision for each cluster.#`
- **Agreeing Parties:** A list of roles (e.g., `Person: #TODO#, Role: Enterprise Architect`).

**Our Key Lessons (Please recall this context):**

1.  **"Noisy" Notebooks Fail:** Uploading all 100+ PDF docs into one notebook with all `.md` files causes the AI to be "lazy" and fail to read the full content of the `.md` files.
2.  **"Focused Notebooks" are the Solution:** The only reliable method is to create a separate, focused NotebookLM for each topic (e.g., a "GitOps Notebook" with only the GitOps PDF docs, the `GITOPS.md` file, and the two dictionary files).
3.  **"All-in-One" Prompts Fail:** A single prompt for updating, removing, and creating is non-deterministic and produces "false positives" (reporting existing text as a new update).
4.  **A Two-Prompt System is Required:** We must use two separate, generic prompts: one for `UPDATE/REMOVE` and one for `CREATE`.

---

**My Task:**

Please generate the two (2) generic, reusable NotebookLM prompts (each **under 2000 characters**) that we finalized.

**1. Generate the "UPDATE/REMOVE" Prompt (v30)**
Generate the generic prompt for reviewing existing ADRs. This prompt must:

- Be a template that uses a `[PREFIX]` placeholder (e.g., `GITOPS-`).
- Assume the user is in a "focused notebook."
- Define the "PDFs" as the source of truth and the "ADRs with prefix [PREFIX]-" as the baseline.
- Instruct the AI to find only `MISSING or INCORRECT` info.
- **Crucially:** Require a `Rationale for Update:` field to prevent the "false positive" circular logic error.
- Demand that any updated section be **rewritten in full**, not as a "delta chunk."
- Follow our agreed-upon format (`**[Title]:**`, `Alts = titles only`, etc.).

**2. Generate the "CREATE" Prompt (v31)**
Generate the generic prompt for suggesting new ADRs. This prompt must:

- Be a template that uses a `[PREFIX]` placeholder.
- Instruct the AI to find the _next sequential ID_ for that prefix (by checking the existing ADRs).
- Generate the _full skeleton_ for a new AD, based on the **ADR Structure Reference** provided above.
- Reference the `ad_parties_role_dictionnary.md` and use the `Person: #TODO#, Role: [Role Name]` format.
- Follow our agreed-upon format (`**[Title]:**`, `Alts = titles only`, etc.).

---

Please provide these two generic prompts so I can save them as my final, repeatable workflow.
