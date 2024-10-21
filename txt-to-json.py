import json

def txt_to_json(txt_file, json_file):
    data = {}
    
    with open(txt_file, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip()
    
    with open(json_file, 'w') as json_out:
        json.dump(data, json_out, indent=4)
    
    print(f"Data has been successfully written to {json_file}")

# Example usage
txt_file = 'input.txt'
json_file = 'output.json'
txt_to_json(txt_file, json_file)