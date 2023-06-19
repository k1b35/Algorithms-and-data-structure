import random
from datetime import datetime, timedelta


def generate_random_messages(num_messages):
    employees = ["Сотрудник 1", "Сотрудник 2", "Сотрудник 3"]
    messages = []
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    for i in range(num_messages):
        employee = random.choice(employees)
        message_time = start_date + timedelta(seconds=random.randint(0, 604800))
        message = {"сотрудник": employee, "время": message_time}
        messages.append(message)

    return messages



def find_employee_with_most_messages(messages):
    message_counts = {}

    for message in messages:
        employee = message["сотрудник"]

        if employee in message_counts:
            message_counts[employee] += 1
        else:
            message_counts[employee] = 1

    max_messages_employee = max(message_counts, key=message_counts.get)
    message_count = message_counts[max_messages_employee]

    return max_messages_employee, message_count



random_messages = generate_random_messages(100)


max_messages_employee, message_count = find_employee_with_most_messages(random_messages)


print("Сотрудник с наибольшим количеством сообщений:")
print("Сотрудник:", max_messages_employee)
print("Количество сообщений:", message_count)
