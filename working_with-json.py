import json
import pandas as pd
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("The file was not found")
        return None
    except json.JSONDecodeError:
        print("Failed to decode JSON")
        return None
    
  

def remove_column(file_path, column_name):
    try:
        # Read the JSON file into a DataFrame
        data = pd.read_json(file_path)
        
        # Remove the specified column
        data = data.drop(column_name, axis=1)
        
        # Write the modified DataFrame back to the JSON file
        data.to_json(file_path, orient='records', lines=True, indent=4)
        
        print("Column successfully removed")
    except FileNotFoundError:
        print("The file was not found")
    except pd.errors.ParserError:
        print("Failed to parse JSON")


  def remov_column(file_path, column_name):
     try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            print("Error: Data is not a list of dictionaries")
            return
        
        for item in data:
            if column_name in item:
                del item[column_name]
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Column successfully removed")
    except FileNotFoundError:
        print("The file was not found")
    except json.JSONDecodeError:
        print("Failed to decode JSON")