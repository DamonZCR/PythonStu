import sys, os

this_dir = os.path.dirname(__file__)
print(this_dir)

filename = os.path.realpath("{0}/relative/file.path".format(this_dir))
print(filename)

