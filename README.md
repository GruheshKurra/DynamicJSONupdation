## Dynamic JSON Updation


### Step 1:Open MySQL or MySQL in XAMPP Server

Code to Create a database.
```sql
CREATE DATABASE prototype;
```

### Step 2:Use the Database

Code to use the database.
```sql
use prototype;
```

### Step 3:Create a table to store the JSON data.

Code to Create a SQL table(config).
```sql
CREATE TABLE IF NOT EXISTS config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    environment VARCHAR(255),
    section VARCHAR(255),
    `key` VARCHAR(255),
    value VARCHAR(255)
);

```

### Step 4:Making Changes

Download both JSON files and change the path in the python code aswell

### Step 5:Pycharm

Go to project settings in the python and click on the python Interpreter and add "mysql-connector-python" extension to the project 

### Step 6:Run Python code

```python
import json
import mysql.connector
from mysql.connector import MySQLConnection, Error
import time

# Define a list of JSON file paths
json_files = [
    'C:\\Users\\karth\\Desktop\\Files\\xtraleap\\finalfiles\\Prototype.json',
    'C:\\Users\\karth\\Desktop\\Files\\xtraleap\\finalfiles\\prototype2.json',
]

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "prototype"
}

def fetch_config_data():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM config")
            rows = cursor.fetchall()
            return rows
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
    return []

def update_json_file(json_file_path):
    try:
        rows = fetch_config_data()
        if not rows:
            return

        # Load existing JSON data from the file
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)

        # Check for new rows and add them to the existing JSON data
        for row in rows:
            environment = row['environment']
            section = row['section']
            key = row['key']
            value = row['value']
            if environment not in existing_data:
                existing_data[environment] = {}
            if section not in existing_data[environment]:
                existing_data[environment][section] = {}
            if key not in existing_data[environment][section]:
                existing_data[environment][section][key] = value

        # Save the updated JSON data back to the file
        with open(json_file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)
        print(f"JSON file '{json_file_path}' updated successfully")
    except Exception as e:
        print(f"Error updating JSON file '{json_file_path}': {e}")

def print_menu():
    print("\nMenu:")
    print("1. Add File Location")
    print("2. View File List")
    print("3. Remove File Location")
    print("4. Update JSON File (All)")
    print("5. Update Specific JSON File")
    print("6. View Database Configuration")
    print("7. Change Database Configuration")
    print("8. Help")
    print("0. Exit")

def add_file_location():
    file_location = input("Enter the file location: ").strip()
    json_files.append(file_location)
    print(f"File location '{file_location}' added successfully.")

def view_file_list():
    print("\nFile List:")
    for i, file_path in enumerate(json_files, start=1):
        print(f"{i}. {file_path}")

def remove_file_location():
    view_file_list()
    if json_files:
        file_index = input("Enter the file index to remove (0 to go back): ").strip()
        if file_index == '0':
            return
        try:
            file_index = int(file_index)
            if 1 <= file_index <= len(json_files):
                removed_file = json_files.pop(file_index - 1)
                print(f"File location '{removed_file}' removed successfully.")
            else:
                print("Invalid file index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No file locations to remove.")

def view_database_config():
    print("\nDatabase Configuration:")
    for key, value in db_config.items():
        print(f"{key.capitalize()}: {value}")

def change_database_config():
    global db_config
    print("Current Database Configuration:")
    view_database_config()
    for key in db_config:
        new_value = input(f"Enter new {key.capitalize()} (press Enter to keep current value, 0 to go back): ").strip()
        if new_value == '0':
            return
        if new_value:
            db_config[key] = new_value
    print("Database configuration updated successfully.")

def display_help():
    print("\nHelp:")
    print("1. Add File Location: Add a new JSON file location to the list.")
    print("2. View File List: Display the list of currently added JSON file locations.")
    print("3. Remove File Location: Remove a JSON file location from the list.")
    print("4. Update JSON File (All): Update all JSON files with data from the database.")
    print("5. Update Specific JSON File: Update a specific JSON file with data from the database.")
    print("6. View Database Configuration: Display the current database connection details.")
    print("7. Change Database Configuration: Change the database connection details.")
    print("8. Help: Display help instructions.")
    print("0. Exit: Exit the program.")

while True:
    print_menu()
    choice = input("Enter your choice (0-8): ").strip()

    if choice == '1':
        add_file_location()
    elif choice == '2':
        view_file_list()
    elif choice == '3':
        remove_file_location()
    elif choice == '4':
        if not json_files:
            print("No file locations added. Please add a file location first.")
        else:
            for file_path in json_files:
                update_json_file(file_path)
    elif choice == '5':
        if not json_files:
            print("No file locations added. Please add a file location first.")
        else:
            print("Select a file to update:")
            view_file_list()
            file_index = input("Enter the file index to update (0 to go back): ").strip()
            if file_index == '0':
                continue
            try:
                file_index = int(file_index)
                if file_index == 0:
                    for file_path in json_files:
                        update_json_file(file_path)
                elif 1 <= file_index <= len(json_files):
                    update_json_file(json_files[file_index - 1])
                else:
                    print("Invalid file index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == '6':
        view_database_config()
    elif choice == '7':
        change_database_config()
    elif choice == '8':
        display_help()
    elif choice == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    time.sleep(1)  # Delay for one second between menu displays


```

