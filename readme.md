<h1>How to Use the Random Image Overlay Script</h1>

This document explains how to use a Python script that applies randomly chosen overlay images and text to the images in a specific directory.

<h2>Prerequisites:</h2>

You need Python 3.8 or newer installed on your computer.
<br>
You need the Python Imaging Library (PIL) installed. If you haven't installed it yet, you can do so by running pip install pillow in your command line.
<br>
<br>
<h2>Instructions:</h2>

Set up your directories: The script uses specific directories to find your images, overlays, and fonts. Set up these directories as follows:
<br>
<br>
Create a directory with the images you want to modify. Note down its path.
<br>
Create a directory for your overlay images and text files. Note down its path.
<br>
Create a directory for your font files (with a .ttf extension). Note down its path.
<br>
Create a directory where you want the script to save the modified images. Note down its path.

<h2>Update the script:</h2>
<br>
Open the script in a text editor (such as Notepad or Visual Studio Code). Replace the following placeholders with the paths you noted down in step 1:
<br>
Replace 'IMAGE DIRECTORY PATH' with the path to your images.
<br>
Replace 'OVERLAY DIRECTORY PATH' with the path to your overlay images and texts.
<br>
Replace 'FONT DIRECTORY PATH' with the path to your font files.
<br>
Replace 'OUTPUT DIRECTORY PATH' with the path where you want the modified images to be saved.
  
<h2>Adjust script parameters (optional): If you want, you can adjust these parameters in the script to change how it works:</h2>

font_size adjusts the initial size of the overlay text font.
<br>
min_font_size determines the smallest size that the overlay text font can be.
<br>
max_image_overlays determines the maximum number of overlay images that can be applied to each image.
<br>
max_text_overlays determines the maximum number of overlay texts that can be applied to each image.
  
<h2>Run the script:</h2>
<br>
Open a command line window.
<br>
Navigate to the directory where the script is saved using the cd command. 
<br>
Then, run the script with the python command followed by the script's filename. (For example, if your script is called "random_overlay.py", you would run python random_overlay.py.)
<br>
That's it! The script will now process each image in your images directory, apply random overlays, and save the modified images in your output directory. It will also print the path of each saved image in the command line. Enjoy your newly modified images!
