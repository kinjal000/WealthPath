#!/bin/bash
# ====================================================================
# AWS Infrastructure Heartbeat Verification & Runtime Monitoring Engine
# Objective: Transparent system runtime parsing diagnostics metrics
# ====================================================================

echo "=== AWS EC2 CLOUD PLATFORM DIAGNOSTIC SNAPSHOT ==="
echo "Timestamp Clock: $(date)"
echo "Host Resource Check: $(uptime)"
echo "--------------------------------------------------"

# 1. Inspect Port 5000 Flask Application Thread Binding Status
echo -n "Application Daemon Port Status Validation (5000): "
if ss -tuln | grep -q ':5000'; then
    echo "[ONLINE / OPERATIONAL]"
else
    echo "[CRITICAL DOWNALERT - SERVICE FLASK DISCONNECTED]"
fi

# 2. Inspect MySQL Engine State
echo -n "Database Core Framework Daemon Engine State: "
if systemctl is-active --quiet mysql; then
    echo "[RUNNING / ACTIVE]"
else
    echo "[CRITICAL DOWNALERT - MYSQL ENGINE UNREACHABLE]"
fi

# 3. Assess Computing Load Telemetry Vectors
echo "--------------------------------------------------"
echo "EC2 Local EBS Resource Allocation metrics:"
df -h | grep '^/dev/' || true
echo "=================================================="