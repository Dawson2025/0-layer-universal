---
resource_id: "039efae9-9119-4875-9435-6b397e3a1c87"
resource_type: "output"
resource_name: "REQ_002_yoga_speaker_implementation"
---
# Implementation: Yoga Pro 9 Speaker I2C Configuration

<!-- section_id: "cb271d3a-59c2-4ac7-b7c5-33f3a3607792" -->
## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

<!-- section_id: "bb97a488-b90d-436a-9f3f-68ba39552f65" -->
## Date
2026-01-26

<!-- section_id: "400aca32-598e-4790-8736-1fb2a6563cbe" -->
## Files Created

<!-- section_id: "ee0873e0-f6a4-426b-b3b7-3f57a946c9c1" -->
### 1. I2C Bypass Script

**Location**: `/usr/local/bin/2pa-byps.sh`

**Purpose**: Enables the subwoofer by sending I2C commands to TAS2781 amplifier

**Key Operations**:
```bash
# Detects laptop model from DMI
laptop_model=$(</sys/class/dmi/id/product_name)

# Finds correct I2C bus (Synopsys DesignWare adapter)
i2c_bus=$(find_i2c_bus)

# Sends configuration to amplifier addresses
# For model 83DN: addresses 0x3f and 0x38
i2cset -f -y "$i2c_bus" "$value" 0x00 0x00
# ... (multiple register configurations)
```

**Source**: Adapted from [maximmaxim345/yoga_pro_9i_gen9_linux](https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux)

---

<!-- section_id: "bf77106e-9408-4aff-953c-3246616c5bc0" -->
### 2. Systemd Service

**Location**: `/etc/systemd/system/yoga-16imh9-speakers.service`

**Content**:
```ini
[Unit]
Description=Turn on speakers using i2c configuration
After=suspend.target hibernate.target hybrid-sleep.target suspend-then-hibernate.target

[Service]
User=root
Type=oneshot
ExecStart=/bin/sh -c "/usr/local/bin/2pa-byps.sh | logger"

[Install]
WantedBy=multi-user.target sleep.target
Also=suspend.target hibernate.target hybrid-sleep.target suspend-then-hibernate.target
```

**Purpose**: Runs bypass script at boot and after sleep/hibernate

---

<!-- section_id: "08df8f0a-24ce-4dca-8624-ad0ae0008bc1" -->
### 3. Driver Blacklist

**Location**: `/etc/modprobe.d/disable-tas2781-driver.conf`

**Content**:
```
blacklist snd_hda_scodec_tas2781_i2c
```

**Purpose**: Prevents kernel driver from resetting I2C configuration

---

<!-- section_id: "7d1bf77d-d420-4609-a3cc-23090433ec50" -->
### 4. EasyEffects Preset

**Location**: `~/.config/easyeffects/output/Yoga Pro 9i Official.json`

**Source**: Downloaded from GitHub repo

**Purpose**: Audio enhancement preset tuned specifically for Yoga Pro 9 speakers

---

<!-- section_id: "1cd03e3c-33a8-4cf9-93cf-8688109ad1ed" -->
## Commands Executed

<!-- section_id: "0c2fa61b-2e70-4528-aa1c-48fbaabf6725" -->
### Install Dependencies
```bash
sudo apt-get install -y i2c-tools
```

<!-- section_id: "79b88a4a-875f-4e56-af1c-78be6425f8aa" -->
### Create and Enable Service
```bash
sudo chmod +x /usr/local/bin/2pa-byps.sh
sudo systemctl daemon-reload
sudo systemctl enable yoga-16imh9-speakers.service
```

<!-- section_id: "11c62970-4777-446b-8146-c7fdf2a70198" -->
### Run Immediately (Without Reboot)
```bash
sudo /usr/local/bin/2pa-byps.sh
sudo rmmod snd_hda_scodec_tas2781_i2c
```

<!-- section_id: "ce9f8be1-9f7f-4335-9247-5de684211b80" -->
### Load EasyEffects Preset
```bash
easyeffects --load-preset "Yoga Pro 9i Official"
```

<!-- section_id: "27712a31-7b09-4876-98e3-3284cc76eb9d" -->
## Implementation Notes

- Laptop model detected as **83DN** (Yoga Pro 9 16IMH9)
- I2C bus **2** used for communication
- Driver successfully unloaded without reboot
- EasyEffects preset loaded and active
