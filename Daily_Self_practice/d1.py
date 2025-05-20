# Task Details:
# Write a Python script that:

# Checks disk usage on your system.

# Prints the total space, used space, and free space in a human-readable format (e.g., GB).

# Prints a warning if free space is below a threshold (like 20%).

import shutil
def check_disk_usage(disk_path="/"): # Default to root directory
    # Get disk usage statistics
    total, used, free = shutil.disk_usage(disk_path)
     # Convert bytes to GB
    total_gb = total / (2**30)
    used_gb = used / (2**30)
    free_gb = free / (2**30)
    
    print(f"Total space: {total_gb:.2f} GB")
    print(f"Used space: {used_gb:.2f} GB")
    print(f"Free space: {free_gb:.2f} GB")
    
    # Check if free space is below 20%
    if free / total < 0.2:
        print("Warning: Free space is below 20%!")
   
# Example usage
if __name__ == "__main__":
    check_disk_usage()