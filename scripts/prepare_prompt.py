#!/usr/bin/env python3
import re
import sys
import argparse
from pathlib import Path

# --- Configuration (Relative to project root) ---
ADR_DIRECTORY = "adr"
PROMPT_DIRECTORY = "prompts"
PROMPT_TEMPLATE_FILENAME = "template-adr-update-load.md"
CHAR_LIMIT = 1950  # A safe buffer below 2000

def main():
    # --- Path Setup ---
    try:
        script_path = Path(__file__).resolve()
        project_root = script_path.parent.parent
    except NameError:
        # Fallback for environments where __file__ is not defined
        project_root = Path.cwd()

    adr_dir = project_root / ADR_DIRECTORY
    prompt_dir = project_root / PROMPT_DIRECTORY

    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(
        description="Generate a set of 'LOAD' prompts for reviewing ADRs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage (run from project root '~/workspace/adr'):
  ./scripts/prepare_prompt.py OCP-BM
  (This finds 'prompts/template-adr-update-load.md', 'adr/OCP-BM.md', 
   and generates one 'LOAD' prompt for EACH ADR found.)
"""
    )
    parser.add_argument(
        "prefix_base",
        type=str,
        help="The base prefix for the ADRs (e.g., OCP-BM, GITOPS, LOG)"
    )
    args = parser.parse_args()

    # --- Variable Derivation ---
    prefix_base = args.prefix_base
    filename_str = f"{prefix_base}.md"
    prefix_for_regex = f"{prefix_base}-"
    
    filename_path = adr_dir / filename_str
    prompt_template_path = prompt_dir / PROMPT_TEMPLATE_FILENAME

    # --- Read ADR File ---
    if not filename_path.exists():
        print(f"Error: ADR file not found at '{filename_path}'", file=sys.stderr)
        sys.exit(1)
    try:
        adr_content = filename_path.read_text()
    except Exception as e:
        print(f"Error: Could not read file {filename_path}: {e}", file=sys.stderr)
        sys.exit(1)

    # --- Read Prompt Template File ---
    if not prompt_template_path.exists():
        print(f"Error: Prompt template not found at '{prompt_template_path}'", file=sys.stderr)
        sys.exit(1)
    try:
        prompt_template_content = prompt_template_path.read_text()
    except Exception as e:
        print(f"Error: Could not read file {prompt_template_path}: {e}", file=sys.stderr)
        sys.exit(1)

    # --- **BUG 1 FIX**: Use finditer to slice, not split ---
    # This pattern finds the *start* of each ADR block
    pattern = re.compile(
        r"^\#\#\s*{prefix}\S+".format(prefix=re.escape(prefix_for_regex)),
        re.MULTILINE | re.IGNORECASE
    )
    
    matches = list(pattern.finditer(adr_content))
    
    if not matches:
        print(f"Error: No ADRs with prefix '{prefix_for_regex}' found in {filename_str}.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Found {len(matches)} ADRs in {filename_str}. Generating 'LOAD' prompts...\n")

    # --- Iterate through matches and slice the content ---
    for i, current_match in enumerate(matches):
        start_index = current_match.start()
        
        # Find the end index (start of next ADR or end of file)
        end_index = len(adr_content)
        if i + 1 < len(matches):
            end_index = matches[i + 1].start()
            
        # Slice the full ADR text block
        adr_full_text_raw = adr_content[start_index:end_index]
        
        # **BUG 2 FIX**: Clean the sliced block by splitting on the "---" separator
        # and taking the first part.
        adr_text_cleaned = adr_full_text_raw.split("\n---\n")[0].strip()
        
        # Get the ID for the warning/end marker
        ad_id_match = re.search(r"^\#\#\s*(\S+)", adr_text_cleaned)
        ad_id = ad_id_match.group(1) if ad_id_match else "UNKNOWN_ADR"

        # Fill the template
        final_prompt = prompt_template_content.format(ADR_FULL_TEXT=adr_text_cleaned)
        prompt_len = len(final_prompt)

        # --- Print Warning (if over limit) ---
        if prompt_len > CHAR_LIMIT:
            print(
                f"# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                f"# WARNING: ADR '{ad_id}' IS TOO LONG ({prompt_len} characters).\n"
                f"# The 2000-char limit will be exceeded. You must review this ADR\n"
                f"# manually using the 'Abridged Review (v25)' prompt.\n"
                f"# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n"
            )
        else:
            # --- **REQUEST 2 FIX**: Add the START marker ---
            print(f"# --- START OF PROMPT FOR {ad_id} ---")
            # Print the ready-to-use prompt
            print(final_prompt.strip())
            print(f"# --- END OF PROMPT FOR {ad_id} ---\n# (Copy the text above, paste in NotebookLM, then use 'prompts/adr-update-review.md')\n")

if __name__ == "__main__":
    main()