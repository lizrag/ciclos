import shutil
import logging

def sync_data(origin, dest):
    try:
        shutil.copy2(origin, dest)
        logging.info("Sync successful!")
        print("Copied successfully")
    except Exception as e:
        print(f"Failed to copy: {e}")
        logging.error("Error syncing directories:")
