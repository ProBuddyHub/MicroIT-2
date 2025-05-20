from flask import Flask, render_template, request, redirect, jsonify
import random, string, json, os

app = Flask(__name__)
URL_DB_FILE = "urls.json"

# Load or initialize URL data
if os.path.exists(URL_DB_FILE):
    with open(URL_DB_FILE, "r") as file:
        url_data = json.load(file)
else:
    url_data = {}

def save_url_data():
    with open(URL_DB_FILE, "w") as file:
        json.dump(url_data, file, indent=4)

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def home():
    return render_template('url_shortener.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('longUrl')
    if not long_url:
        return jsonify({'error': 'No URL provided'}), 400

    # Check if already shortened
    for code, original in url_data.items():
        if original == long_url:
            short_url = request.host_url + code
            return jsonify({'shortUrl': short_url})

    # Generate unique short code
    while True:
        code = generate_short_code()
        if code not in url_data:
            break

    url_data[code] = long_url
    save_url_data()

    short_url = request.host_url + code
    return jsonify({'shortUrl': short_url})

@app.route('/<code>')
def redirect_short_url(code):
    long_url = url_data.get(code)
    if long_url:
        return redirect(long_url)
    return "Invalid short URL", 404

if __name__ == '__main__':
    app.run(debug=True)

