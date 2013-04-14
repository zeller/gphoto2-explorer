import optparse
import pyexiv2
import os
import sqlite3
import subprocess

photos_datetime_map = {}

def process(files, out):
    # Read datetime objects into map for each photo
    for photo_filename in files:
        meta = pyexiv2.metadata.ImageMetadata(photo_filename)
        meta.read()
        datetime_key = 'Exif.Photo.DateTimeOriginal'
        if datetime_key in meta.exif_keys:
            photos_datetime_map[photo_filename] = meta[datetime_key].value
    
    print repr(photos_datetime_map)

    # sort the images on timestamp and calculate seconds delay between photos
    progression = sorted(photos_datetime_map.iteritems(), key=lambda x: x[1], reverse=False)
    progression_files = [progression[i][0] for i in range(len(progression))]
    progression_delay = [(progression[i+1][1]-progression[i][1]).seconds for i in range(len(progression)-1)] + [10]

    print repr(progression_files)
    print repr(progression_delay)

    def get_thumbfile(filename):
        dirname = os.path.dirname(filename)
        basepath, extension = os.path.splitext(filename)
        basename = os.path.basename(basepath)
        thumbname = basename + '.thumb' + extension
        dirname = os.path.join(dirname, "thumbs")
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        thumbfile = os.path.join(dirname, thumbname)
        return thumbfile

    for filename in progression_files:
        sp = subprocess.Popen("convert -resize 200x " + filename + " " + get_thumbfile(filename), shell=True)
        sp.wait()

    file_arguments = ' '.join(["-delay %s %s" % (min(delay*10, 100), get_thumbfile(filename)) for delay, filename in zip(progression_delay, progression_files)])

    sp = subprocess.Popen("convert " + file_arguments + " -loop 0 " + out, shell=True)
    sp.wait()

def main():
    usage="python %prog [options] files"
    parser = optparse.OptionParser(usage)
    parser.add_option("-o", "--out",
                      action="store",
                      dest="out",
                      help="File to write GIF results to")

    (opts, args) = parser.parse_args()

    if not (opts.out and len(args) > 0):
        parser.print_help()
        exit()

    process(args, opts.out)

if __name__ == "__main__":
    cn = main()
