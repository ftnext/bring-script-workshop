# bring-script-workshop
Workshop at PyCon APAC 2020

- Slide: https://bit.ly/bring-script-pyconapac
- Repostiory: https://github.com/ftnext/bring-script-workshop

## Prerequisite

- Python 3.7
- Google Chrome (Use at the GUI part)

## Preparation

### 1. Clone this repository

```
git clone https://github.com/ftnext/bring-script-workshop.git
```

### 2. Install dependencies

Use what you've always done when setting up your environment.  
I usually use `venv` module.

```
cd bring-script-workshop
python3 -m venv venv
source venv/bin/activate  # macOS / Linux
pip install -r requirements.txt
```

It will take some time...  
I will introduce myself and this workshop using the [slide](https://docs.google.com/presentation/d/1N5kNws1d1c3S00hBQjb9sPETovACgm0yRIzNPMR2Nmk/edit?usp=sharing).

### 3. Execute the image size redction script

Get some images. (Use your favorite images)  
e.g.) https://www.flickr.com/photos/pyconjp/48743997848/in/album-72157710870622516/  
License of the above image is CC-BY. ref: https://www.pycon.jp/committee/license.html (Japanese)

Put your images in the `target_images/memories` directory.  
For example,

```
.
├── README.md  # this file
└── target_images
    └── memories
        ├── pyconjp1.jpg
        └── pyconjp2.jpg
```

Execute the script.

```
cd first_step_script
python shrink_image.py
```

Check the `images/memories` directory (newly created).

## Main contents

This is a Quick tour from CLI through GUI to Web app.  
Please see the `cut_in_chase` directory.

The `outcomes` directory holds completed codes in this workshop.

If you have any troubles or questions about this repository, feel free to contact to me(nikkie)

- PyCon APAC Notice Board
- Creating issue in this repository
- Twitter [@ftnext](https://twitter.com/ftnext).
