from rembg import remove
from PIL import Image


def remove_background(image_path, output_path):
    processed_image = Image.open(image_path)

    # removing background
    output_image = remove(processed_image)

    # saving image
    output_image.save(output_path)
    print("Image processed successfully")


image_path = f"input.jpg"  # Insert path to where image is saved
output_path = f"output.png"  # Insert name and path to save processed image

remove_background(image_path, output_path)