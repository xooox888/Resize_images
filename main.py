import os
from PIL import Image

# Function to resize images
def resize_images(size=(1000, 1000)):
    input_directory = os.getcwd()  # Current directory
    output_directory = os.path.join(input_directory, 'resized_images')

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            img_path = os.path.join(input_directory, filename)
            img = Image.open(img_path)
            img_resized = img.resize(size)
            img_resized.save(os.path.join(output_directory, filename))
            print(f"Resized and saved {filename} to {output_directory}")

# Call the function
resize_images()
