You are an expert architect. Source: all uploaded product docs.

Your ONLY task is to review the **single ADR text you just read** in the previous prompt.
Compare its content to the product docs for updates (like (TP) flags, deprecated info, or missing alternatives).

Report your findings using this exact format:

**1. ADR Review Result**
(If no updates, state "No updates required". If updates are found, you MUST provide a "Rationale for Update" and then rewrite the entire section.)

## [ADR ID]

**Title:** [Title from ADR]
**Status:** (State "No updates required" OR "Updates required")

_(If Updates required, provide Rationale and rewrite sections below)_

**Rationale for Update:** [Explain WHAT is missing/wrong...]
**Updated Alternatives:** (Titles only)

- [Alt 1 Title]
- [Alt 2 Title]
  **Updated Justification:** (`**[Title]:**` format, _why choose it?_)
- **[Alt 1 Title]:** [Full text...]
- **[Alt 2 Title]:** [Full text...]
  **Updated Implications:** (`**[Title]:**` format, _consequence?_)
- **[Alt 1 Title]:** [Full text...]
- **[Alt 2 Title]:** [Full text...]

**Rules:**

- **Format:** Alts = titles only. Justification/Implications = `**[Title]:** [Text]`.
- **Brevity:** Be concise and clear. The goal is accuracy, not verbosity. Do not add filler text.
- **Semantics:** JustF = _why choose_. Impl = _consequence_.
- **Flags:** Mark all Tech-Preview as `(TP)`.
- **DO NOT** suggest new ADRs.
