# bring-script-workshop
Workshop at PyCon APAC 2020

## Prerequisite

- Python 3.7
- Google Chrome (Use at the GUI part)

## Preparation

### 1. Clone this repository

```
git clone https://github.com/ftnext/bring-script-workshop.git
```

### 2. Install dependencies

I usually use `venv` module.

```
cd bring-script-workshop
python3 -m venv venv
source venv/bin/activate  # macOS / Linux
pip install -r requirements.txt
```

It will take some time...  
I will introduce myself and this workshop using the Google slide.

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

```

Check the `images/memories` directory (newly created).
