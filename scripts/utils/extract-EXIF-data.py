import pyexiv2
import os
import sqlite3

photos_dir='../photos'
database_dir='../db'

photos_datetime_map = {}

# Read datetime objects into map for each photo
for photo_filename in os.listdir(photos_dir):
    meta = pyexiv2.metadata.ImageMetadata(os.path.join(photos_dir, photo_filename))
    meta.read()
    datetime_key = 'Exif.Photo.DateTimeOriginal'
    if datetime_key in meta.exif_keys:
        photos_datetime_map[photo_filename] = meta[datetime_key].value
        

# Save the map to a database for easy access
database_filename = os.path.join(database_dir, 'photos_datetime.db')
conn = sqlite3.connect(database_filename)
c = conn.cursor()
c.execute('DROP TABLE photos_datetime')
c.execute('CREATE TABLE photos_datetime (filename text, datetime text)')
for key, value in photos_datetime_map.iteritems():
    c.execute("INSERT INTO photos_datetime VALUES ('%s','%s')" % (key, value))
conn.commit()
conn.close()
