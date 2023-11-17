import os

image_path = r'C:\Users\JR Stalin\Desktop\iris-class\templates\path\to\iris_image.png'  # Adjust this to the actual path

# Check if the file exists
if os.path.isfile(image_path):
    print(f'The image file "{image_path}" exists.')
else:
    print(f'The image file "{image_path}" does not exist.')
