import json
import os

def clean_databricks_docs():
    # Read the original JSON file
    input_file = 'data/documents/raw/Databricks_docs.json'
    output_file = 'data/documents/cleaned/Databricks_docs_cleaned.json'
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract only the markdown fields
    cleaned_data = []
    for item in data:
        if 'markdown' in item:
            cleaned_data.append({
                'markdown': item['markdown']
            })
    
    # Write the cleaned data to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    clean_databricks_docs() 