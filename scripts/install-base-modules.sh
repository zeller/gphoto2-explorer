if [ $(id -u) -ne 0 ]; then
  printf "Script must be run as root.\n"
  exit 1
fi

apt-get update

# Camera utilities
apt-get install gphoto2
apt-get install python
apt-get install python-pyexiv2

# Image processing
apt-get install imagemagick

# Web server
apt-get install apache2
apt-get install libapache2-mod-php5
apt-get install sqlite
apt-get install php5-sqlite

# @optional:
# apt-get install emacs
# apt-get install php-elisp
