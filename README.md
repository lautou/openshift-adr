# ADR Repository Maintenance with NotebookLM

This document outlines the official workflow for creating and maintaining Architecture Decision Records (ADRs) using a "Focused Notebook" strategy in NotebookLM.

## 1. The Core Strategy

The reliability of the AI prompts depends on a **"Focused Notebook"**. A "noisy" notebook with all product documentation for all topics will produce unreliable results.

To review or create ADRs, you MUST create a dedicated NotebookLM and upload _only_ the following:

- The ADR md files.
- The `ad_prefix_dictionary.md` file.
- The `ad_parties_role_dictionnary.md` file.
- The official Red Hat documentation (PDFs).

Repeat this process for each topic (e.g., an "OCP-BM Notebook" with only `OCP-BM.md` and OCP Bare Metal docs).

## 2. The Prompts

This workflow uses two separate, reusable prompts. One for reviewing existing ADs and one for creating new ones.

---

### Task 1: Updating or Removing Existing ADRs

Use this prompt to check if your existing ADRs are out-of-date or obsolete.

**Recommended Process:**

1.  In your focused notebook, set the `[PREFIX]` in the prompt below.
2.  Run the prompt.
3.  **This prompt can return "false positives."** The most reliable method is to clear the context and re-run the prompt until you receive a stable "No updates required" result at least two times consecutively. This confirms your file is 100% in sync.

---

### Task 2: Creating New ADRs

Use this prompt to discover new features in the documentation and generate a skeleton for a new ADR.

**Recommended Process:**

1.  In your focused notebook, set the `[PREFIX]` in the prompt below.
2.  Run the prompt. A single run is usually sufficient.
3.  Copy the generated skeleton into your `.md` file.
