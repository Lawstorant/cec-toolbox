enable-services:
	systemctl daemon-reload
	systemctl enable cec-toolbox-wakeup
	systemctl enable cec-toolbox-suspend

disable-services:
	systemctl disable cec-toolbox-wakeup
	systemctl disable cec-toolbox-suspend

install:
	install -Dm755 cec-toolbox /usr/bin/cec-toolbox
	install -Dm644 cec-toolbox-suspend.service /usr/lib/systemd/system/cec-toolbox-suspend.service
	install -Dm644 cec-toolbox-wakeup.service /usr/lib/systemd/system/cec-toolbox-wakeup.service

remove: disable-services
	rm /usr/bin/cec-toolbox || true
	rm /usr/lib/systemd/system/cec-toolbox-* || true

install-and-enable: install
	make enable-services
