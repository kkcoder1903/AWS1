#!/bin/bash

# Set the log file path
LOG_FILE="/var/log/webserver.log"

# Create a backup directory if it does not exist
BACKUP_DIR="/var/backups/webserver"

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir "$BACKUP_DIR"
fi

# Rotate the log file
mv "$LOG_FILE" "$LOG_FILE.1"
touch "$LOG_FILE"

# Backup the log file
cp "$LOG_FILE.1" "$BACKUP_DIR/webserver-$(date +%Y-%m-%d).log"

# Remove old log files
find "$BACKUP_DIR" -type f -name "webserver-*.log" -mtime +7 -delete
