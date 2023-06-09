def roads(*args):
    roads_dict = {'short': [], 'long': [], 'very long': [], 'wonderful': []}
    for road in args:
        if len(road) >= 2 and sum([1 for letter in road if letter.isupper()]) >= 2:
            roads_dict['wonderful'].append(road)
        elif len(road) <= 10:
            roads_dict['short'].append(road)
        elif len(road) <= 25:
            roads_dict['long'].append(road)
        else:
            roads_dict['very long'].append(road)
    for key in roads_dict:
        roads_dict[key].sort()
    return roads_dict


data = [
 'road through the Forest',
 'road along the bank of a Clear stream',
 'In the Clouds',
 'on the field',
 'under the Magic Oak Tree'
]
print(roads(*data))
