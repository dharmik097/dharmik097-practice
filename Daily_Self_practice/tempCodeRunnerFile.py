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