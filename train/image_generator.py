from PIL import Image
import os

def genRotatedImages(input_image_path, output_folder):
    # Load the image
    image = Image.open(input_image_path)
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    # Define the target size
    target_size = (224, 224)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Rotate the image from 1 to 360 degrees, resize, and save each rotation
    for degree in range(1, 361):
        rotated_image = flipped_image.rotate(degree)
        resized_image = rotated_image.resize(target_size)
        output_image_path = os.path.join(output_folder, f"rotated_flipped_{degree}.png")
        resized_image.save(output_image_path)

# Usage
input_image_path = 'data/photos/train_resized_marked/Img4.jpeg'  # Change this to the path of your input image
output_folder = 'data/photos/train_gen'  # Change this to your desired output folder

genRotatedImages(input_image_path, output_folder)
