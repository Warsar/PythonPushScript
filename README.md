# PythonPushScript
## What does it do?
PPS allows us to push any script to a Linux based server; execute it and display the output on your local PC. This is especially useful if
you don’t want to waste time manually copying the script to the required server. Since it leaves no file behind on the remote server you
don’t have to worry about stacking up useless files wondering weeks later if you still need it or not and if it’s not deprecated yet.
Keeping the scripts you use in 1 location guarantees not accidentally using deprecated versions of your scripts.

There is probably a better way to do this using existing applications but this was interesting to create and useful in my situation where
we don't use any tool to easily deploy new servers or changes.

## Requirements
- Python installed
- SSH and SFTP access to remote server
- Paramiko package for Python

## Todo
This is just something I created when I had free time at work but there are some things I want to add:
- Upload multiple files at once (in case the script needs data from another file)
- Upload to multiple servers
