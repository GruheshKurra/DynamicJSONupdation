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
CREATE TABLE config (
  id INT AUTO_INCREMENT PRIMARY KEY,
  environment VARCHAR(255),
  section VARCHAR(255),
  `key` VARCHAR(255), 
  value VARCHAR(255),
  flag INT DEFAULT 0
);
```

### Step 4:Making Changes

Download both JSON files and change the path in the python code aswell

### Step 5:Pycharm

Go to project settings in the python and click on the python Interpreter and add "mysql-connector-python" extension to the project 

### Step 6:Main Optimized Code

```python
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

```

### Step 6:Run Python code

```python
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
create_table_sql = """
CREATE TABLE IF NOT EXISTS config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    environment VARCHAR(255),
    section VARCHAR(255),
    `key` VARCHAR(255),
    value VARCHAR(255),
    flag INT DEFAULT 0
);
"""
insert_sql = """
INSERT INTO config (environment, section, `key`, value)
VALUES (%s, %s, %s, %s)  
"""
update_sql = """
UPDATE config 
SET value = %s, flag = 1
WHERE environment = %s AND section = %s AND `key` = %s
"""
reset_flags_sql = """
UPDATE config
SET flag = 0
"""

# Create the table if it doesn't exist
cursor.execute(create_table_sql)

# Reset all flags to 0 before processing updates
cursor.execute(reset_flags_sql)
db.commit()

# Load JSON data from file
with open(r"C:\Users\akagr\Downloads\Prototype.json") as f:
    data = json.load(f)

# Load the existing JSON data from file (json2)
with open(r"C:\Users\akagr\Downloads\prototype2.json", "r") as f:
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
with open(r"C:\Users\akagr\Downloads\prototype2.json", "w") as f:
    json.dump(json2, f, indent=4)

print("Database updated and JSON file updated.")

```

