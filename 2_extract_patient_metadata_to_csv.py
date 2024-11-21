# %% [markdown]
# # Extract the Patient Metadata

# %%
import json
import csv
import os

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_data(json_data):
    """Extract data from the first entry in the JSON into a flat dictionary."""
    results = {}
    # Focus on the first entry only, if it exists
    entry = json_data.get('entry', [{}])[0]  # Default to empty dict if no entries

    # Recursive function to handle nested dictionaries
    def flatten(data, prefix=''):
        if isinstance(data, dict):
            for key, value in data.items():
                flatten(value, f"{prefix}{key}_")
        elif isinstance(data, list):
            for i, item in enumerate(data):
                flatten(item, f"{prefix}{i}_")
        else:
            results[prefix[:-1]] = data

    flatten(entry)
    return results

def write_to_csv(data_list, headers, output_file):
    """Write a list of dictionaries to a CSV file."""
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)

def process_directory(directory_path, output_csv):
    """Process all JSON files in the directory and compile them into one CSV file."""
    all_data = []
    fieldnames_set = set()

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            json_path = os.path.join(directory_path, filename)
            json_data = load_json(json_path)
            extracted_data = extract_data(json_data)
            all_data.append(extracted_data)
            fieldnames_set.update(extracted_data.keys())

    write_to_csv(all_data, sorted(list(fieldnames_set)), output_csv)

# Example usage
directory_path = '/home/cdsw/patient-records-jsons/'
output_csv = '/home/cdsw/hl7_patient_pii.csv'
process_directory(directory_path, output_csv)



