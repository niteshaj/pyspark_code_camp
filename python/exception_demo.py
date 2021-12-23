import sys


# Custom exception
class WrongOsError(Exception):
    pass


# we can raise an exception using raise
if not sys.platform.startswith("win32"):
    raise WrongOsError("oops.....")
