import json
import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sushma",
    database="prototype"
)
cursor = db.cursor()

# Define SQL statements
insert_sql = """
  INSERT INTO config (environment, section, key, value, is_updated)
  VALUES (%s, %s, %s, %s, 1)  
"""
update_sql = """
  UPDATE config 
  SET value = %s, is_updated = 1
  WHERE environment = %s AND section = %s AND key = %s
"""
check_value_sql = """
  SELECT value FROM config 
  WHERE environment = %s AND section = %s AND key = %s
"""

# Load JSON data from file (json1)
with open(r"C:\Users\sushm\Downloads\json_1.json") as f:
    data = json.load(f)

# Update or insert the values from json1 into the database only if they've changed
for env, env_config in data.items():
    for section, section_config in env_config.items():
        for key, value in section_config.items():
            print(f"Processing env: {env}, section: {section}, key: {key}")  # <-- ADDED
            cursor.execute(check_value_sql, (env, section, key))
            row = cursor.fetchone()

            if row:
                # If the value is different in the database, update it and set is_updated to 1
                if str(row[0]) != str(value):  # Convert both to string for comparison
                    print(f"Updating value for env: {env}, section: {section}, key: {key}")  # <-- ADDED
                    cursor.execute(update_sql, (value, env, section, key))
            else:
                print(f"Inserting value for env: {env}, section: {section}, key: {key}")  # <-- ADDED
                cursor.execute(insert_sql, (env, section, key, value))

# Load json2 data from file
with open(r"C:\Users\sushm\Downloads\json_2.json", "r") as f:
    json2 = json.load(f)

# Fetch the updated values from the database
select_updated_sql = "SELECT environment, section, key, value FROM config WHERE is_updated = 1"
cursor.execute(select_updated_sql)
updated_values_from_db = cursor.fetchall()

# Update json2 with the fetched values (only if they exist in json2)
for env, section, key, value in updated_values_from_db:
    if env in json2 and section in json2[env] and key in json2[env][section]:
        print(f"Updating json2 for env: {env}, section: {section}, key: {key}")  # <-- ADDED
        json2[env][section][key] = value

# Save the updated json2 data back to the file
with open(r"C:\Users\sushm\Downloads\json_2.json", "w") as f:
    json.dump(json2, f, indent=4)

# Reset the is_updated column for all rows
reset_sql = "UPDATE config SET is_updated = 0"
cursor.execute(reset_sql)

# Commit and close the database connection
db.commit()
db.close()

print("Database and JSON file updated.")
