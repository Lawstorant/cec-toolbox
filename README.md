# cec-toolbox

### Dependencies:
- cec-ctl
- python3
- python-evdev

### Installation
```shell
sudo make install
sudo make enable-services
# or
sudo make install-and-enable
```

### Removal
```shell
sudo make remove
```

## Usage
```shell
# Turn on the TV and switch to PC
cec-toolbox on

# Turn off the TV
cec-toolbox off

# Get current PC's input
cec-toolbox get-input

# Switch to current input
cec-toolbox notice-me

# Switch to HDMI 3
cec-toolbox input 3

# configure as playback device
# (done automatically for on/off commands)
cec-toolbox configure

# run input daemon manually (systemd service preferred)
cec-toolbox daemon
```

## Config
This script reads `/etc/cec-toolbox.conf`. You can set a custom address or device name there. This is useful if you're
using a CEC adapter on a port, separate from the true input you want to use.

`/etc/cec-toolbox.conf`:
```shell
CUSTOM_ADDRESS=1.2.3.4
DEVICE_NAME="Laptop"
```

`cec-toolbox` can write the config file itself. There are three helper commands:
```shell
# Write custom address to config
sudo cec-toolbox set-custom-address 1.2.3.4

# Write custom device name to config
sudo cec-toolbox set-custom-name Laptop

# Clear config file
sudo cec-toolbox clear-config
```

## Arch Linux
AUR package: [cec-toolbox-git](https://aur.archlinux.org/packages/cec-toolbox-git)

