friends = input("Enter 3 friends names").split(",")

people = open("people.txt", "r")
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open("nearby_friends.txt", "w")

for friend in friends_nearby_set:
    nearby_friends_file.write(friend)

nearby_friends_file.close()
