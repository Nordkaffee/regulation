import threading

class _Queue:
    """Queue implementation for the EventQueue.

    Attributes:
        _list:
            Current queue of items.
        _condition:
            Threading condition to notify worker(s).

    """

    def __init__(self):
        self._list = []
        self._condition = threading.Condition()

    def enqueue(self, element):
        """Adds an item to the back of the queue and wakes up a waiting worker.

        """
        with self._condition:
            self._list.append(element)
            self._condition.notify()

    def is_empty(self):
        """Returns True if the queue is empty and False otherwise.

        """
        with self._condition:
            return len(self._list) == 0

    def dequeue(self):
        """Removes the first item from the queue or waits if queue is empty.

        """
        with self._condition:
            while self.is_empty():
                self._condition.wait()
            return self._list.pop(0)


class _Worker(threading.Thread):
    """Worker implementation for the EventQueue.

    Attributes:
        _running:
            Flag whether the worker is running or not.
        _get_next_task:
            Function to get the next task from the queue. Must be passed at
            construction.

    """

    def __init__(self, get_next_task):
        super(_Worker, self).__init__()
        self._running = True
        self._get_next_task = get_next_task

    def run(self):
        """Starts the worker.

        """
        while self._running:
            task = self._get_next_task()
            self._execute(task)

    def _execute(self, task):
        """Executes the assigned task.

        """
        task.execute()

    def stop(self):
        """Stops the worker.

        """
        self._running = False


class EventQueue:
    """Implementation of a task based event queue.

    Tasks can be enqueued and a background worker takes care of each task
    one-by-one.

    Attributes:
        _queue:
            Queue with a condition to notify sleeping workers upon new items.
        _worker:
            Worker which waits for new items in the queue and handles them.

    """

    def __init__(self):
        self._queue = _Queue()
        self._worker = _Worker(self._queue.dequeue)
        self._worker.start()

    def enqueue(self, task):
        """Adds an item to the back of the queue.

        """
        self._queue.enqueue(task)

    def stop(self):
        """Stops the worker.

        """
        self._worker.stop()