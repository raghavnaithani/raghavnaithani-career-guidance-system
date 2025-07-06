from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder='../frontend/templates')

# Configure upload folder (create a 'uploads' directory in your project)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

# Add this new route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return {'error': 'No file uploaded'}, 400
    
    file = request.files['resume']
    
    if file.filename == '':
        return {'error': 'No selected file'}, 400
    
    if file and file.filename.endswith('.pdf'):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return {'status': 'success', 'message': 'File uploaded successfully'}
    else:
        return {'error': 'Only PDF files are allowed'}, 400

if __name__ == '__main__':
    app.run(debug=True)