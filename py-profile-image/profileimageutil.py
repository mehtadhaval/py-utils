import random
import tempfile

from PIL import Image, ImageDraw, ImageFont


def get_random_background_color():
    """
    Generates random color from a set of pre-defined base colors
    :return:
    """
    colors = (
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255)
    )
    base_color = random.choice(colors)
    color = []
    for base_color_component in base_color:
        variation = round(random.random()*30)
        color_component = base_color_component + variation if base_color_component < 127 else \
            base_color_component - variation
        lo, hi = 0, 255
        color_component = lo if color_component <= lo else hi if color_component >= hi else color_component
        color.append(color_component)
    return color


def generate_image(text, out_file, height=100, width=100):
    height = height
    width = width
    image = Image.new('RGBA', (width, height))
    font = ImageFont.truetype("OpenSans-Semibold.ttf", int(min(height, width)*0.8))
    d = ImageDraw.Draw(image)
    text = text[:1]
    text_size = font.getsize(text)
    d.ellipse((0, 0, width, height), fill=tuple(get_random_background_color() + [255]))
    x, y = ((width-text_size[0])/2), ((text_size[1]-height)/2)
    d.text((x, y), text, font=font, fill=(255, 255, 0, 255))
    image.save(out_file, "PNG")
