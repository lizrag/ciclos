import shutil
import logging

def sync_data(origin, dest):
    try:
        shutil.copy(origin, dest)
        # shutil.move(origin, dest, copy_function = shutil.copy)
        logging.info("Sync successful!")
        print("Copied successfully")
    except Exception as e:
        print(f"Failed to copy: {e}")
        logging.error("Error syncing directories:")


#print("Starting")