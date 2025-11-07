## File Format Converter (CSV, JSON, YAML, XLSX)

Simple Python CLI to convert data files by extension.

- CSV ↔ JSON
- JSON ↔ YAML
- CSV ↔ XLSX

### Install

```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### CLI Usage

```bash
# General form
python -m converter convert INPUT.ext OUTPUT.ext

# Examples
python -m converter convert data/input.csv data/output.json
python -m converter convert data/input.json data/output.yaml
python -m converter convert data/input.csv data/output.xlsx
python -m converter convert data/input.xlsx data/output.csv

# Compact JSON
python -m converter convert input.json output.json --no-pretty-json
```

Notes:
- CSV expects a header row. Nested objects/lists are serialized to JSON strings in CSV.
- XLSX conversion requires `pandas` and `openpyxl`.

### Library Use

```python
from pathlib import Path
from converter.main import convert_file

convert_file(Path("input.csv"), Path("output.json"))
```

### Limitations
- CSV round-tripping of nested structures results in JSON-encoded strings in cells.
- Only the first sheet of XLSX is read/written.

## Web UI (Flask)

```bash
pip install -r requirements.txt
python web/app.py
# Open http://127.0.0.1:5000
```

- Upload a file and choose the target format (JSON/YAML/CSV/XLSX).
- Click Convert & Download to receive the converted file.


