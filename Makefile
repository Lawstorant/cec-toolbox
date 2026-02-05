enable-services:
	systemctl daemon-reload
	systemctl reenable cec-toolbox-input
	systemctl reenable cec-toolbox-wakeup
	systemctl reenable cec-toolbox-suspend
	systemctl reenable cec-toolbox-poweroff
	systemctl reenable cec-toolbox-mouse-wake

	systemctl start cec-toolbox-input
	systemctl start cec-toolbox-mouse-wake

disable-services:
	systemctl disable cec-toolbox-input || true
	systemctl disable cec-toolbox-wakeup || true
	systemctl disable cec-toolbox-suspend || true
	systemctl disable cec-toolbox-poweroff || true
	systemctl disable cec-toolbox-mouse-wake || true

install:
	mkdir -p $(PREFIX)/usr/bin
	mkdir -p $(PREFIX)/usr/share/cec-toolbox/input-daemon
	mkdir -p $(PREFIX)/usr/share/cec-toolbox/mouse-wake
	mkdir -p $(PREFIX)/usr/lib/systemd/system

	install -Dm755 cec-toolbox $(PREFIX)/usr/bin/cec-toolbox
	install -Dm644 input-daemon/*.py $(PREFIX)/usr/share/cec-toolbox/input-daemon/
	install -Dm644 mouse-wake/*.py $(PREFIX)/usr/share/cec-toolbox/mouse-wake/
	install -Dm644 systemd/*.service $(PREFIX)/usr/lib/systemd/system/

remove: disable-services
	rm $(PREFIX)/usr/bin/cec-toolbox || true
	rm -rf $(PREFIX)/usr/share/cec-toolbox || true
	rm $(PREFIX)/usr/lib/systemd/system/cec-toolbox-* || true

install-and-enable: install
	make enable-services
