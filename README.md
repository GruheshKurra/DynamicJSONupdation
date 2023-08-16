## Dynamic JSON Updation

### config table
Code to Create a SQL table.
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
