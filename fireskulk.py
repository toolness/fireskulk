#! /usr/bin/python

import os
import shutil
import plistlib

INFO_PLIST = "%s/Contents/Info.plist"
STRINGS = "%s/Contents/Resources/en.lproj/InfoPlist.strings"
APP_INI = "%s/Contents/MacOS/application.ini"
FIREFOX_ICNS = "%s/Contents/Resources/firefox.icns"

# Hardlink files instead of copying them.
copy = os.link

# Alternatively, comment-out the above line and replace with
# the line below to use file copying instead.
#copy = shutil.copyfile

def makefox(name, rootdir):
    srcdir = "/Applications/Firefox.app"
    appdir = "/Applications/%s.app" % name
    if os.path.exists(appdir) and os.path.isdir(appdir):
        print "Removing %s..." % appdir
        shutil.rmtree(appdir)
    print "Creating new %s..." % appdir
    
    for dirname, dirpaths, filenames in os.walk(srcdir):
        reldirname = os.path.relpath(dirname, srcdir)
        if reldirname == '.':
            destdirname = appdir
        else:
            destdirname = os.path.join(appdir, reldirname)
        os.mkdir(destdirname)
        for filename in filenames:
            abs_src_file = os.path.join(dirname, filename)
            abs_dest_file = os.path.join(destdirname, filename)
            if abs_src_file == INFO_PLIST % srcdir:
                info_plist = plistlib.readPlist(abs_src_file)
                del info_plist['CFBundleDocumentTypes']
                version = info_plist['CFBundleVersion']
                idname = name.replace(' ', '_').lower()
                info_plist['CFBundleIdentifier'] = 'org.mozilla.%s' % idname
                fullname = "%s %s" % (name, version)
                info_plist['CFBundleGetInfoString'] = fullname
                info_plist['CFBundleName'] = name
                plistlib.writePlist(info_plist, abs_dest_file)
            elif abs_src_file == APP_INI % srcdir:
                app_ini = open(abs_src_file, 'r').read()
                f = open(abs_dest_file, 'w')
                f.write(app_ini.replace('Firefox', name))
                f.close()
            elif abs_src_file == STRINGS % srcdir:
                strings = open(abs_src_file, 'r').read()
                strings = strings.decode('utf-16')
                f = open(abs_dest_file, 'w')
                f.write(strings.replace('Firefox', name).encode('utf-16'))
                f.close()
            elif abs_src_file == FIREFOX_ICNS % srcdir:
                os.link("%s/firefox.icns" % rootdir, abs_dest_file)
            else:
                copy(abs_src_file, abs_dest_file)

if __name__ == '__main__':
    cfgdir = os.path.expanduser('~/.fireskulk')
    for dirname in os.listdir(cfgdir):
        abspath = os.path.join(cfgdir, dirname)
        if os.path.isdir(abspath):
            makefox(dirname, abspath)
