import threading

class _Queue:
    """

    """

    def __init__(self):
        self._list = []
        self._condition = threading.Condition()

    def enqueue(self, element):
        """

        """
        with self._condition:
            self._list.append(element)
            self._condition.notify()

    def is_empty(self):
        """

        """
        with self._condition:
            return len(self._list) == 0

    def dequeue(self):
        """

        """
        with self._condition:
            while self.is_empty():
                self._condition.wait()
            return self._list.pop(0)


class _Worker(threading.Thread):
    """

    """

    def __init__(self, get_next_task):
        super(_Worker, self).__init__()
        self._running = True
        self._get_next_task = get_next_task

    def run(self):
        """

        """
        while self._running:
            task = self._get_next_task()
            self._execute(task)

    def _execute(self, task):
        """

        """
        task.execute()

    def stop(self):
        self._running = False


class EventQueue:
    """

    """

    def __init__(self):
        self._queue = _Queue()
        self._worker = _Worker(self._queue.dequeue)
        self._worker.start()

    def enqueue(self, task):
        self._queue.enqueue(task)

    def stop(self):
        self._worker.stop()