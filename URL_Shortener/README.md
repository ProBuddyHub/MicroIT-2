# 🔗 URL Shortener – Flask Based

A minimal yet powerful URL shortener built using Flask (Python), with a clean UI and full offline capability. This project allows users to shorten long URLs into compact short codes, and automatically redirects them when visited.

## 📌 Features

- 🔐 Shortens long URLs into 6-character alphanumeric codes
- 🔄 Automatically redirects to original long URLs via short links
- 📂 Stores mappings in a local `urls.json` file
- ♻️ Prevents duplicate entries by checking for already shortened URLs
- 🌐 Displays shortened link with clickable UI
- 🌓 Dark theme with clean modern design
- 🧩 Fully local — No database or external requests needed

## 🧱 Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python 3 with Flask
- **Storage**: JSON file for persistence (`urls.json`)

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ProBuddyHub/MicroIt-2.git
   cd url-shortener-flask

2. **Install Flask**
   ```bash
   pip install flas

3. **Run the app**
   ```bash
   python app.py

4. **Open your browser and go to: http://127.0.0.1:5000**

---

**File Structure**

url-shortener/
│
├── app.py                 # Main Flask application
├── urls.json              # JSON file storing long-short URL mappings
├── templates/
│   └── url_shortener.html # HTML frontend


## 🧠 **How It Works**

  -  When a user submits a URL, the backend checks for duplication.

  -  If not found, a random 6-character code is generated.

  -  The mapping is saved in urls.json.

  -  When /shortcode is visited, Flask redirects to the original URL.

## 🔐 **Security Notes**

  -  This version is for educational or small local use.

  -  No input validation/sanitization is performed on URLs.

  -  Not intended for production deployment without proper checks and hosting security.

##💡 **Future Improvements**

  -  Add user authentication and dashboard

  -  Custom short code support

  -  Analytics on URL visits

  -  QR code generation

  -  Docker containerization


