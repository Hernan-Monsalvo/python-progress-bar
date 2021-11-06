import sys
import math

def foo():
    # do something
    pass

def progress_bar(total, progress):

    pos =  math.floor(progress / total * 100)

    bar_str = "[                                                 ] {}/{}".format(progress, total)
    sys.stdout.flush()
    sys.stdout.write("\r%d%%" % pos)
    bar = pos/2
    bar  = math.floor(bar)

    for i in range(bar):
        if i > 0:
            bar_str = foo(bar_str, i, "■")

    sys.stdout.write("  {}".format(bar_str))
