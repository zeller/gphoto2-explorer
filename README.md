# gphoto2 Photo Explorer

This utility will sync with any gphoto2 compatible camera using USB
and create a web interface which categorizes photos into a calendar
based on available EXIF data.

## Installation

```
git clone git://github.com/zeller/gphoto2-explorer.git /var/www/gphoto2-explorer
```

For convience, an installation script is provided for easily
installing required module on Debian based systems.

This system has been tested on both Raspbian and Ubuntu 12.04.

* `scripts/install-base-modules.sh`: Installs the packages needed for
  the DSLR USB interface, post-processing of photos, and the web
  server.

## Using

* `scripts/sync.sh`: Downloads all of the most recently taken photos
  of off the DSLR and into the `photos` directory and `thumbs`
  directory, extracting EXIF data into a sqlite database.

Visit http://localhost/gphoto2-explorer/album/ to view your photos in
calendar format. The number of photos taken on each day will be
displayed as a clickable link with a link to a thumbnail based view of
all photos taken on that day, with originals obtainable by clicking on
any thumbnail.

## Hacking

It may be useful to install the following extra packages if you plan
to work on the codebase.

```
apt-get install emacs
apt-get install php-elisp
```

## Copyright

Copyright © 2012-2013 Michael Zeller and contributors
