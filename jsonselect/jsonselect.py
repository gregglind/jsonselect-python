"""



"""

# for now, just reuse the gross implementation we had before!
from jsonmangle import Ql


def compile_selector(selector):
    return lambda thing:  Ql(selector,thing)

class JSONSelect(object):
    def __init__(self,selector):
        # parse the selector?
        self.compiled=compile_selector(selector)
        

    def __call__(self,thing):
        """ apply the selector to the thing,
            possibly returning a selector?
        """
        return self.compiled(thing)


Q = JSONSelect


