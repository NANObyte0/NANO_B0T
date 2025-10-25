from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    return get_Chat_response(msg)

def get_Chat_response(text):
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')  # النموذج الجديد (أو 'gemini-2.5-pro')
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}. Check your GEMINI_API_KEY, internet, or try 'gemini-2.5-pro'."

if __name__ == '__main__':
    app.run(debug=True)