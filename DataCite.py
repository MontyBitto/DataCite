import gzip
import json

subjects = []

# Read the entire file content
with gzip.open('output25.json.gz', 'rt', encoding='utf-8') as f:
    try:
        data = json.load(f) 
        for obj in data:
            if 'subjects' in obj and obj['subjects']:
                subjects.extend(obj['subjects'])
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

print(subjects)

