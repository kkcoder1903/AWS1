#!/bin/bash

# Get the current time
CURRENT_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# Get the CPU usage
CPU_USAGE=$(top -b -n 1 | grep -E "^%Cpu" | awk '{print $2}')

# Get the memory usage
MEMORY_USAGE=$(free -h | grep Mem: | awk '{print $3}')

# Get the disk usage
DISK_USAGE=$(df -h | grep / | awk '{print $5}')

# Get the I/O usage
IO_USAGE=$(iostat -x 1 | tail -1 | awk '{print $2}')

# Get the network usage
NETWORK_USAGE=$(ip addr show eth0 | grep "inet " | awk '{print $2}')

# Set the thresholds
CPU_THRESHOLD=80
MEMORY_THRESHOLD=90
DISK_THRESHOLD=90
IO_THRESHOLD=80
NETWORK_THRESHOLD=100

# Redirect the output into a file
echo "Time,CPU Usage,Memory Usage,Disk Usage,I/O Usage,Network Usage" > /var/log/metrics.txt

# Append the current metrics to the file
echo "$CURRENT_TIME,$CPU_USAGE,$MEMORY_USAGE,$DISK_USAGE,$IO_USAGE,$NETWORK_USAGE" >> /var/log/metrics.txt 
