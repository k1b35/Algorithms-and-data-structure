capitals = []

file_in = open("capitals.txt", encoding="UTF-8")
for line in file_in:
    capitals.append(line.rstrip("\n"))
    # print(line)
file_in.close()


def group_capitals(capitals):
    intervals = {}

    for capital in capitals:
        city, country, population = capital.split()
        population = int(population)

        interval = (population // 100) * 100

        if interval in intervals:
            intervals[interval].append(city)
        else:
            intervals[interval] = [city]

    sorted_intervals = sorted(intervals.items(), key=lambda x: x[0])

    for interval, cities in sorted_intervals:
        lower_bound = interval
        upper_bound = interval + 100
        print(f'{lower_bound} - {upper_bound}: {", ".join(sorted(cities))}')


group_capitals(capitals)
