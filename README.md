{
  "development": {
    "database": {
      "connectionString": "Server=(devdb)\\mssqllocaldb;Database=IdentityServer4Admin;Trusted_Connection=True;MultipleActiveResultSets=true",
      "maxConnections": 50,
      "timeout": 30,
      "backupEnabled": true,
      "backupFrequency": "daily"
    },
    "logging": {
      "level": "debug",
      "logToFile": true,
      "logFilePath": "/var/log/app_dev.log",
      "maxFileSize": "10MB"
    },
    "api": {
      "baseUrl": "http://api.dev.example.com",
      "timeout": 5000,
      "corsEnabled": true,
      "maxRequestPerMinute": 1000
    },
    "email": {
      "smtpServer": "smtp.dev.example.com",
      "port": 587,
      "username": "user@example.com",
      "password": "dev_email_password",
      "senderEmail": "noreply@dev.example.com",
      "defaultTemplate": "default_template.html"
    },
    "cache": {
      "enabled": true,
      "maxSize": "100MB",
      "expirationTime": 600
    }
  },
  "QA": {
    "database": {
      "connectionString": "Server=(qadb)\\mssqllocaldb;Database=IdentityServer4Admin;Trusted_Connection=True;MultipleActiveResultSets=true",
      "maxConnections": 100,
      "timeout": 20,
      "backupEnabled": true,
      "backupFrequency": "weekly"
    },
    "logging": {
      "level": "info",
      "logToFile": true,
      "logFilePath": "/var/log/app_qa.log",
      "maxFileSize": "5MB"
    },
    "api": {
      "baseUrl": "http://api.qa.example.com",
      "timeout": 3000,
      "corsEnabled": false,
      "maxRequestPerMinute": 500
    },
    "email": {
      "smtpServer": "smtp.qa.example.com",
      "port": 587,
      "username": "user@example.com",
      "password": "qa_email_password",
      "senderEmail": "noreply@qa.example.com",
      "defaultTemplate": "default_template.html"
    },
    "cache": {
      "enabled": true,
      "maxSize": "50MB",
      "expirationTime": 900
    }
  },
  "production": {
    "database": {
      "connectionString": "Server=(proddb)\\mssqllocaldb;Database=IdentityServer4Admin;Trusted_Connection=True;MultipleActiveResultSets=true",
      "maxConnections": 200,
      "timeout": 15,
      "backupEnabled": true,
      "backupFrequency": "monthly"
    },
    "logging": {
      "level": "warning",
      "logToFile": false,
      "maxFileSize": "20MB"
    },
    "api": {
      "baseUrl": "https://api.example.com",
      "timeout": 1000,
      "corsEnabled": true,
      "maxRequestPerMinute": 2000
    },
    "email": {
      "smtpServer": "smtp.example.com",
      "port": 587,
      "username": "user@example.com",
      "password": "prod_email_password",
      "senderEmail": "noreply@example.com",
      "defaultTemplate": "default_template.html"
    },
    "cache": {
      "enabled": true,
      "maxSize": "200MB",
      "expirationTime": 1200
    }
  }
}
