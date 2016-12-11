import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, send_file
from werkzeug.utils import secure_filename
from io import BytesIO

UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ['GET','POST'])
def upload_file():
	if request.method == 'POST':
		 file = request.files['file']
		 if file.filename == '':
		 	return redirect(request.url) #loop back if no file
		 if file:
		 	#filename = secure_filename(file.filename)
		 	#file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		 	#return redirect(url_for('uploaded_file', filename=filename))
		 	byte_io = BytesIO()
		 	file.save(byte_io)
		 	byte_io.seek(0)
		 	return send_file(byte_io, mimetype='image')
	return render_template('upload.html')

@app.route('/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__=='__main__':
	app.run(debug=True)