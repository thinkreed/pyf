from concurrent.futures import ThreadPoolExecutor


class Workers:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=4)

    def get_worker(self):
        return self.executor
