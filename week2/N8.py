def discount_checker(threshold, *purchases):
    l = []
    for i in purchases:
        if i > threshold:
            l.append(i)
    return l


print(discount_checker(1000, 500, 1500, 800, 1200, 900, 1000, -1500, 5000))
