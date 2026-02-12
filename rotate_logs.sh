#!/bin/bash

LOG_DIR="/home/user/project"
LOG_FILE="$LOG_DIR/access.log"
ARCHIVE_NAME="access_$(date +%F_%H-%M).log.gz"

if [ -f "$LOG_FILE" ]; then
    if [ -f "$LOG_FILE" ]; then
    echo "Rotation log: $ARCHIVE_NAME"
    
    
    cp "$LOG_FILE" "$LOG_DIR/temp_log"
    gzip -c "$LOG_DIR/temp_log" > "$LOG_DIR/$ARCHIVE_NAME"
    rm "$LOG_DIR/temp_log"

    
    > "$LOG_FILE"
    
    
    find "$LOG_DIR" -name "access_*.gz" -mtime +7 -delete
else
    echo "File $LOG_FILE not found!"
fi