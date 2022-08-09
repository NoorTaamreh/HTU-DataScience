import portalocker

with portalocker.Lock('TestPython.txt') as fh:
    fh.write('first instance')