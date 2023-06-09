def find_max_decreasing_sequence(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = lines[1:]
    luminosity_values = [int(line.split(';')[2]) for line in lines]
    longest_sequence = []
    current_sequence = []
    for luminosity in luminosity_values:
        if not current_sequence or luminosity <= current_sequence[-1]:
            current_sequence.append(luminosity)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [luminosity]
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence
    start_index = luminosity_values.index(longest_sequence[0])
    start_date, start_time = lines[start_index].split(';')[:2]
    return len(longest_sequence), f'{start_date} {start_time}'


filename = 'alpha_oriona.csv'

result = find_max_decreasing_sequence(filename)
with open('result.txt', 'w') as file:
    file.write(str(result[0]) + '\n')
    file.write(result[1] + '\n')
