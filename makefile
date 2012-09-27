install: unity-lens-osm
	mkdir  /opt/extras.ubuntu.com/
	mkdir  /opt/extras.ubuntu.com/unity-lens-osm/
	cp unity-lens-osm /opt/extras.ubuntu.com/unity-lens-osm/unity-lens-osm
	mkdir /opt/extras.ubuntu.com/unity-lens-osm/
	mkdir /opt/extras.ubuntu.com/unity-lens-osm/media/
	cp lens-nav-osm.svg /opt/extras.ubuntu.com/unity-lens-osm/media/lens-nav-osm.svg
	mkdir /usr/share/unity/lenses/
	mkdir /usr/share/unity/lenses/extras-unity-lens-osm/
	cp extras-unity-lens-osm.lens /usr/share/unity/lenses/extras-unity-lens-osm/extras-unity-lens-osm.lens
	cp extras-unity-lens-osm.service /usr/share/dbus-1/services/extras-unity-lens-osm.service
