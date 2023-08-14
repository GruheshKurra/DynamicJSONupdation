import json
import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Karthik9149111",
    database="prototype"
)
cursor = db.cursor()

# Define SQL statements
insert_sql = """
  INSERT INTO config (environment, section, `key`, value)
  VALUES (%s, %s, %s, %s)  
"""
update_sql = """
  UPDATE config 
  SET value = %s
  WHERE environment = %s AND section = %s AND `key` = %s
"""

# Load JSON data from file
with open(r"C:\Users\akagr\Downloads\Prototype.json") as f:
    data = json.load(f)

for env, env_config in data.items():
    for section, section_config in env_config.items():
        for key, value in section_config.items():
            # Check if row exists
            select_sql = "SELECT 1 FROM config WHERE environment = %s AND section = %s AND `key` = %s"
            cursor.execute(select_sql, (env, section, key))
            row = cursor.fetchone()

            if row:
                # Update existing row
                values = (value, env, section, key)
                cursor.execute(update_sql, values)
            else:
                # Insert new row
                values = (env, section, key, value)
                cursor.execute(insert_sql, values)

            # Modify the JSON data to reflect the database update
            section_config[key] = value

db.commit()
db.close()

output_file_path = r"C:\Users\akagr\Downloads\prototypejsontojson.json"
with open(output_file_path, "w") as f:
    json.dump(data, f, indent=2)

print("Database and JSON file updated.")
