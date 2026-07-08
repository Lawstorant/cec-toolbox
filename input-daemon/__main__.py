#! /usr/bin/env python3

from evdev import InputDevice, ecodes as e, list_devices
from evdev import UInput, InputEvent, KeyEvent

from re import search
from time import sleep

from mapping import cec_mapping

print("starting cec-toolbox input daemon\n")

def main_loop() -> None:
    devices = [InputDevice(path) for path in list_devices()]
    cec = None

    for device in devices:
        if search("DP-[0-9]", device.name):
            cec = device

    if not cec:
        print("No CEC input devices found!")
        return

    cec.grab()
    cap = cec.capabilities(verbose=False)
    for code in sum(cec_mapping.values(), []):
        if code not in cap[e.EV_KEY]:
            cap[e.EV_KEY].append(code)

    if e.EV_SYN in cap:
        cap.pop(e.EV_SYN)

    virt = UInput(events=cap, name='CEC-toolbox Virtual Input')

    event: InputEvent
    for event in cec.read_loop():
        if event.type != e.EV_KEY:
            continue

        key = KeyEvent(event)
        new_keys: list[int] = []

        if key.scancode not in cec_mapping:
            continue

        if key.keystate == 1:
            print(f"Detected supported key: {key.keycode}")

        for code in cec_mapping[key.scancode]:
            virt.write(e.EV_KEY, code, key.keystate)
            virt.syn()
            sleep(0.1)

    cec.ungrab()


while True:
    main_loop()
    sleep(2)
