#!/usr/bin/python3
import sys

# Dictionary to store status code counts
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

# Variable to track the total file size
total_file_size = 0
line_count = 0

def print_stats():
    """Prints the current statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

try:
    # Read stdin line by line
    for line in sys.stdin:
        line = line.strip()
        line_count += 1
        
        # Split line into components
        parts = line.split()
        if len(parts) < 7:
            continue
        
        # Extract status code and file size
        status_code = parts[-2]
        try:
            file_size = int(parts[-1])
            total_file_size += file_size
        except ValueError:
            continue
        
        # Update status code count if it is a valid code
        if status_code in status_counts:
            status_counts[status_code] += 1
        
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print statistics on keyboard interrupt
    print_stats()
    raise

# Print final statistics after all lines have been processed
print_stats()
