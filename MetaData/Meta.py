"""

Script to give us the meta-data of a picture.

"""

from PIL import Image
from PIL.ExifTags import TAGS
#video-path
img = input("What file do you want to analyze?\n(Remember that u can only analyze images!\n>>> ").replace("'","").replace(" ","")
image = Image.open(img)
all_data = image.getexif()


# getting all the data from the image

for tag_id in all_data:
    # translating all the metadata.
    tag = TAGS.get(tag_id, tag_id)
    data = all_data.get(tag_id)
    # decode bytes
    if isinstance(data, bytes):
        data = data.decode(encoding = 'unicode_escape')
    print(f"{tag:25}: {data}")
