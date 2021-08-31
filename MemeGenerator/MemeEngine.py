"""MemeEngine for loading image and write message with Pillow."""

import random
import os
from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
  """MemeEngine class."""

  def __init__(self, output_dir: str):
    """Meme Engine constructor.

    param output_dir: image output directory
    """
    if not os.path.isdir(output_dir):
    	os.makedirs(output_dir)
    
    self.output_dir = output_dir

  def make_meme(self, img_path, text, author, width=500) -> str: # generated image path
    """Load image using Pillow library and write the meme's messages and author."""
    try:
      img = Image.open(img_path)
    except:
      raise Exception("not image found")

    ratio = width / img.size[0]
    height = int(ratio * img.size[1])
    img = img.resize((width, height), Image.NEAREST)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=30)
    draw.text((10,30), text, font=font, fill="red")
    draw.text((10,70), author, font=font, fill="green")

    output_path = f"{self.output_dir}/{random.randint(0, 1000000)}.jpg"
    img.save(output_path)
    
    return output_path
