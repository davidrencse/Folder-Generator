```md
# CSV Folder Generator

A small Python utility that generates realistic-looking “tech project” folder names from a topic CSV wordlist and creates them inside an `output/` directory under a base path you provide.

## What It Does

- Prompts you to choose a topic:
  - Computer Architecture
  - Object Oriented Programming
  - Operating Systems
  - Data Structures
  - Computer Networking
- Loads the matching CSV file (expects a `word` column).
- Randomly generates folder names using:
  - one CSV entry + number, or
  - two CSV entries + suffix + number, or
  - one CSV entry + suffix + number
- Sanitizes names to be Windows-safe.
- Creates the folders in:

`<BASE_PATH>\output\`

Example:
- Base path: `E:\comp architecture`
- Output created in: `E:\comp architecture\output\`

## Files

Recommended repo layout:

```


````

## Requirements

- Python 3.10+ (uses `match/case`)
- No third-party packages required.

## CSV Format

Each topic CSV must include a header named `word`:

```csv
word
Cache Memory Hierarchy Project
Virtual Memory Paging Notes
Binary Tree Traversal Suite Project
````

## Usage

1. Put `main.py` and the CSV files in the same folder.
2. Run:

```bash
python main.py
```

3. Follow the prompts:

* Select a topic number (1–5)
* Enter a base directory (example: `E:\comp architecture`)
* Enter a folder count (default: 88)

Folders will be created in:

`<BASE_PATH>\output\`

## Configuration

### Change the default folder count

In `main.py`, change:

```python
folder_count = 88
```

### Change naming style

In `generate_folder_names()`:

* Edit the `suffixes` list
* Adjust the patterns used to build names
* Change the number format if desired

### Change output directory name

Output currently goes to:

```python
output_dir = os.path.join(base_dir, "output")
```

Rename `"output"` to anything you want (e.g., `"generated"`).

## Behavior Notes

* The generator avoids duplicate names during a single run.
* If a folder already exists, it is skipped.
* Names are sanitized to remove illegal filesystem characters.
* Basic Windows reserved names are avoided (`CON`, `PRN`, `AUX`, `NUL`).

## License

MIT
