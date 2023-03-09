import os
import hashlib

def getMd5(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        hash = hashlib.md5(data).hexdigest()
    return hash

def findDuplicates(path):
    checksums = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            checksum = getMd5(full_path)
            if checksum in checksums:
                checksums[checksum].append(full_path)
            else:
                checksums[checksum] = [full_path]

    duplicates = {key:filenames for key,filenames in checksums.items() if len(filenames) > 1}

    for key, value in duplicates.items():
        print("Дубликаты:")
        for path in value:
            print("\t{0}".format(path))

findDuplicates('task2')