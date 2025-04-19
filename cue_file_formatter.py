import re
import sys


def parse_cue_sheet(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Regular expression to match tracks
    track_pattern = re.compile(
        r"TRACK \d+ AUDIO\s+TITLE \"(.+?)\"\s+PERFORMER \"(.+?)\"\s+FILE \"(.+?)\" WAVE\s+INDEX 01 (\d{2}:\d{2}:\d{2})",
        re.MULTILINE,
    )

    tracks = track_pattern.findall(content)

    # Dictionary to store tracks and check duplicates
    track_dict = {}

    for title, performer, file_path, index in tracks:
        if (
            file_path not in track_dict
        ):  # Check if the file path is already added to avoid duplicates
            track_dict[file_path] = f"{index} {performer} - {title}"

    return sorted(track_dict.values(), key=lambda x: x.split()[0])  # Sort by index time


def save_new_format(tracks, output_filename):
    with open(output_filename, "w") as file:
        for track in tracks:
            file.write(track + "\n")


# Usage
input_filepath = sys.argv[1]
output_filepath = sys.argv[2]
if input_filepath == "" or output_filepath == "":
    print("need input file and output file")
    exit(1)

tracks = parse_cue_sheet(input_filepath)
save_new_format(tracks, output_filepath)
print("Formatted tracks saved successfully.")
