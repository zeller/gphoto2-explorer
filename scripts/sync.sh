if [ ! -d ../thumbs ]; then
    mkdir ../thumbs
fi

pushd ../thumbs
# Download all thumbnails from the DSLR (fast)
gphoto2 --get-all-thumbnails --new
popd

if [ ! -d ../photos ]; then
    mkdir ../photos
fi

pushd ../photos
# Download all photos from the DSLR (slow)
gphoto2 --get-all-files --new

if [ ! -d ../db ]; then
    mkdir ../db
fi

# Extract EXIF datetime to a database
python utils/extract-EXIF-data.py

# Convert all photos to thumbnails (200 pixels width)
find . -name \*.JPG | xargs -I % convert -resize 200x "%" "../thumbs/%"
popd
