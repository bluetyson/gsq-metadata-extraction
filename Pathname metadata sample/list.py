import sys, os

root = sys.argv[1]

for root, folder, files in os.walk(root):
    for file in files:
        print(os.path.join(root, file))