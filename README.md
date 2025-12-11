# cec-toolbox

### Dependencies:
- cec-ctl

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
```

### Arch Linux
AUR package: [cec-toolbox-git](https://aur.archlinux.org/packages/cec-toolbox-git)

