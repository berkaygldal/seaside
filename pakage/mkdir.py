import os

def mkdir(dirname):
    try:
        os.mkdir(dirname)
    except Exception as e:
        return e