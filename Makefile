
VERSION=0.3
ARCH=noarch
PACKAGE=amahi-transmission

rpm: update-header dist
	(cd release && rpmbuild -ta $(PACKAGE)-$(VERSION).tar.gz)
	mv ~/rpmbuild/RPMS/$(ARCH)/$(PACKAGE)-$(VERSION)-*.$(ARCH).rpm release/
	mv ~/rpmbuild/SRPMS/$(PACKAGE)-$(VERSION)-*.src.rpm release/
	sha1sum release/$(PACKAGE)-$(VERSION)-*.$(ARCH).rpm

dist:
	(mkdir -p release && cd release && mkdir -p $(PACKAGE)-$(VERSION))
	rsync -a amahi-transmission* $(PACKAGE).spec Makefile release/$(PACKAGE)-$(VERSION)/
	(cd release && tar -czvf $(PACKAGE)-$(VERSION).tar.gz $(PACKAGE)-$(VERSION))
	(cd release && rm -rf $(PACKAGE)-$(VERSION))

update-header:
	sed -i -e 's/^Version:\s*[0-9.]*\s*$$/Version: $(VERSION)/' $(PACKAGE).spec

install: rpm
	(cd release && sudo rpm -Uvh $(PACKAGE)-$(VERSION)-*.$(ARCH).rpm)
