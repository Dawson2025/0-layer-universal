# Implementation: Yoga Pro 9 Speaker I2C Configuration

## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

## Date
2026-01-26

## Files Created

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

### 3. Driver Blacklist

**Location**: `/etc/modprobe.d/disable-tas2781-driver.conf`

**Content**:
```
blacklist snd_hda_scodec_tas2781_i2c
```

**Purpose**: Prevents kernel driver from resetting I2C configuration

---

### 4. EasyEffects Preset

**Location**: `~/.config/easyeffects/output/Yoga Pro 9i Official.json`

**Source**: Downloaded from GitHub repo

**Purpose**: Audio enhancement preset tuned specifically for Yoga Pro 9 speakers

---

## Commands Executed

### Install Dependencies
```bash
sudo apt-get install -y i2c-tools
```

### Create and Enable Service
```bash
sudo chmod +x /usr/local/bin/2pa-byps.sh
sudo systemctl daemon-reload
sudo systemctl enable yoga-16imh9-speakers.service
```

### Run Immediately (Without Reboot)
```bash
sudo /usr/local/bin/2pa-byps.sh
sudo rmmod snd_hda_scodec_tas2781_i2c
```

### Load EasyEffects Preset
```bash
easyeffects --load-preset "Yoga Pro 9i Official"
```

## Implementation Notes

- Laptop model detected as **83DN** (Yoga Pro 9 16IMH9)
- I2C bus **2** used for communication
- Driver successfully unloaded without reboot
- EasyEffects preset loaded and active
