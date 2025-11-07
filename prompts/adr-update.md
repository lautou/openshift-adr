You are an expert architect. Source: product docs (OCP, GitOps). Files: `GITOPS.md`, `OCP-BM.md`, `ad_parties_role_dictionnary.md`.

Review **only** `GITOPS.md` & `OCP-BM.md` against the docs. Report updates, removals, new ADs.

Use this exact format:

**1. ADs to Update**
(Rewrite all affected sections. Alts = titles only. Justification/Implications = titled.)

* **[AD ID]: [Title]**
    * **Updated Alternatives:**
        * [Alternative 1 Title]
    * **Updated Justification:**
        * **[Alt 1 Title]:** [Full text, corrected]
    * **Updated Implications:**
        * **[Alt 1 Title]:** [Full text, corrected]

**2. ADs to Remove**
(List obsolete ADs from GITOPS.md or OCP-BM.md.)

* **[AD ID]: [Title]**
    * Reason: [Briefly state why].

**3. ADs to Create**
(New ADs for OCP-BM or GitOps only. Full skeleton. Titled Justification/Implications.)

* **[Suggested AD ID]**: [Suggested Title]
    * Architectural Question: [Question].
    * Assumption: [N/A or context].
    * Alternatives:
        * [Alternative 1 Title]
        * [Alternative 2 Title]
    * Justification:
        * **[Alt 1 Title]:** [Justification text]
    * Implications:
        * **[Alt 1 Title]:** [Implication text]
    * Agreeing Parties (from `ad_parties_role_dictionnary.md`):
        * [Role 1]

**Rules:**
* Updates: Provide full rewritten text for sections.
* New ADs: Provide complete skeleton.
* **Format:** Alts = titles only. Justification/Implications = `**[Title]:** [Text]`.
* Scope: OCP-BM & GITOPS only.
* **ID Rule:** `GITOPS.md` (01-04), `OCP-BM.md` (01-02). MUST suggest next ID (e.g., `GITOPS-05`, `OCP-BM-03`). No ID reuse.
* Flags: Mark all Tech-Preview as `(TP)`.
