from flask import Flask, render_template, request, send_file, jsonify
from cryptography.fernet import Fernet
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    action = request.form['action']
    key = request.form['key']
    file = request.files['file']

    if not file or not key or not action:
        return jsonify({'error': 'Missing required fields.'})

    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        with open(filepath, 'rb') as f:
            data = f.read()

        fernet = Fernet(key.encode())

        if action == 'encrypt':
            processed_data = fernet.encrypt(data)
            result_filename = f"encrypted_{filename}"
        elif action == 'decrypt':
            processed_data = fernet.decrypt(data)
            result_filename = f"decrypted_{filename}"
        else:
            return jsonify({'error': 'Invalid action.'})

        result_path = os.path.join(RESULT_FOLDER, result_filename)
        with open(result_path, 'wb') as f:
            f.write(processed_data)

        return send_file(result_path, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/generate-key')
def generate_key():
    key = Fernet.generate_key().decode()
    return jsonify({'key': key})


if __name__ == '__main__':
    app.run(debug=True)

