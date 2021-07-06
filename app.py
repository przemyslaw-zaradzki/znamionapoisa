from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from image_processing import processing

app = Flask(__name__)

images_folder = os.path.join("static", "images")

app.config['SECRET_KEY'] = 'thisisasecrete'
app.config['UPLOADED_IMAGES_DEST'] = 'static/images'
app.config['DISPLAY_IMAGES_PATH'] = images_folder
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ["JPG"]
app.config['MAX_IMAGE_FILESIZE'] = 1 * 1024 * 1024

def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                flash("Image must have a filename")
                return redirect(request.url)
            if not allowed_image(image.filename):
                flash("That image extension is not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)
            #image.save(os.path.join(app.config["UPLOADED_IMAGES_DEST"], filename))
            image.save(app.config["UPLOADED_IMAGES_DEST"] + "/skinn.jpg")
            return redirect(url_for('.result'))
    return render_template('upload_image.html')

@app.route("/result")
def result():
    prediction = processing(os.path.join(app.config["UPLOADED_IMAGES_DEST"], "skinn.jpg"))
    pict = os.path.join(app.config["DISPLAY_IMAGES_PATH"], "skinn.jpg")
    return render_template('result.html', pict = pict, p=prediction)

@app.route("/about")
def about():
    return render_template('about.html')
