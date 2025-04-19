from PIL import Image, ImageDraw, ImageFont
import os

# Create a 32x32 image with a dark background
img = Image.new('RGBA', (32, 32), color=(40, 40, 40, 255))
draw = ImageDraw.Draw(img)

# Try to use a system font, fallback to default if not found
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
except:
    font = ImageFont.load_default()

# Draw the initials
draw.text((6, 4), "PG", font=font, fill=(255, 255, 255, 255))

# Ensure the images directory exists
os.makedirs('content/images', exist_ok=True)

# Save as favicon.ico
img.save('content/images/favicon.ico', format='ICO') 