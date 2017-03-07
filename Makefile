install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/moh.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-moh
	rm /etc/wazo-admin-ui/conf.d/moh.yml
	systemctl restart wazo-admin-ui
