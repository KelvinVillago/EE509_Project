import os
from PIL import Image

def resize_images(input_dir, output_dir, size=(224, 224)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            try:
                with Image.open(input_path) as img:
                    img_resized = img.resize(size, Image.ANTIALIAS)
                    img_resized.save(output_path)
                    print(f"Resized {filename} and saved to {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Define input and output directories
input_directory = "data/photos/train2"
output_directory = "data/photos/train2_resized"

# Call the function to resize images
resize_images(input_directory, output_directory)
