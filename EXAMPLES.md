# File Format Converter - Example Commands

## Basic Usage

### Show Help
```powershell
# Using full Python path
C:/Users/pasal/anaconda3/python.exe converter/main.py

# Or using module syntax
C:/Users/pasal/anaconda3/python.exe -m converter

# Or using __main__.py directly
C:/Users/pasal/anaconda3/python.exe converter/__main__.py
```

### Show Convert Command Help
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert --help
```

## Conversion Examples

### CSV to JSON
```powershell
# Convert CSV to JSON (pretty formatted)
C:/Users/pasal/anaconda3/python.exe converter/main.py convert my_input.csv output.json

# Convert CSV to JSON (compact format)
C:/Users/pasal/anaconda3/python.exe converter/main.py convert my_input.csv output.json --no-pretty-json
```

### JSON to CSV
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert my_output.json output.csv
```

### JSON to YAML
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert my_output.json config.yaml
```

### YAML to JSON
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert config.yaml data.json
```

### CSV to Excel (XLSX)
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert my_input.csv output.xlsx
```

### Excel (XLSX) to JSON
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert data.xlsx output.json
```

### Excel (XLSX) to CSV
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert data.xlsx output.csv
```

### Excel (XLSX) to YAML
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert data.xlsx config.yaml
```

## Using Different Paths

### Absolute Paths
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert "C:\Users\pasal\OneDrive\Desktop\FDE\my_input.csv" "C:\Users\pasal\OneDrive\Desktop\FDE\output.json"
```

### Relative Paths
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert ./my_input.csv ./output.json
```

### Output to Different Directory
```powershell
C:/Users/pasal/anaconda3/python.exe converter/main.py convert my_input.csv results/output.json
```

## Quick Reference

**Supported Input Formats:**
- `.json` - JSON files
- `.yaml` or `.yml` - YAML files
- `.csv` - CSV files
- `.xlsx` - Excel files

**Supported Output Formats:**
- `.json` - JSON files (pretty-printed by default)
- `.yaml` or `.yml` - YAML files
- `.csv` - CSV files
- `.xlsx` - Excel files

**Options:**
- `--no-pretty-json` - Disable pretty formatting for JSON output (compact format)

## Example Workflow

```powershell
# 1. Convert CSV to JSON
C:/Users/pasal/anaconda3/python.exe converter/main.py convert data.csv data.json

# 2. Convert JSON to YAML
C:/Users/pasal/anaconda3/python.exe converter/main.py convert data.json config.yaml

# 3. Convert YAML back to Excel
C:/Users/pasal/anaconda3/python.exe converter/main.py convert config.yaml spreadsheet.xlsx
```

