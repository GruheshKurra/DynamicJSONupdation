import json
import mysql.connector
from mysql.connector import MySQLConnection, Error
import time

# Define a list of JSON file paths
json_files = [
    'C:\\Users\\akagr\\OneDrive\\Desktop\\XtraLeap\\Prototype.json',
    'C:\\Users\\akagr\\OneDrive\\Desktop\\XtraLeap\\prototype2.json',
]

def fetch_config_data():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="prototype"
        )
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
    rows = fetch_config_data()
    if not rows:
        return

    # Load existing JSON data from the file
    with open(json_file_path, 'r') as json_file:
        existing_data = json.load(json_file)

    # Merge database data into the existing JSON data
    for row in rows:
        environment = row['environment']
        section = row['section']
        key = row['key']
        value = row['value']
        if environment in existing_data and section in existing_data[environment] and key in existing_data[environment][section]:
            existing_data[environment][section][key] = value

    # Save the updated JSON data back to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)
    print(f"JSON file '{json_file_path}' updated successfully")

while True:
    for json_file_path in json_files:
        update_json_file(json_file_path)
    time.sleep(3600)
