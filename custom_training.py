import g4f

def train_model(text):  
    try:
        with open("custom_model_id.txt", "r") as model_id_file:
            model_id = model_id_file.read().strip()
    except:
        model_id = "text-davinci-003"

    response = g4f.Completion.create(
        model  = model_id,
        prompt = text
    )

    model_id = response['id']

    with open("custom_model_id.txt", "w") as model_id_file:
        model_id_file.write(model_id)

    

    