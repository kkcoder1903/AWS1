# Simple Monitoring Script

This simple monitoring script is a bash script that collects various system metrics, such as CPU usage, memory usage, disk usage, I/O usage, and network information, and stores them in a log file for monitoring and analysis. You can run this script periodically using cron or any other scheduling tool to keep track of your system's performance over time.

## Usage

1. **Prerequisites**: Ensure that you have the necessary permissions to run the script and access the required commands (e.g., `top`, `free`, `df`, `iostat`, and `ip`).

2. **Customize Thresholds**: You can customize the threshold values for different metrics by editing the following variables at the bottom of the script:

   - `CPU_THRESHOLD`: Set the CPU usage threshold (percentage).
   - `MEMORY_THRESHOLD`: Set the memory usage threshold (percentage).
   - `DISK_THRESHOLD`: Set the disk usage threshold (percentage).
   - `IO_THRESHOLD`: Set the I/O usage threshold (percentage).
   - `NETWORK_THRESHOLD`: Set the network usage threshold (percentage).

3. **Redirect Output**: The script will create or update a log file at `/var/log/metrics.txt` to store the collected metrics. Make sure you have write permissions to this directory. You can change the log file location if needed.

4. **Schedule the Script**: You can schedule this script to run at regular intervals, e.g., using cron jobs. For example, to run it every 5 minutes, add the following line to your crontab:

   ```bash
   */5 * * * * /path/to/monitoring_script.sh
   ```

5. **Run the Script Manually**: You can also run the script manually by executing it with bash:

   ```bash
   bash monitoring_script.sh
   ```

## Metrics Collected

The script collects the following system metrics:

- **Current Time**: The timestamp when the metrics are collected.

- **CPU Usage**: The CPU usage as a percentage. It uses the `top` command to retrieve this information.

- **Memory Usage**: The memory usage as reported by the `free` command.

- **Disk Usage**: The usage of the root file system as reported by the `df` command.

- **I/O Usage**: The I/O usage, specifically the second column (tps), as reported by the `iostat` command.

- **Network Usage**: The IP address of the `eth0` interface. You can modify the interface name if needed.

## Monitoring Thresholds

The script allows you to set monitoring thresholds for different metrics. If any of these thresholds are exceeded, it may indicate potential issues with system performance.

## Log File

The script appends the collected metrics to the log file, creating a CSV-style log that can be easily analyzed. You can use this log to track the performance of your system.
