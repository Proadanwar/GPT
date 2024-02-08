from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Your bot is alive!"

# Route to keep your bot alive
@app.route('/keep-alive')
def keep_alive():
    # Perform any additional actions to keep your bot alive here
    return "Bot is still alive!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
