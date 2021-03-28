import time
from tasks import Task


class LightsOnTask(Task):
    """

    """

    def __init__(self):
        super(LightsOnTask, self).__init__()

    def execute(self):
        """

        """
        print('Switching on lights!')
        print('Sleeping...')
        time.sleep(10)    


class LightsOffTask(Task):
    """

    """

    def __init__(self):
        super(LightsOffTask, self).__init__()

    def execute(self):
        """

        """
        print('Switching off lights!')