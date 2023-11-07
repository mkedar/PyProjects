import paramiko # pip install paramiko
import os
import time

# Set up the SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the Red Pitaya
try:
    ssh.connect(hostname='192.168.137.189', username='root', password='root')
    
    # List of commands to execute
    commands = [
        'echo "Entering RP from Python"',
        'ls -l',
        # Add more commands as needed

        # Shutdown RP Machine
        'shutdown now',
    ]
    
    # Execute each command
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"Executing: {command}")
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
        time.sleep(2)
finally:
    # Close the SSH connection
    ssh.close()

# Shutdown Windows Machine 
shutdown_command = 'shutdown /s /t 1'  
os.system(shutdown_command)
