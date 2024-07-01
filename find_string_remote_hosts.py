import paramiko
import threading

# File containing the list of hosts
HOSTS_FILE = "hosts.txt"

# File to search on each host
FILE_TO_SEARCH = "/path/to/file.txt"

# String to search for
SEARCH_STRING = "search_string"


# Function to search for a string on a remote host
def search_on_host(host):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the host (replace 'username' and 'password' with actual credentials)
        ssh.connect(host, username='your_username', password='your_password')

        # Execute the grep command
        stdin, stdout, stderr = ssh.exec_command(f"grep -H '{SEARCH_STRING}' '{FILE_TO_SEARCH}'")

        # Print the output
        for line in stdout:
            print(f"{host}: {line.strip()}")

        # Close the connection
        ssh.close()
    except Exception as e:
        print(f"Failed to search on {host}: {e}")


# Read the list of hosts
with open(HOSTS_FILE, 'r') as f:
    hosts = f.read().splitlines()

# Create and start a thread for each host
threads = []
for host in hosts:
    thread = threading.Thread(target=search_on_host, args=(host,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Search completed on all hosts.")
