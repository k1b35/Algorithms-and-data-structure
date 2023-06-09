n = int(input())
friends = []
for i in range(n):
    friends.append(input().lower())

friend_dict = {}
while True:
    friend = input().strip()
    if not friend:
        break
    for f in friends:
        if (len(friend) >= len(f)) and (f in friend.lower()):
            friend_dict[f] = friend.upper()
            break

for f in friends:
    if f in friend_dict:
        print(f + ": " + friend_dict[f])
    else:
        print(f + ":")