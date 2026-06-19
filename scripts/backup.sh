#!/bin/bash
# ====================================================================
# AWS Cloud EC2 Backup Automation Shell Subsystem
# Architecture Objective: Safe, structured transactional snapshot processing
# ====================================================================

# Set parameters explicitly matching deployment configurations
BACKUP_DIR="/home/ubuntu/backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H%M%S")
DATABASE_TARGET="wealthpath"
MYSQL_USER="wealthuser"
MYSQL_AUTH_PASS="kinjal123"

echo "[$(date)] Instantiating local snapshot routine stack..."

# Ensure file hierarchy presence
mkdir -p "$BACKUP_DIR"
chmod 700 "$BACKUP_DIR"

OUTPUT_FILE="$BACKUP_DIR/${DATABASE_TARGET}_prod_snapshot_${TIMESTAMP}.sql"

# Execute safe pipeline generation dump
mysqldump --host="localhost" \
          --user="$MYSQL_USER" \
          --password="$MYSQL_AUTH_PASS" \
          --no-tablespaces \
          "$DATABASE_TARGET" > "$OUTPUT_FILE"

# Evaluate execution code path output
if [ $? -eq 0 ]; then
    echo "[SUCCESS] Dump snapshot safely generated at: $OUTPUT_FILE"
    # Clean up backups older than 7 days to preserve EC2 EBS storage space
    find "$BACKUP_DIR" -name "*.sql" -mtime +7 -exec rm {} \;
    echo "[INFO] EBS Storage clearing routine executed successfully."
else
    echo "[CRITICAL ERROR] Structural Mysqldump step failed evaluation paths." >&2
    exit 1
fi