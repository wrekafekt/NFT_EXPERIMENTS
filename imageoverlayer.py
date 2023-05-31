import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont

# Define the directory of your images
img_dir = 'C:/Users/allso/OneDrive/Documents/images'
overlay_dir = 'C:/Users/allso/OneDrive/Documents/overlays'  # directory with overlay images and text files
font_dir = 'C:/Users/allso/OneDrive/Documents/fonts'  # directory of your fonts

# Get list of overlay images
overlay_images = [f for f in os.listdir(overlay_dir) if f.endswith(".png") or f.endswith(".jpg")]

# Get list of overlay texts
overlay_texts = [f for f in os.listdir(overlay_dir) if f.endswith(".txt")]

# Get list of fonts
fonts = [f for f in os.listdir(font_dir) if f.endswith(".ttf")]

# Ensure there are fonts in the directory
if not fonts:
    print("No fonts found. Please check your font directory.")
    exit(1)

# Define font size
font_size = 24  # Initialize with your desired value
min_font_size = 10  # Minimum font size for legibility

# Define the maximum number of overlays per image
max_image_overlays = 5  # Adjust to your desired value
max_text_overlays = 12  # Adjust to your desired value

for filename in os.listdir(img_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image file
        with Image.open(os.path.join(img_dir, filename)) as img:
            img = img.convert("RGBA")  # Ensure the original image is in RGBA format for transparency
            width, height = img.size

            # Load a random font
            font_path = random.choice(fonts)
            font = ImageFont.truetype(os.path.join(font_dir, font_path), font_size)

            # Create draw object
            draw = ImageDraw.Draw(img)

            # Add multiple random overlay images
            num_image_overlays = random.randint(1, max_image_overlays)  # Determine the number of overlays for the current image
            for _ in range(num_image_overlays):
                # Randomly select an overlay image
                overlay_img_path = os.path.join(overlay_dir, random.choice(overlay_images))

                # Open the overlay image
                overlay_img = Image.open(overlay_img_path).convert("RGBA")  # Convert image to RGBA

                # Randomly resize overlay image
                max_size = random.randint(50, 200)  # Max size in pixels, adjust to your needs
                overlay_img.thumbnail((max_size, max_size))

                # Randomly position the overlay on the blank image
                position_x = random.randint(0, max(0, width - overlay_img.width))
                position_y = random.randint(0, max(0, height - overlay_img.height))

                # Paste the overlay onto the original image with the overlay's alpha as the mask
                img.paste(overlay_img, (position_x, position_y), mask=overlay_img)

            # Add multiple random overlay texts
            num_text_overlays = random.randint(1, max_text_overlays)
            for _ in range(num_text_overlays):
                # Randomly select an overlay text
                overlay_text_path = os.path.join(overlay_dir, random.choice(overlay_texts))

                # Read the overlay text from the text file
                with open(overlay_text_path, 'r') as f:
                    overlay_text = f.read().strip()

                # Randomly adjust the font size for the overlay text
                overlay_font_size = random.randint(min_font_size, font_size)

                # Load the font with the adjusted size
                overlay_font = ImageFont.truetype(os.path.join(font_dir, font_path), overlay_font_size)

                # Calculate the text size
                text_width, text_height = draw.textsize(overlay_text, font=overlay_font)

                # Reduce font size until text fits within image width
                while text_width > width and overlay_font_size > min_font_size:
                    overlay_font_size -= 1
                    overlay_font = ImageFont.truetype(os.path.join(font_dir, font_path), overlay_font_size)
                    text_width, text_height = draw.textsize(overlay_text, font=overlay_font)

                # If the font size has decreased below the minimum, wrap the text to fit the image
                if font_size < min_font_size:
                    overlay_text = textwrap.fill(overlay_text, width=int(width/font_size))

                # Add the overlay text at a random position
                text_position_x = random.randint(0, max(0, width - text_width))
                text_position_y = random.randint(0, max(0, height - text_height))
                draw.text((text_position_x, text_position_y), overlay_text, font=overlay_font, fill=(0, 0, 0, 255))

            # Save the modified image
            output_dir = 'C:/Users/allso/OneDrive/Documents/output'  # directory to save the modified images
            os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
            output_filename = os.path.splitext(filename)[0] + "_modified.png"  # modify the filename if desired
            output_path = os.path.join(output_dir, output_filename)
            img.save(output_path)

            # Print the path of the saved image
            print("Modified image saved at:", output_path)
