import os
import subprocess
import argparse
import random
from math import ceil

parser = argparse.ArgumentParser()
parser.add_argument(
    "-s", "--source",  required=True)
parser.add_argument("-d", "--destination",
                    default=None)
parser.add_argument(
    "-c", "--count", type=int, default=None)
parser.add_argument(
    "-f", "--frame", type=int, default=10)
parser.add_argument(
    "-l", "--log",  action="store_true")
parser.add_argument("-e", "--extended",
                    action="store_true")
args = parser.parse_args()

# Work out the paths to the files.
source = os.path.abspath(args.source)
if args.destination is None:
    destination = os.path.join(source, "mix.mp3")
else:
    destination = os.path.abspath(args.destination)

# Get a list of mp3 files to mix.
mp3Files = [os.path.join(source, f)
            for f in os.listdir(source) if f.endswith(".mp3")]
if args.count is not None:
    mp3Files = random.sample(mp3Files, args.count)

# Generate a list of start times within each file.
startTimes = []
for mp3_file in mp3Files:
    duration = float(subprocess.check_output(
        ['ffprobe', '-i', mp3_file, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")]))
    startTimes.append(random.randint(0, int(duration - args.frame)))

# start_times = random.sample(start_times, args.count)

# Generate a list of track frame options.
options = []
outputs = []
for i, start_time in enumerate(startTimes):
    input_file = mp3Files[i]
    start = start_time
    duration = args.frame
    fadeDuration = args.frame // 3 if args.extended else 0
    fadeIn = f"afade=t=in:ss=0:d={fadeDuration}"
    fadeOut = f",afade=t=out:st={duration-fadeDuration}:d={fadeDuration}"
    options.append(
        f"ffmpeg -ss {start} -to {start+duration} -i \"{input_file}\" -af {fadeIn}{fadeOut} -y  output{i}.mp3")
    outputs.append(f"output{i}.mp3")

outputs = "|".join(outputs)
options.append(f"ffmpeg -i concat:{outputs} -c copy {destination}")
print(options)

if args.log:
    print("--- processing files:",
          ", ".join([os.path.basename(f) for f in mp3Files]))

for command in options:
    subprocess.call(command)
if args.log:
    print("--- done!")

# python task7.py -s "task7" -c 2 -f 5 -l -e -d "task7/mix.mp3"
