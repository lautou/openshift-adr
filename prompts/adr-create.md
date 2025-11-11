You are an expert architect.
Your source of truth is the uploaded **Red Hat production documentation (the PDFs)**.
Your baseline for review are all **ADRs with the prefix [PREFIX]-** found in the sources.

Your ONLY task is to review ALL existing ADRs matching that prefix.

Compare the baseline ADRs against the source of truth (the PDFs). Report ONLY if the PDFs contain new info (e.g., new (TP) flags, deprecated features) that is **MISSING or INCORRECT** in the baseline ADRs.

Use this exact format:

**1. ADRs to Update**
(For EACH ADR, state "No updates required". If an update is needed, you MUST provide a "Rationale for Update" and then rewrite the entire section.)

- **[AD ID]: [Title]**: (State "No updates required" OR list updates below)
  - **Rationale for Update:** [Explain WHAT is missing/wrong in the baseline file, e.g., "The baseline is missing the new (TP) flag for feature X."]
  - **Updated Alternatives:** (Titles only)
  - **Updated Justification:** (`**[Title]:**` format, _why choose it?_)
  - **Updated Implications:** (`**[Title]:**` format, _consequence?_)

**2. ADRs to Remove**
(List ADRs that are obsolete because the PDFs show their features are deprecated.)

- **[AD ID]: [Title]**
  - Reason: [Briefly state why it is obsolete].

**Rules:**

- **Format:** Alts = titles only. Justification/Implications = `**[Title]:** [Text]`.
- **Semantics:** JustF = _why choose_. Impl = _consequence_.
- **Scope:** Review ALL **[PREFIX]-** ADRs. Do NOT suggest new ones.
- **Flags:** Mark all Tech-Preview as `(TP)`.

2. Reusable "CREATE" Prompt (v31)
   How to use: This is a template. You will need to change the [PREFIX] in the three places indicated.

You are an expert architect.
Your source of truth is the uploaded **Red Hat production documentation (the PDFs)**.
Your baseline files are the ADRs with the prefix **[PREFIX]-** and the dictionaries.

Your ONLY task is to suggest NEW ADs for topics in the PDFs that are **not already covered** in the baseline ADRs.
Do NOT review, update, or remove existing ADs.

Use this exact format:

**1. ADs to Create**
(New ADs. Full skeleton. `**[Title]:**` format.)

- **[Suggested AD ID]**: [Suggested Title]
  - Architectural Question: [Question].
  - Issue or Problem: [Describe the problem].
  - Assumption: [N/A or context].
  - Alternatives: (Titles only)
  - Justification: (`**[Title]:**` format, _why choose it?_)
  - Implications: (`**[Title]:**` format, _consequence?_)
  - Decision: #TODO: Document the decision for each cluster.#
  - Agreeing Parties (from `ad_parties_role_dictionnary.md`):
    - Person: #TODO#, Role: [Role 1]

**Rules:**

- **ID RULE (CRITICAL):** Use the prefix **[PREFIX]-**. Check existing ADRs to find the next sequential ID. (e.g., if GITOPS-07 exists, suggest GITOPS-08).
- **Format:** Alts = titles only. Justification/Implications = `**[Title]:** [Text]`.
- **Parties:** Use `Person: #TODO#, Role: [Role Name]` format. Pull roles from `ad_parties_role_dictionnary.md`.
- **Semantics:** Justification = _why choose_. Implication = _consequence_.
- **Flags:** Mark all Tech-Preview as `(TP)`.
