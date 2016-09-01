"""
Small class to extract timing details from distracting the items to be timed.

The purpose of this class is to measure the time some python code takes by
using the "with" function.

**Source**: Jeff Preshing has a blog of useful code - mostly in C++.  This
code is at:

http://preshing.com/20110924/timing-your-code-using-pythons-with-statement/

Jeff's example of how to use it:
    import httplib

    with Timer() as t:
        conn = httplib.HTTPConnection('google.com')
        conn.request('GET', '/')

    print('Request took %.03f sec.' % t.interval)

Jeff's reasons for doing it this way is explained at the URL above.

**Modifications** by deeppunster:

1.  Added documentation

2.  Changed time.clock to time.process_time since time.clock has been
    depricated since Python 3.3.

"""

import time

class JPTimer:
    """
    Class to time something using the "with" statement.
    """
    def __init__(self):
        """
        Predefine all internally used variables.

        Note - this is an attempt to further reduce overhead and further
        documentation.
        """
        self.start = None
        self.end = None
        self.interval = None

    def __enter__(self):
        """
        Start timing something.

        Note - the with statement will invoke this automatically.
        :return: an instance of this class
        """
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        """
        Stop timing something and calculate the difference.

        Note - the with statement will invoke this automatically.
        :param args:
        :return:
        """
        self.end = time.process_time()
        self.interval = self.end - self.start
