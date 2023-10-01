import os

from text_extraction import get_text 
from custom_training import train_model

file_path = '/../data-dev/extracted_files/'

def read_files(website_name):
    file_path_full = os.path.join(file_path, website_name)

    with open(file_path_full, "r") as file:
        for line in file:
            get_text(line)


def start_custom_training():
    file_names = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]

    for file_name in file_names:
        file_path = os.path.join(file_path, file_name)

        with open(file_path, 'r') as file:
            train_model(file.read())

    print("Custom training completed.")

    return True


