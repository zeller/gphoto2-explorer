pushd ../thumbs
# Download all thumbnails from the DSLR (fast)
gphoto2 --get-all-thumbnails --new
popd

pushd ../photos
# Download all photos from the DSLR (slow)
gphoto2 --get-all-files --new

# Extract EXIF datetime to a database
python utils/extract-EXIF-data.py

# Convert all photos to thumbnails (200 pixels width)
find . -name \*.JPG | xargs -I % convert -resize 200x "%" "../thumbs/%"
popd
