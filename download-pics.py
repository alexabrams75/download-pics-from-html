from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve
import os
import sys

# Script to parse HTML files and find all linked images, and download them 

# Folder where all the HTML files are located
folder = "T:\\Web Team\\P6 Employee Files\\Mr. Abrams\\Info pages review - new website\\html"

# for each file in the folder
for file in os.listdir(folder):

	# joins folder + file name to look for correct file
    fileLoc = os.path.join(folder, file)

    with open(fileLoc, "r", encoding="utf-8") as f:
        print("Current file: %s" % file)
        contents = f.read()
        soup = bs(contents, "lxml")

        # For each img tag, find the src link and download the content at the link
        for image in soup.findAll("img"):
            print("Image: %(src)s" % image)
            filename = image["src"].split("/")[-1]
            if (not "JPG" in filename.upper() and not "PNG" in filename.upper()):
                filename = filename + ".jpg"
            urlretrieve(image["src"], filename)

