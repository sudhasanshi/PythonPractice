import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='| %(levelname)-15s | %(asctime)s | %(name)s | %(lineno)-4s ::  %(message)s')

logger = logging.getLogger("test")

# Define the command you want to execute
command = [
       'grep -rl "org" *',
       'ls',
       'pwd'
       ]

# Run the command
The stdout=subprocess.PIPE parameter captures the output of the command, which you can then access using result.stdout.
for cmd in command:
    result = subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  # Print the output
    print(result.stdout)
    print(result.stderr, end='')
  # end='' used to remove newline
#subprocess.run() is used to run the specified command.
#The shell=True parameter indicates that the command should be run in a shell.
#The check=True parameter raises a CalledProcessError if the command returns a non-zero exit code, indicating an error.
#The text=True parameter ensures that the output is returned as a string.
