import logging

# Set up logging configuration
log_file = 'keylog.txt'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to handle key presses
def keylogger():
    print("Keylogger started. Press Enter to log each key. Press Ctrl+C to stop.")
    try:
        while True:
            key = input()
            logging.info(key)
    except KeyboardInterrupt:
        print("\nKeylogger stopped by user.")

# Run the keylogger
if __name__ == '__main__':
    keylogger()
