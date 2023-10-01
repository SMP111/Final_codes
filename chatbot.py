import g4f


print(g4f.Provider.Ails.params)  # supported args

import g4f

from website_data import get_all_links
from preprocessing import start_custom_training

x = False
def init(link):
    while(not x):    
        get_all_links(link, None)
        y = start_custom_training()

        if(y == True):
            break

def send_message(msg):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg}],
        stream=True
    )

    return response

