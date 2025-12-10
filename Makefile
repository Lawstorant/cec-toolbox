enable-services:
	systemctl daemon-reload
	systemctl reenable cec-toolbox-wakeup
	systemctl reenable cec-toolbox-suspend
	systemctl reenable cec-toolbox-poweroff

disable-services:
	systemctl disable cec-toolbox-wakeup || true
	systemctl disable cec-toolbox-suspend || true
	systemctl disable cec-toolbox-poweroff || true

install:
	install -Dm755 cec-toolbox /usr/bin/cec-toolbox
	install -Dm644 cec-toolbox-suspend.service /usr/lib/systemd/system/cec-toolbox-suspend.service
	install -Dm644 cec-toolbox-poweroff.service /usr/lib/systemd/system/cec-toolbox-poweroff.service
	install -Dm644 cec-toolbox-wakeup.service /usr/lib/systemd/system/cec-toolbox-wakeup.service

remove: disable-services
	rm /usr/bin/cec-toolbox || true
	rm /usr/lib/systemd/system/cec-toolbox-* || true

install-and-enable: install
	make enable-services
