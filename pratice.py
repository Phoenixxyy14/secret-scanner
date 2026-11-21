import os

folder = "test_files"
keywords = ['api_key', 'secret', 'password', 'token']
total = 0

files = os.listdir(folder)

for file in files:
    path = folder + '/' + file
    print('scanning', file)
    with open(path) as f:
        for line in f:
            for word in keywords:
                if word in line:
                    print("HIT:", file, "-", line.strip())
                    total = total + 1

print("Total hits:", total)