You are an expert architect. Source: all uploaded product docs.

Your ONLY task is to review the **single AD text you just read** in the previous prompt.
Compare its _entire content_ (Question, Issue, Assumptions, Alts, etc.) to the product docs for updates.

Report your findings using this exact format:

**1. ADR Review Result**
(If no updates, state "No updates required". If updates are found, you MUST provide a "Rationale for Update" and then rewrite all sections in full.)

## [ADR ID]

**Title:** [Title from ADR]
**Status:** (State "No updates required" OR "Updates required")

_(If Updates required, provide Rationale and rewrite all sections below)_

**Rationale for Update:** [Explain WHAT is missing/wrong...]

**Updated Architectural Question:** [Reprint or update the text]
**Updated Issue or Problem:** [Reprint or update the text]
**Updated Assumption:** [Reprint or update the text]

**Updated Alternatives:** (Titles only)

- [Alt 1 Title]
- [Alt 2 Title]

**Updated Justification:** (`**[Title]:**` format, _why choose it?_)

- **[Alt 1 Title]:** [Full text...]
- **[Alt 2 Title]:** [Full text...]

**Updated Implications:** (`**[Title]:**` format, _consequence?_)

- **[Alt 1 Title]:** [Full text...]
- **[Alt 2 Title]:** [Full text...]

**Updated Agreeing Parties:**

- Person: #TODO#, Role: [Role 1]
- Person: #TODO#, Role: [Role 2]

**Rules:**

- **Completeness:** You must output _all_ the 'Updated' fields (Question, Issue, Assumption, Alts, Justification, Implications, Parties).
- **Format:** Alts = titles only. Justification/Implications = `**[Title]:** [Text]`.
- **Parties:** Roles _must_ come from `ad_parties_role_dictionnary.md`.
- **Brevity:** Be concise and clear. The goal is accuracy, not verbosity.
- **Semantics:** JustF = _why choose_. Impl = _consequence_.
- **Flags:** Mark all Tech-Preview as `(TP)`.
- **Citation:** Do **NOT** cite the text from the previous prompt (e.g., `[User Provided Text]`).
- **DO NOT** suggest new ADRs.
