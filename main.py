import json

# Function to load the JSON file
def load_json(filename='main.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save the JSON data
def save_json(data, filename='main.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add a line to a category
def add_line(category, line, filename='main.json'):
    data = load_json(filename)
    if category not in data:
        data[category] = []
    data[category].append(line)
    save_json(data, filename)

# Function to delete a line from a category
def delete_line(category, line, filename='main.json'):
    data = load_json(filename)
    if category in data and line in data[category]:
        data[category].remove(line)
        save_json(data, filename)

# Function to display current categories and lines
def display_data(filename='main.json'):
    data = load_json(filename)
    for category, lines in data.items():
        print(f"{category}:")
        for line in lines:
            print(f"  - {line}")
        print()

# Example usage
if __name__ == '__main__':
    while True:
        print("Options:")
        print("1. Add line")
        print("2. Delete line")
        print("3. View current data")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter the category (standard, ultra, academic): ")
            line = input("Enter the line to add: ")
            add_line(category, line)
        elif choice == '2':
            category = input("Enter the category (standard, ultra, academic): ")
            line = input("Enter the line to delete: ")
            delete_line(category, line)
        elif choice == '3':
            display_data()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")
