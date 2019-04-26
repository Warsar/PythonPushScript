import sys
import os
import platform
import getpass

try:
    import paramiko
    import warnings
    warnings.filterwarnings(action='ignore',module='.*paramiko.*')

    # User input
    remote_ip = raw_input('IP: ')
    script_file=raw_input('File: ')
    execute_command=raw_input('Specify the command needed to execute the script: ')
    remote_username = raw_input('Username: ')

    # Where to place the script
    script_file_path = '/tmp/' + script_file

    # Connect to remote host
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(remote_ip, username=remote_username, password=getpass.getpass('Password: '))
    print "Opened SSH-connection: " + remote_username + "@" + remote_ip


    # Setup sftp connection and transmit the script
    print "Opening SFTP-connection: " + remote_username + "@" + remote_ip
    sftp = client.open_sftp()
    print "Copying file to " + script_file_path + " started"
    sftp.put(script_file, script_file_path)
    print "Copying file to " + script_file_path + " completed"

    # Run the transmitted script remotely without args and show its output.
    # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
    print "Executing script with: " + execute_command
    stdout = client.exec_command('cd /tmp;'+ execute_command)[1]


    sftp.remove(script_file_path)
    print "Deleted file " + script_file_path + " completed"


    print "Closing SFTP-connection: " + remote_username + "@" + remote_ip
    sftp.close()

    print "Closing SSH-connection: " + remote_username + "@" + remote_ip
    client.close()

    # Output of script
    print "SCRIPT OUTPUT:"
    for line in stdout:
        # Process each line in the remote output
        print line


    sys.exit(0)
except IndexError:
    pass
