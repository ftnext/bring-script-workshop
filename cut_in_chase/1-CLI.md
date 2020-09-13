Notice: Work at the `first_step_script` directory.

## First example of argparse

Create `hello_world.py` as the following:

```python
from argparse import ArgumentParser
# allow to take (required) arguments from the command line
parser = ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()

# name attribute of args stores the (str) value specified in 
print(f"Hello, {args.name}")  # command line
```

Execute the script.

```
# If name is not specified, a help message is displayed
$ python hello_world.py
usage: hello_world.py [-h] name
hello_world.py: error: the following arguments are required: name

# Call example
$ python hello_world.py PyConAPAC
Hello, PyConAPAC
```

## Change shrink_image.py into CLI app

Before

```python
if __name__ == "__main__":
    image_dir_path = Path("../target_images/memories")
    shrinked_dir_path = Path("images") / image_dir_path.name
    shrinked_dir_path.mkdir(exist_ok=True, parents=True)
    for image_path in image_dir_path.iterdir():
        if image_path.suffix not in SHRINK_TARGET_EXTENSION:
            continue
        save_path = shrinked_dir_path / image_path.name
        resize_image(image_path, save_path, 300)
        print(f"{image_path} is shrinked: {save_path}")
```

After (Add 4 lines and delete 1 line)

```python
from argparse import ArgumentParser  # Added

# :

if __name__ == "__main__":
    parser = ArgumentParser()  # Added
    parser.add_argument("target_image_path")  # Added
    args = parser.parse_args()  # Added

    # image_dir_path = Path("../target_images/memories")  # Deleted
    image_dir_path = Path(args.target_image_path)  # Added
    shrinked_dir_path = Path("images") / image_dir_path.name
    shrinked_dir_path.mkdir(exist_ok=True, parents=True)
    for image_path in image_dir_path.iterdir():
        if image_path.suffix not in SHRINK_TARGET_EXTENSION:
            continue
        save_path = shrinked_dir_path / image_path.name
        resize_image(image_path, save_path, 300)
        print(f"{image_path} is shrinked: {save_path}")
```

## Tips of argparse

I will tell you some tips using the [slide](https://docs.google.com/presentation/d/1N5kNws1d1c3S00hBQjb9sPETovACgm0yRIzNPMR2Nmk/edit?usp=sharing).
