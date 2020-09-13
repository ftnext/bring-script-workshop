# See `diff -y first_step_script/shrink_image.py outcomes/cli/shrink_image.py`

"""Shrink images in `../target_images/memories`
- Images with a width or height greater than 300px are to be resized
- Shrinked images are placed in directory `images/memories`
"""

from argparse import ArgumentParser  # Added
from pathlib import Path

from PIL import Image


SHRINK_TARGET_EXTENSION = (".jpg", ".jpeg", ".png")


def calculate_shrinked_size(width, height, max_length):
    """Calculate shrinked size in proportion
    The larger of width and height should be equal to max_length.
    For exanple, width=500px, height=400px
    width : height = max_length : new_height
    i.e. new_height = max_length * height / width
    if you swap the width and the height:
    width : height = new_width : max_length
    """
    if width > height:
        new_width = max_length
        new_height = int(max_length * height / width)
    else:
        new_width = int(max_length * width / height)
        new_height = max_length
    return (new_width, new_height)


def resize_image(image_path, save_path, max_length):
    """Resize a given image so that the width and the height
    is equal or less than max_length
    Return a result as bool:
    - When the image need to resize and succeed, return True
    - When the image does not need to resize, return False
    """
    image = Image.open(image_path)
    width, height = image.size
    if width > max_length or height > max_length:
        shrinked_size = calculate_shrinked_size(width, height, max_length)
        resized_image = image.resize(shrinked_size, Image.BICUBIC)
        resized_image.save(save_path)
        return True
    return False


if __name__ == "__main__":
    parser = ArgumentParser()  # Added
    parser.add_argument("target_image_path")  # Added
    args = parser.parse_args()  # Added

    image_dir_path = Path(args.target_image_path)  # Changed
    shrinked_dir_path = Path("images") / image_dir_path.name
    shrinked_dir_path.mkdir(exist_ok=True, parents=True)
    for image_path in image_dir_path.iterdir():
        if image_path.suffix not in SHRINK_TARGET_EXTENSION:
            continue
        save_path = shrinked_dir_path / image_path.name
        resize_image(image_path, save_path, 300)
        print(f"{image_path} is shrinked: {save_path}")
