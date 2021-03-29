""" Tasks to handle the lights """

import time
from tasks import Task


class LightsOnTask(Task):
    """Task to switch on the lights if they are not already switched on.

    """

    def __init__(self):
        super(LightsOnTask, self).__init__()

    def execute(self):
        """Switches on lights.
        
        If the lights were already on, doesn't do anything.

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
        """Switches off lights.

        If the lights were already off, doesn't do anything.

        """
        print('Switching off lights!')