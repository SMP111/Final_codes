from flask import Flask, request, jsonify, render_template
import g4f

app = Flask(__name__, static_folder="static", template_folder=".")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_message = request.json.get('message', '')
    
    bot_response = send_message(user_message)
    
    return jsonify(response=bot_response)

def send_message(msg):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg}],
        stream=True
    )

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
