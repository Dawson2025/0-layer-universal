#!/bin/bash
# resource_id: "0657e8cb-1f4e-4ef9-904d-c64439109296"
# resource_type: "script"
# resource_name: "add_vps_key_to_linux"
# Run this on Linux to allow passwordless SSH from VPS

VPS_KEY="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w root@ubuntu-4gb-nbg1-1"

mkdir -p ~/.ssh
chmod 700 ~/.ssh

if grep -q "ubuntu-4gb-nbg1-1" ~/.ssh/authorized_keys 2>/dev/null; then
    echo "VPS key already added"
else
    echo "$VPS_KEY" >> ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys
    echo "VPS key added! You can now SSH from VPS without password."
fi
