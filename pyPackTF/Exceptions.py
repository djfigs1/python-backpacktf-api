class RequestFailure(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return str(self.reason)

class NoErrorMessage(Exception):
    def __str__(self):
        return "There was no error message given with the request"