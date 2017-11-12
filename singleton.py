#
##  Singleton Decorator modified from Paul Manta's (https://stackoverflow.com/a/7346105)
#
class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    #
    ## Just call something decorated with a Singleton to get the instance. Not (guaranteeded, but don't try it) thread-safe.
    #
    def __call__(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
