# Log Rotation and Backup Bash Script

This bash script is designed to perform log rotation and backup for a specific log file on a hypothetical web server. Log rotation is a common practice to manage log files and prevent them from growing indefinitely. This script allows you to rotate and archive log files to save disk space while preserving historical data.

## Usage

Follow these steps to create and use the log rotation and backup script:

1. **Create a Script File**:

   Create a new file with a `.sh` extension (e.g., `rotate_and_backup.sh`).

2. **Add Script Content**:

   Copy and paste the following script content into the file:

   ```bash
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
   ```

   This script rotates the log file, backs up the rotated log file, and deletes old backup files that are older than 7 days.

3. **Save and Exit**:

   Save the file and exit your text editor.

4. **Make the Script Executable**:

   Make the script executable by running the following command:

   ```bash
   chmod +x rotate_and_backup.sh
   ```

5. **Run the Script**:

   To run the script, use the following command:

   ```bash
   ./rotate_and_backup.sh
   ```

   This will execute the log rotation and backup process.

6. **Schedule with Cron (Optional)**:

   To automate log rotation and backup, you can schedule the script to run periodically using a cron job. For example, to run the script every day at midnight, add the following line to your crontab file:

   ```
   0 0 * * * /path/to/rotate_and_backup.sh
   ```

   This schedule will ensure that your log files are rotated and backed up daily.

## Notes

- Replace `/var/log/webserver.log` and `/var/backups/webserver` with the actual paths and filenames as needed for your web server logs.

- The script rotates the log file by renaming it to `webserver.log.1` and creating a new `webserver.log`.

- It creates daily backups of the rotated log files in the `BACKUP_DIR` with filenames like `webserver-YYYY-MM-DD.log`.

- The script removes log files in the `BACKUP_DIR` that are older than 7 days to manage disk space.

This script helps you maintain log files effectively, ensuring that you have access to historical data while keeping disk space usage under control.
