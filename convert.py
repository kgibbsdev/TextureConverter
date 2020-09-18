import pathlib
import os
from PIL import Image  # pip3 install Pillow

working_dir = pathlib.Path().absolute()
texture_source_directory = "TIF Files"
converted_directory = "Converted Textures"
converted_directory_exists = os.path.isdir(converted_directory)

images = []

if converted_directory_exists == False:
    os.mkdir(converted_directory)
    print("Created directory to store converted files.")

for filepath in os.listdir(working_dir):  # filepath = name of file
    extension_removed = os.path.splitext(filepath)[0]
    full_path = os.path.join(working_dir, filepath)
    file_is_converted = os.path.isfile(str(working_dir) + '/' +
                                       converted_directory + '/' + extension_removed + '.png')
    # For any file that has the extension ".tif"
    if filepath.lower().endswith('.tif') and file_is_converted == False:
        converted_image = Image.open(full_path)
        converted_image.save(str(working_dir) + '/' +
                             converted_directory + '/' + extension_removed + '.png', "PNG")
    else:
        print("Converting skipped for " + filepath)
