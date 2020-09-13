Notice: Work at the repository **root** directory.

```
pwd
cd ..  # if you are in the first_step_script directory
```

## First example of Eel

### 1. Create boilerplate for Eel app.  

(I created the helper command `bringscript`)

```
# Create hello app's boilerplate codes in the current directory (= repository root)
bringscript gui hello .
```

After: It will create the gui directory.

```
├── first_step_script
├── gui
│   ├── gui.py
│   └── web
│       └── hello.html
└── target_images
```

workaround

```
mkdir -p gui/web
touch gui/gui.py
touch gui/web/hello.html
```

### 2. Change gui.py

Before

```python
@eel.expose()
def spam():
    pass
```

After

```python
from datetime import datetime  # Added

@eel.expose
def hello():
    return f"Hello World at {datetime.now()}"

# if you starts from the empty file.
if __name__ == "__main__":
    eel.init("web")
    eel.start("hello.html", size=(600, 400))
```

### 3. Change HTML in hello.html

Workaround (if you start blank HTML)

```
<!DOCTYPE html>
<html>
  <head>
    <script type="text/javascript" src="/eel.js"></script>
    <script type="text/javascript">

    </script>
  </head>
  <body>

  </body>
</html>
```

Before

```html
  <body>

  </body>
```

After

```html
  <body>
    <button type="button" onclick="greeting()" class="styled">Greet</button>
    <p id="greeting"></p>
  </body>
```

### 4. Change JavaScript Code in hello.html

Before

```html
    <script type="text/javascript">

    </script>
```

After

```html
    <script type="text/javascript">
      function print_greeting(message) {
        let greeting = document.getElementById("greeting");
        greeting.innerHTML = message;
      }
      function greeting() {
        eel.hello()(print_greeting);
      }
    </script>
```

### Execution

```
cd gui
python gui.py 
```

## Convert CLI to GUI

Edit `gui.py` and `web/hello.html`.

### 1. Edit `gui.py`

Copy the `shrink_image.py` code and paste it in `gui.py`.

```python
from pathlib import Path  # Added
import re  # Added

import eel
from PIL import Image  # Added

# :  same as shrink_image.py

def existing_path(path_str):
    path = Path(path_str)
    if not path.exists():
        print(f"{path_str}: No such file or directory")
        return None
    return path


# if __name__ == "__main__":  # deleted
@eel.expose  # Added
def resize(target_image_path_str, max_length):
    target_image_path = existing_path(target_image_path_str)
    if not target_image_path:
        return None

    if target_image_path.is_file():
        target_paths = [target_image_path]
        # web directory == localhost:8000/
        shrinked_dir_path = Path("web/images")
    else:
        target_paths = target_image_path.iterdir()
        shrinked_dir_path = Path("web/images") / target_image_path.name
    shrinked_dir_path.mkdir(exist_ok=True, parents=True)

    save_paths = []
    for image_path in target_paths:
        if image_path.suffix not in SHRINK_TARGET_EXTENSION:
            continue
        save_path = shrinked_dir_path / image_path.name
        has_resized = resize_image(image_path, save_path, max_length)
        print(f"{image_path} is shrinked: {save_path}")
        save_paths.append(re.sub(r"^web/", "", str(save_path)))
    return save_paths
```

### 2. Edit `web/hello.html`

After: HTML

```HTML
  <body>
    <div>
      <label for="image-path-input">Specify image file or directory path to be resized:</label>
      <input id="image-path-input" placeholder="Type image path here" value="/Users/" size="60">
    </div>
    <div>
      <label for="max-length-input">Specify max length:</label>
      <input id="max-length-input" value="300">
    </div>
    <button type="button" onclick="resize()">Resize</button>
    <div id="resized-image">---</div>
  </body>
```

After: JavaScript

```HTML
    <script type="text/javascript">
      function listUpImages(imagePaths) {
        var imageHtml = `<p>No specified file or directory</p>`;
        if (imagePaths) {
          imageTags = imagePaths.map(path => `<img src=${path}>`);
          imageHtml = imageTags.join('');
        }
        let imageDiv = document.getElementById("resized-image");
        imageDiv.innerHTML = imageHtml;
      }

      function resize() {
        let targetImagePath = document.getElementById("image-path-input").value;
        let maxLengthStr = document.getElementById("max-length-input").value;
        let maxLength = parseInt(maxLengthStr, 10);
        eel.resize(targetImagePath, maxLength)(listUpImages);
      }
    </script>
```
