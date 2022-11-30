from threading import Thread, Event


class ConvertThread(Thread):
    def __init__(self, main, debug=False):
        super().__init__()
        self.main = main
        self.working = True
        self.paused = False
        self.count = 0
        self.access_key = self.main.config['access_key']
        self.secret_key = self.main.config['secret_key']
        self.region = self.main.config['region']
        self._stop_event = Event()
        self._pause_event = Event()

    def run(self):
        pass

    def stop(self):
        self._stop_event.set()

    def should_stop(self):
        return self._stop_event.is_set()

    def pause(self):
        self._pause_event.set()

    def resume(self):
        self._pause_event.clear()

    def should_pause(self):
        return self._pause_event.is_set()
