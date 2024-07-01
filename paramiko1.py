import threading

import paramiko

def find_file(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:

        STR_SEARCH = "Login failed"
        PATH_SEARCH = "/var/log/system.log"



        ssh.connect(host, username="admin", password="admin")

        stdin, stdout, stderr = ssh.exec_command(f"grep -H '{STR_SEARCH}' '{PATH_SEARCH}'")

        for line in stdout:
            print(f"Host: {host} --> {line.strip()}")
    except Exception as e:
        print("Failed to search !!")
    finally:
        ssh.close()

def main():
    with open("hosts.txt", "r") as f_ob:
        hosts = f_ob.read().splitlines()
    for host in hosts:
        find_file(host)
    threads = []

    for host in hosts:
        thread = threading.Thread(target=find_file,args=(host,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
