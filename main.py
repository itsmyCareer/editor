from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        result = request.form

        f = request.files['file']
        t = result.get('title')
        u = result.get('user')
        o = secure_filename(u + '/'+f.filename)
        f.save('imgs' + '/' + o)
        return '성공'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')