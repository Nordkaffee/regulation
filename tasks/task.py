""" Abstract Task """


class Task:
    """Abstract base class for all tasks.

    """

    def __init__(self):
        pass

    def execute(self):
        raise NotImplementedError('Task.execute is an abstract function.')