# File Format Converter
A simple Python tool to convert datasets between CSV, JSON, and Parquet formats using Pandas and PyArrow.

Features
Convert CSV → JSON / Parquet
Convert JSON → CSV / Parquet
Convert Parquet → CSV / JSON
Lightweight and easy to extend
Supports structured data for data engineering and analytics
Technologies Used
Python 3.x
Pandas (data handling)
PyArrow (Parquet format support)
Installation
Clone or download this repository:
git clone https://github.com/yourusername/file-format-converter.git
cd file-format-converter
Install dependencies:
pip install pandas pyarrow
Usage
1. Import and Use in Python
from file_format_converter import (
    csv_to_json, json_to_csv, csv_to_parquet,
    parquet_to_csv, json_to_parquet, parquet_to_json
)

# Convert CSV to JSON
csv_to_json("sample.csv", "output.json")

# Convert JSON to CSV
json_to_csv("sample.json", "output.csv")
2. Example Files
sample.csv
sample.json
Use them to test conversions directly.

Future Enhancements
Command-Line Interface (CLI) support
GUI for drag-and-drop file conversion
Support for additional formats (Excel, Avro)
Error handling and logging
Project Structure
file-format-converter/
│── file_format_converter.py   # Conversion logic
│── sample.csv                 # Example CSV file
│── sample.json                # Example JSON file
│── README.md                  # Documentation
