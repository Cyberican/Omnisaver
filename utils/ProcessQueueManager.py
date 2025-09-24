# Manages a queue of processes to be executed in order.
class ProcessQueueManager:
    def __init__(self):
        self.queue = []

    def add_process(self, process):
        self.queue.append(process)

    def get_next_process(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0
    