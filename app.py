from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from image_processing import processing

app = Flask(__name__)

images_folder = os.path.join("static", "images")

app.config['SECRET_KEY'] = 'thisisasecrete'
app.config['UPLOADED_IMAGES_DEST'] = 'static/images'
app.config['DISPLAY_IMAGES_PATH'] = images_folder
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ["JPG", "JPEG", "PNG"]
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
            image = request.files["inpFile"]
            if image.filename == "":
                flash("Image must have a filename")
                return redirect(request.url)
            if not allowed_image(image.filename):
                flash("That image extension is not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOADED_IMAGES_DEST"], filename))
            return redirect(url_for('.result', img_name=filename))
    return render_template('upload_image.html')

@app.route("/result/<img_name>")
def result(img_name):
    class_names, prediction, probabilities = processing(img_name)
    pict = url_for('.send_file', filename=img_name)
    return render_template('result.html', pict = pict, class_names=class_names, prediction=prediction, probabilities=probabilities)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOADED_IMAGES_DEST'], filename)

@app.route("/about")
def about():
    return render_template('about.html')
