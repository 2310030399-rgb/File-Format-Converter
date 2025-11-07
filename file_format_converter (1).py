import pandas as pd
import os

print("Current working directory:", os.getcwd())

def csv_to_json(csv_file, json_file):
    try:
        df = pd.read_csv(csv_file)
        df.to_json(json_file, orient='records', indent=4)
        print(f"Converted {csv_file} to {json_file}")
    except Exception as e:
        print(f"Error: {e}")

def json_to_csv(json_file, csv_file):
    try:
        df = pd.read_json(json_file)
        df.to_csv(csv_file, index=False)
        print(f"Converted {json_file} to {csv_file}")
    except Exception as e:
        print(f"Error: {e}")

def csv_to_parquet(csv_file, parquet_file):
    try:
        import pyarrow
        df = pd.read_csv(csv_file)
        df.to_parquet(parquet_file, engine='pyarrow', index=False)
        print(f"Converted {csv_file} to {parquet_file}")
    except ImportError:
        print("pyarrow is not installed. Please install it with 'pip install pyarrow'.")
    except Exception as e:
        print(f"Error: {e}")

def parquet_to_csv(parquet_file, csv_file):
    try:
        df = pd.read_parquet(parquet_file)
        df.to_csv(csv_file, index=False)
        print(f"Converted {parquet_file} to {csv_file}")
    except Exception as e:
        print(f"Error: {e}")

def json_to_parquet(json_file, parquet_file):
    try:
        import pyarrow
        df = pd.read_json(json_file)
        df.to_parquet(parquet_file, engine='pyarrow', index=False)
        print(f"Converted {json_file} to {parquet_file}")
    except ImportError:
        print("pyarrow is not installed. Please install it with 'pip install pyarrow'.")
    except Exception as e:
        print(f"Error: {e}")

def parquet_to_json(parquet_file, json_file):
    try:
        df = pd.read_parquet(parquet_file)
        df.to_json(json_file, orient='records', indent=4)
        print(f"Converted {parquet_file} to {json_file}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("File Format Converter")
    print("1. CSV to JSON")
    print("2. JSON to CSV")
    print("3. CSV to Parquet")
    print("4. Parquet to CSV")
    print("5. JSON to Parquet")
    print("6. Parquet to JSON")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        csv = input("Enter CSV file name: ")
        jsn = input("Enter output JSON file name: ")
        csv_to_json(csv, jsn)
    elif choice == '2':
        jsn = input("Enter JSON file name: ")
        csv = input("Enter output CSV file name: ")
        json_to_csv(jsn, csv)
    elif choice == '3':
        csv = input("Enter CSV file name: ")
        pq = input("Enter output Parquet file name: ")
        csv_to_parquet(csv, pq)
    elif choice == '4':
        pq = input("Enter Parquet file name: ")
        csv = input("Enter output CSV file name: ")
        parquet_to_csv(pq, csv)
    elif choice == '5':
        jsn = input("Enter JSON file name: ")
        pq = input("Enter output Parquet file name: ")
        json_to_parquet(jsn, pq)
    elif choice == '6':
        pq = input("Enter Parquet file name: ")
        jsn = input("Enter output JSON file name: ")
        parquet_to_json(pq, jsn)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()