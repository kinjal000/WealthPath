#!/bin/bash
# ====================================================================
# AWS Ubuntu EC2 Deployment Pipeline Strategy Automation script
# Target OS Execution Base: Ubuntu Server LTS Setup Instance Nodes
# ====================================================================

set -e # Terminate immediately upon script error generation paths

echo "===================================================================="
echo "Initializing System Architecture Setup Process Layer"
echo "===================================================================="

# Step 1: Run Apt Sync Layer Actions
echo "[1/4] Running operational system update vectors..."
sudo apt update -y && sudo apt upgrade -y

# Step 2: Ensure critical execution layer dependencies are available
echo "[2/4] Pulling Linux development components and client runtimes..."
sudo apt install python3-pip python3-dev default-libmysqlclient-dev build-essential -y

# Step 3: Package installations from requirements file context
echo "[3/4] Resolving and installing explicit pip dependencies..."
# Navigating upward dynamically to locate requirement configurations
cd "$(dirname "$0")/.."
pip3 install -r requirements.txt --break-system-packages

# Step 4: Provision Flask runtime execution configuration loops safely
echo "[4/4] Resolving active background instances..."
# Safely clear running instance loops on Port 5000 to eliminate binding lockouts
PID_LOCK=$(lsof -t -i:5000 || true)
if [ -not -z "$PID_LOCK" ]; then
    echo "Stale application instance identified ($PID_LOCK). Purging process context..."
    kill -9 "$PID_LOCK"
fi

echo "Spinning production environment worker thread channels..."
nohup python3 app.py > app.log 2>&1 &

echo "===================================================================="
echo "DEPLOYMENT RUNTIME EXECUTED: App available at http://<EC2-PUBLIC-IP>:5000"
echo "===================================================================="