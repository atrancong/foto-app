import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, send_file
from werkzeug.utils import secure_filename
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def upload_file():
	if request.method == 'POST':
		 file = request.files['file']
		 if file.filename == '':
		 	return redirect(request.url) #loop back to front page if no file
		 if file:
		 	byte_io = BytesIO()
		 	file.save(byte_io) #save file contents to memory
		 	byte_io.seek(0)
		 	return send_file(byte_io, mimetype='image')
	return render_template('upload.html')

if __name__=='__main__':
	app.run(debug=True)