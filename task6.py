import os
import shutil
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--source", required=True)
parser.add_argument("--days", type=int, required=True)
parser.add_argument("--size", type=int, required=True)
args = parser.parse_args()

today = datetime.date.today()

for file in os.listdir(args.source):
    filePath = os.path.join(args.source, file)
    mod_date = datetime.date.fromtimestamp(os.path.getmtime(filePath))
    size = os.path.getsize(filePath)

    if (today - mod_date).days > args.days:
        if not os.path.exists(os.path.join(args.source, "Archive")):
            os.makedirs(os.path.join(args.source, "Archive"))
        shutil.move(filePath, os.path.join(args.source, "Archive"))
    
    elif size < args.size:
        if not os.path.exists(os.path.join(args.source, "Small")):
            os.makedirs(os.path.join(args.source, "Small"))
        shutil.move(filePath, os.path.join(args.source, "Small"))

#python task6.py --source "task6" --days 0 --size 1