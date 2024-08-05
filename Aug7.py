import json

def read_data(file_path):
    """Reads JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return None

def process_data(data):
    """Processes the data (e.g., filtering out even numbers)."""
    if not isinstance(data, list):
        print("Error: Expected a list of numbers.")
        return None

    # Example processing: Filter even numbers
    processed_data = [num for num in data if num % 2 == 0]
    return processed_data

def write_data(file_path, data):
    """Writes the processed data to a file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully written to {file_path}.")
    except IOError:
        print(f"Error: Failed to write data to {file_path}.")

def main():
    input_file = 'input_data.json'
    output_file = 'output_data.json'

    # Read data from a file
    data = read_data(input_file)
    if data is None:
        return

    # Process the data
    processed_data = process_data(data)
    if processed_data is None:
        return

    # Write the processed data to a file
    write_data(output_file, processed_data)

if __name__ == "__main__":
    main()
