import os
import time
import asyncio
import subprocess
from utils import ProcessQueueManager

class Initializer:
    def __init__(self):
        self.process_manager = ProcessQueueManager.ProcessQueueManager()

    async def start_process(self, script_name):
        # Path to the script you want to start in the operations directory
        operations_dir = os.path.join(os.path.dirname(__file__), 'operations')
        script_path = os.path.join(operations_dir, script_name)
        if os.path.isfile(script_path):
            process = subprocess.Popen(['python', script_path])
            self.process_manager.add_process(process)
            print(f"Started process with PID: {process.pid}")
        else:
            print(f"Script not found: {script_path}")

    async def say_after(self, delay, what):
        await asyncio.sleep(delay)
        print(what)

    async def main(self, script_name):
        print(f"started at {time.strftime('%X')}")
        await self.say_after(1, 'Initializing...')
        await self.start_process(script_name)
        await self.say_after(2, 'Done!')
        print(f"finished at {time.strftime('%X')}")

if __name__ == "__main__":
    # Create an instance of Initializer and start the process
    initializer = Initializer()
    asyncio.run(initializer.main('run_processes.py'))
