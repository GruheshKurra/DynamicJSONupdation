## Dynamic JSON Updation

### config table

### Step 1:Open your MySQL or MySQL in XAMPP Server
Code to Create a database.
```sql
CREATE DATABASE prototype;
```

### Step 2:Use the Database
Code to use the database.
```sql
CREATE DATABASE prototype;
```

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
