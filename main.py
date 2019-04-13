from flask import Flask, request, render_template,redirect, url_for
from werkzeug.utils import secure_filename
import os
from utils import Classifier


app = Flask(__name__,template_folder="templates", static_folder="uploads")
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def hello():
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        file = request.files['file']

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            # return url_for(filename)
            classifier = Classifier()
            result = classifier.classify(filename)
            print(result)
            return render_template('index.html',result=result, file=filename, form=False)
    return render_template('index.html',form=True)

if __name__ == "__main__":
    app.run()
