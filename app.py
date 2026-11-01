from flask import Flask, redirect

app = Flask(__name__)

# Main page
@app.route('/')
def home():
    return redirect("https://t.me/zadock01")

# Exact style like halo-iiab.onrender.com/admin/BMAV
@app.route('/admin/BMAV')
def admin_bmav():
    return redirect("https://t.me/zadock01")

# Your Telegram shortcut
@app.route('/telegram')
def telegram():
    return redirect("https://t.me/zadock01")

# Any name you want
@app.route('/zadock')
def zadock():
    return redirect("https://t.me/zadock01")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)