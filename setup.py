#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

###################### DO NOT TOUCH THIS (HEAD TO THE SECOND PART) ######################

import os
import sys
import stat

try:
    import DistUtilsExtra.auto
    from DistUtilsExtra.command import build_extra
except ImportError:
    print >> sys.stderr, 'To build unity-lens-osm you need https://launchpad.net/python-distutils-extra'
    sys.exit(1)
assert DistUtilsExtra.auto.__version__ >= '2.18', 'needs DistUtilsExtra.auto >= 2.18'

def update_config(values = {}):

    oldvalues = {}
    #try:
        #fin = file('unity_lens_osm/unity_lens_osmconfig.py', 'r')
        #fout = file(fin.name + '.new', 'w')

        #for line in fin:
        #    fields = line.split(' = ') # Separate variable from value
        #    if fields[0] in values:
        #        oldvalues[fields[0]] = fields[1].strip()
        #        line = "%s = %s\n" % (fields[0], values[fields[0]])
        #    fout.write(line)

        #fout.flush()
        #fout.close()
        #fin.close()
        #os.rename(fout.name, fin.name)
    #except (OSError, IOError), e:
    #    print ("ERROR: Can't find unity_lens_osm/unity_lens_osmconfig.py")
    #    sys.exit(1)
    return oldvalues


class InstallAndUpdateDataDirectory(DistUtilsExtra.auto.install_auto):
    def run(self):
        values = {'__unity_lens_osm_data_directory__': "'%s'" % (self.prefix + '/share/unity-lens-osm/'),
                  '__version__': "'%s'" % (self.distribution.get_version())}
        previous_values = update_config(values)
        DistUtilsExtra.auto.install_auto.run(self)
        update_config(previous_values)
        os.chmod("/opt/extras.ubuntu.com/unity-lens-osm/unity-lens-osm",775)

        
##################################################################################
###################### YOU SHOULD MODIFY ONLY WHAT IS BELOW ######################
##################################################################################

DistUtilsExtra.auto.setup(
    name='unity-lens-osm',
    version='0.1',
    #license='GPL-3',
    #author='Your Name',
    #author_email='email@ubuntu.com',
    #description='UI for managing …',
    #long_description='Here a longer description',
    #url='https://launchpad.net/unity-lens-osm',
    data_files=[
        ('/opt/extras.ubuntu.com/unity-lens-osm/', ['unity-lens-osm']),
        ('/opt/extras.ubuntu.com/unity-lens-osm/media/', ['lens-nav-osm.svg']),
        ('/usr/share/unity/lenses/extras-unity-lens-osm/', ['extras-unity-lens-osm.lens']),
        ('/usr/share/dbus-1/services/', ['extras-unity-lens-osm.service']),
    ],
    cmdclass={'install': InstallAndUpdateDataDirectory}
    )

