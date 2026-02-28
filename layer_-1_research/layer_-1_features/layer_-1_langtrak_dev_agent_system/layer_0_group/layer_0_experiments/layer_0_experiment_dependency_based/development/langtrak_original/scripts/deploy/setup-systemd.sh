#!/bin/bash
# Setup SystemD service for Language Tracker
# Requires sudo privileges

set -e

echo "🔧 SystemD Service Setup for Language Tracker"
echo "=============================================="

# Get current directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
USER=$(whoami)
VENV_PATH="$PROJECT_DIR/.venv"

echo "Project directory: $PROJECT_DIR"
echo "User: $USER"
echo "Virtual env: $VENV_PATH"

# Create systemd service file
SERVICE_FILE="/tmp/lang-trak.service"

cat > "$SERVICE_FILE" << EOF
[Unit]
Description=Language Tracker Web Application
After=network.target

[Service]
Type=notify
User=$USER
WorkingDirectory=$PROJECT_DIR
Environment="PATH=$VENV_PATH/bin:/usr/local/bin:/usr/bin:/bin"
Environment="PORT=5000"
ExecStart=$VENV_PATH/bin/gunicorn --config gunicorn.conf.py app:app
ExecReload=/bin/kill -s HUP \$MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

echo ""
echo "📄 Service file created at: $SERVICE_FILE"
echo ""
cat "$SERVICE_FILE"
echo ""
echo "To install and start the service, run these commands:"
echo ""
echo "  sudo cp $SERVICE_FILE /etc/systemd/system/lang-trak.service"
echo "  sudo systemctl daemon-reload"
echo "  sudo systemctl enable lang-trak"
echo "  sudo systemctl start lang-trak"
echo "  sudo systemctl status lang-trak"
echo ""
echo "Service management commands:"
echo "  sudo systemctl status lang-trak    # Check status"
echo "  sudo systemctl restart lang-trak   # Restart"
echo "  sudo systemctl stop lang-trak      # Stop"
echo "  sudo systemctl logs -u lang-trak -f  # View logs"
echo ""

