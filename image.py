def coordinate(degrees, minutes, seconds):
   return degrees + minutes/60 + seconds/3600

# convert your image to jpg first

from exif import Image
img_path = "/Users/ananyaohrie/Downloads/bk.jpg"

with open(img_path, 'rb') as src:
    img = Image(src)
    print (src.name, img)

if img.has_exif:
 info = "EXIF information is available."
else:
 info = "No EXIF information available."
print(f"Image {src.name}: {info}")

with open(img_path, 'rb') as src:
 img = Image(src)
# print(img.list_all())

if 'datetime' in img.list_all():
  print(img.datetime)
else:
  print("No datetime information available.")

if 'make' in img.list_all():
    print(img.make)
else:
  print("No camera make information available.")
  
if 'model' in img.list_all():
    print(img.model)
else:
    print("No camera model information available.")

if 'gps_latitude' in img.list_all():
    latitude = img.gps_latitude
    print(coordinate(latitude[0], latitude[1], latitude[2]))
else:
    print("No gps latitude information available.")

if 'gps_longitude' in img.list_all():
    longitude = img.gps_longitude
    print(coordinate(longitude[0], longitude[1], longitude[2]))
else:
    print("No gps longitude information available.")

