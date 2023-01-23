import os
import re

pattern = re.compile(r'S(\d+)E(\d+)')

for file in os.listdir():
    if file.endswith(".mp4"):
        match = pattern.search(file)
        if match:
            s = match.group(1)
            e = match.group(2)
            for srt_file in os.listdir():
                if srt_file.endswith(".srt"):
                    if f'S{s}E{e}' in srt_file:
                        os.rename(srt_file, file[:-4] + ".srt")
                        print(f'{srt_file} renamed to {file[:-4] + ".srt"}')
                        break
