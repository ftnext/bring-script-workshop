Notice: Work at the repository **root** directory.

```
pwd
cd ..  # if you are in the gui directory
```

## First example of Flask

### 1. Create boilerplate for Flask app.  

(I created the helper command `bringscript`)

```
# Create hello app's boilerplate codes in the current directory (= repository root)
bringscript web hello .
```

After: It will create the gui directory.

```
├── first_step_script
├── webapp
│   ├── webapp.py
│   └── templates
│       └── hello.html
└── target_images
```

### Workaround (if the `bringscript` command does not work well)

Command line

```
mkdir -p webapp/templates
touch webapp/webapp.py
touch webapp/templates/hello.html
```

webapp/webapp.py

```python
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hello")
def hello():
    return render_template("hello.html")


if __name__ == "__main__":
    app.run(debug=True)
```

webapp/templates/hello.html

```HTML
<!DOCTYPE html>
<html>
  <body>

  </body>
</html>
```

### 2. Change webapp.py

Before

```python
@app.route("/hello")
def hello():
    return render_template("hello.html")
```

After

```python
from datetime import datetime  # Added

@app.route("/hello")
def hello():
    message = f"Hello World at {datetime.now()}"  # Added
    return render_template("hello.html", message=message)  # Edited
```

### 3. Change HTML in hello.html

Before

```html
  <body>

  </body>
```

After

```html
  <body>
    <p>{{ message }}</p>
  </body>
```

### Execution

```
cd webapp
python webapp.py 
```

## Convert GUI to Web app

Edit `webapp.py` and `templates/hello.html`.

### 1. Edit `webapp.py`

Copy the `gui/gui.py` code and paste it in `webapp.py`.

```python
import uuid  # Added
from pathlib import Path  # Added

from flask import Flask, render_template, request  # Edited
from PIL import Image  # Added
from werkzeug.utils import secure_filename  # Added

app = Flask(__name__, static_folder="images")  # Edited

# :  same as gui.py


# @eel.expose  # Deleted and Changed
@app.route("/resize", methods=["GET", "POST"])
def resize():
    if request.method == "GET":
        return render_template("hello.html")

    random_id = uuid.uuid4()
    shrinked_dir_path = Path(f"images/{random_id}")
    shrinked_dir_path.mkdir(exist_ok=True, parents=True)

    max_length = int(request.form["max_length"])
    image_files = request.files.getlist("image_file")

    image_paths = []
    for image_file in image_files:
        secure_name = secure_filename(image_file.filename)
        resized_image_path = shrinked_dir_path / secure_name
        has_resized = resize_image(image_file, resized_image_path, max_length)
        if has_resized:
            image_paths.append(resized_image_path)
    return render_template("hello.html", image_paths=image_paths)
```

### 2. Edit `templates/hello.html`

After: HTML

```HTML
  <body>
    <h1>Resize image</h1>

    {% for image_path in image_paths %}
      <img src="{{ image_path }}">
    {% else %}
      <p>There were no images that needed to be reduced in size.</p>
    {% endfor %}

    <form method="post" enctype="multipart/form-data">
      <div>
        <label for="image_file">Specify image(s) to be resized in your computer:</label>
        <input id="image_file" type="file" name="image_file" accept="image/png, image/jpeg" required multiple>
      </div>
      <div>
        <label for="max-length-input">Specify max length:</label>
        <input id="max_length" name="max_length" value="300" required>
      </div>
      <div>
        <button type="submit">Send</button>
      </div>
    </form>
  </body>
```
