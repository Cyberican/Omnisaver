import subprocess
import os

# Path to the script you want to start in the operations directory
operations_dir = os.path.join(os.path.dirname(__file__), 'operations')
script_name = 'get_processes.py'  # Change this to your actual script name

script_path = os.path.join(operations_dir, script_name)

if os.path.isfile(script_path):
    # Start the process
    # process = subprocess.Popen(['python', script_path])
    # print(f"Started process with PID: {process.pid}")
    process = subprocess.run(['python', script_path], capture_output=True, text=True)
    print(f"Process Output: {process}")
else:
    print(f"Script not found: {script_path}")