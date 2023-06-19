def weather_forecast(today_weather, p_clear, q_cloudy, num_days):
    if today_weather == "ясно":
        p_current = 1
        q_current = 0
    else:
        p_current = 0
        q_current = 1

    for _ in range(num_days):
        p_clear_next = p_current * p_clear + q_current * (1 - p_clear)
        q_cloudy_next = q_current * q_cloudy + p_current * (1 - q_cloudy)
        p_current = p_clear_next
        q_current = q_cloudy_next

    if p_current > q_current:
        forecast = "ясно"
        probability = p_current
    elif p_current < q_current:
        forecast = "пасмурно"
        probability = q_current
    else:
        forecast = "равновероятно"
        probability = p_current

    return forecast, probability


today_weather = input()
p_clear = float(input())
q_cloudy = float(input())
num_days = int(input())

forecast, probability = weather_forecast(today_weather, p_clear, q_cloudy, num_days)

print(forecast)
print(probability)
