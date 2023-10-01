import g4f

#from website_data import get_all_links
#from preprocessing import start_custom_training

conversation = []

def train_model(text):  
    global conversation
    conversation.append({"role": "system", "content": text})

def send_message(msg):
    global conversation
    conversation.append({"role": "user", "content": msg})

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    s = "".join(message for message in response)

    conversation.append({"role": "assistant", "content": s})
    return s

#train_model("I am Bit. Remember this variable X term{1234_1234}.")

