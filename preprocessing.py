import os
import time

from text_extraction import get_text  # Import your custom functions
from chatbot import train_model  # Import your custom functions

file_path = 'data-dev/'

def read_files(website_name):
    file_path_full = os.path.join(file_path, website_name)

    try:
        with open(file_path_full, "r") as file:
            for line in file:
                try:
                    print(line)
                    get_text(line)
                except Exception as e:
                    # Handle or log the exception here
                    print(f"Error processing line: {line}")
                    print(f"Error message: {str(e)}")
                    pass

    except FileNotFoundError:
        print(f"File not found: {file_path_full}")
        pass

def start_custom_training():
    train_model("Learn all the context that I will be putting here. The user will ask you questions about the same.")

    file_path_scraped = 'data-dev/extracted_files/'

    file_names = [f for f in os.listdir(file_path_scraped) if os.path.isfile(os.path.join(file_path_scraped, f))]

    for file_name in file_names:
        file_path = os.path.join(file_path_scraped, file_name)

        try:
            with open(file_path, 'r') as file:
                print("read")
                train_model(file.read())
        except Exception as e:
            # Handle or log the exception here
            print(f"Error processing file: {file_path}")
            print(f"Error message: {str(e)}")
            pass

    print("Custom training completed.")

try:
    start_custom_training()
    
except Exception as e:
    print(f"Error: {str(e)}")

