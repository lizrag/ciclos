import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define source and target directories
source_dir = '/path/to/source/directory/'
target_dir = '/path/to/target/directory/'

# Define rsync options
rsync_options = {
    '--update': True,  # only copy newer files
    '--delete': True,  # delete files on target not in source
    '--exclude': ['*.tmp', '*.log'],  # exclude temporary and log files
}

# Build rsync command with options
rsync_command = ['rsync']
for option, value in rsync_options.items():
    if value is True:
        rsync_command.append(option)
    else:
        rsync_command.append(f'{option}={value}')
rsync_command.append(source_dir)
rsync_command.append(target_dir)

# Execute rsync command and log progress
try:
    subprocess.check_call(rsync_command)
    logging.info('Synchronization successful.')
except subprocess.CalledProcessError as e:
    logging.error(str(e))
    logging.error('Synchronization failed.')
