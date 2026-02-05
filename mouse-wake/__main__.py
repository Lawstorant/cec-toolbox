#! /usr/bin/env python3

import subprocess
import time
from selectors import DefaultSelector, EVENT_READ
from evdev import InputDevice, ecodes as e, list_devices

IDLE_THRESHOLD = 10
COOLDOWN = 30

print("starting cec-toolbox mouse wake daemon\n")


def find_mice():
    mice = []
    for path in list_devices():
        try:
            dev = InputDevice(path)
            caps = dev.capabilities()
            if e.EV_REL in caps:
                rel_caps = caps[e.EV_REL]
                if e.REL_X in rel_caps or e.REL_Y in rel_caps:
                    mice.append(dev)
        except Exception:
            continue
    return mice


def tv_is_off():
    try:
        result = subprocess.run(
            ["/usr/bin/cec-toolbox", "state"],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip() == "0"
    except Exception:
        return False


def main_loop():
    last_mouse_event = time.time()
    last_cec_check = 0

    mice = find_mice()
    if not mice:
        print("No mouse devices found!")
        return

    print(f"Monitoring {len(mice)} mouse device(s): {', '.join(m.name for m in mice)}")

    selector = DefaultSelector()
    for mouse in mice:
        selector.register(mouse, EVENT_READ)

    try:
        while True:
            for key, _ in selector.select():
                device = key.fileobj
                for event in device.read():
                    if event.type != e.EV_REL:
                        continue

                    now = time.time()
                    idle_duration = now - last_mouse_event
                    last_mouse_event = now

                    if idle_duration > IDLE_THRESHOLD and (now - last_cec_check) > COOLDOWN:
                        last_cec_check = now
                        if tv_is_off():
                            print("Mouse movement after idle, turning TV on")
                            subprocess.run(
                                ["/usr/bin/cec-toolbox", "on"],
                                timeout=10
                            )
    finally:
        selector.close()


while True:
    main_loop()
    time.sleep(2)
