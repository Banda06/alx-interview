#!/usr/bin/python3
import sys
import signal

# Dictionary to store the count of each status code
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

def print_stats():
    """
    Function to print the statistics.
    """
    global total_file_size, status_codes_count
    print("File size:", total_file_size)
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def signal_handler(sig, frame):
    """
    Signal handler to handle keyboard interruption (CTRL + C).
    """
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    
    if len(parts) < 7:
        continue
    
    ip_address = parts[0]
    date = parts[3][1:]  # Remove the opening square bracket
    request = parts[4] + " " + parts[5] + " " + parts[6]
    
    try:
        status_code = int(parts[8])
        file_size = int(parts[9])
    except (IndexError, ValueError):
        continue
    
    if request != "\"GET /projects/260 HTTP/1.1\"":
        continue
    
    # Update the total file size
    total_file_size += file_size
    
    # Update the count for the status code
    if status_code in status_codes_count:
        status_codes_count[status_code] += 1
    
    line_count += 1
    
    # Print the statistics after every 10 lines
    if line_count % 10 == 0:
        print_stats()
