import json
import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prototype"
)
cursor = db.cursor()

# Define SQL statements
create_table_sql = """
CREATE TABLE IF NOT EXISTS config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    environment VARCHAR(255),
    section VARCHAR(255),
    `key` VARCHAR(255),
    value VARCHAR(255)
);
"""
insert_sql = """
INSERT INTO config (environment, section, `key`, value)
VALUES (%s, %s, %s, %s)  
"""
update_sql = """
UPDATE config 
SET value = %s
WHERE environment = %s AND section = %s AND `key` = %s
"""

# Create the table if it doesn't exist
cursor.execute(create_table_sql)

# Load JSON data from file
with open(r"C:\Users\akagr\OneDrive\Desktop\XtraLeap\Prototype.json") as f:
    data = json.load(f)

# Load the existing JSON data from file (json2)
with open(r"C:\Users\akagr\OneDrive\Desktop\XtraLeap\prototype2.json", "r") as f:
    json2 = json.load(f)

# Dictionary to keep track of updated values
updated_values = {}

for env, env_config in data.items():
    for section, section_config in env_config.items():
        for key, value in section_config.items():
            # Check if row exists
            select_sql = "SELECT value FROM config WHERE environment = %s AND section = %s AND `key` = %s"
            cursor.execute(select_sql, (env, section, key))
            row = cursor.fetchone()

            if row:
                # Compare current value with existing value
                if row[0] != value:
                    # Update existing row
                    values = (value, env, section, key)
                    cursor.execute(update_sql, values)
                    updated_values[(env, section, key)] = value
            else:
                # Insert new row
                values = (env, section, key, value)
                cursor.execute(insert_sql, values)

# Commit and close the database connection
db.commit()
db.close()

# Update json2 with the data from the database
for (env, section, key), value in updated_values.items():
    if env in json2 and section in json2[env] and key in json2[env][section]:
        json2[env][section][key] = value

# Save the updated json2 data back to the file
with open(r"C:\Users\akagr\OneDrive\Desktop\XtraLeap\prototype2.json", "w") as f:
    json.dump(json2, f, indent=4)

print("Database updated and JSON file updated.")
