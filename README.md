## Dynamic JSON Updation

### config table

-- Step 1: Open your MySQL or MySQL in XAMPP Server

-- Code to create a database
CREATE DATABASE prototype;

```sql
CREATE DATABASE prototype;
```

### Step 2:Use the Database

Code to use the database.
```sql
CREATE DATABASE prototype;
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
