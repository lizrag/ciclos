import os
import shutil
import logging

logging.basicConfig(filename='sync.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

list_dict = [
    {
        "origin":"C:/Users/laura/OneDrive/Documents/prueba/server_A",
        "dest":"C:/Users/laura7OneDrive/Documents/server_A"
    },
    {
        "origin":"C:/Users/laura/OneDrive/Documents/prueba/server_B",
        "dest":"C:/Users/laura/OneDrive/Documents/server_B"
    },
    {
        "origin":"C:/Users/laura/OneDrive/Documents/prueba/server_C",
        "dest":"C:/Users/laura/OneDrive/Documents/server_C"
    }
]

def move_files(origin, destination):
    shutil.copy(origin, destination)



for dictionary in list_dict:
    origin = dictionary["origin"]
    destination = dictionary["dest"]
    try:
        shutil.copy(origin, destination)
        logging.info("Sync successful!")
        print("Copied successfully")
    except Exception as e:
        print(f"Failed to copy: {e}")
        logging.error("Error syncing directories:")



