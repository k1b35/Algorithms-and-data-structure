def generate_bar_chart(numbers):
    max_height = max(numbers)
    num_columns = len(numbers)
    top_line = '* ' * (num_columns + 3)

    chart_lines = []
    for row in range(max_height, 0, -1):
        chart_line = '*'
        for num in numbers:
            if num >= row:
                chart_line += ' *'
            else:
                chart_line += '  '
        chart_line += ' *'
        chart_lines.append(chart_line)



    # Print the chart
    print(top_line)
    for line in chart_lines:
        print(line)
    # print(bottom_line)


numbers = list(map(int, input().split()))


generate_bar_chart(numbers)
