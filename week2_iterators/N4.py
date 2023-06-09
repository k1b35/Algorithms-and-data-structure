import sys


def process_comments():
    lines = iter(sys.stdin)
    line_number = 1
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            comment = line[1:].lstrip()
            output = f'Line {line_number}: {comment}'
            print(output)
        line_number += 1


process_comments()
