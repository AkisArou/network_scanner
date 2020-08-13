import threading

class ThreadJob(threading.Thread):
    def __init__(self, callback: callable, interval: int):
        self.callback = callback
        self.event = threading.Event()
        self.interval = interval
        super(ThreadJob, self).__init__()

    def run(self):
        while not self.event.wait(self.interval):
            self.callback()

