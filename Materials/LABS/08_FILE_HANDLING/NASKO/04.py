import os

file = {}

directory = "../"

for element in os.listdir(directory):
    f = os.path.join(directory,element)
    if os.path.isfile(f):
        ext = os.path.splitext(f)[1]
