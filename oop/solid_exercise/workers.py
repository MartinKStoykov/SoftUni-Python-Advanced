class Worker:

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()

class SuperWorker(Worker):

    def work(self):
        print("I work very hard!!!")
