import logging

def get_secrets():
    pass

def __main__():
    global logger
    logger = logging.getLogger('rpa_api')
    logger.setLevel(logging.DEBUG)
    print("Test")

__main__()
