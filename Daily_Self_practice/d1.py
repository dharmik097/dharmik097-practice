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

#------------------------------------------------------

#  2 Why This Matters:
# Cybersecurity: Finding open ports helps detect unauthorized services or malware.

# DevOps: Useful in server configuration and firewall rule verification.

# Cloud: Often used to secure and audit cloud VMs.

# Write a Python script that:

# Lists all open TCP ports.

# Shows the associated process name.

# Works on Linux/macOS (Windows requires admin and slight tweaks).
import subprocess

def list_open_ports():
    print("Open TCP Ports and Associated Processes:\n")

    try:
        # Run the lsof command to list open internet connections (Linux/macOS)
        result = subprocess.run(['lsof', '-iTCP', '-sTCP:LISTEN', '-Pn'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

        if result.returncode != 0:
            print("Error running lsof:", result.stderr)
            return

        lines = result.stdout.strip().split('\n')
        header = lines[0]
        entries = lines[1:]

        for line in entries:
            print(line)

    except FileNotFoundError:
        print("Error: 'lsof' not found. Install it using your package manager.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    list_open_ports()
