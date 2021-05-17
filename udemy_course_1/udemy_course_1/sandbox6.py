from collections import Counter, defaultdict, deque, namedtuple, OrderedDict


device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])
print(temperature_counter[14.5])

print(Counter({"hello": 5, "hi": 3})["hi"])


my_dict = {"hello": 5}
try:
    print(my_dict["hi"])
except KeyError:
    print("KEY ERROR")

coworkers = [("Rolf", "MIT"), ("Jen", "Oxford"), ("Rolf", "Cambridge"),
             ("Charlie", "Manchester")]
what_we_want = {
    "Rolf": ["MIT", "Cambridge"],
    "Jen": ["Oxford"],
    "Charlie": ["Manchester"]
}

alma_maters = dict()

for coworker in coworkers:
    if coworker[0] not in alma_maters:
        alma_maters[coworker[0]] = []
    alma_maters[coworker[0]].append(coworker[1])

assert what_we_want == alma_maters

print(alma_maters["Rolf"])
try:
    print(alma_maters["Anne"])
except KeyError:
    print("KEY ERROR")

alma_maters = defaultdict(list)  # takes in function

for coworker in coworkers:
    if coworker[0] not in alma_maters:
        alma_maters[coworker[0]] = []
    alma_maters[coworker[0]].append(coworker[1])

print(alma_maters["Rolf"])
print(alma_maters["Anne"])


o = OrderedDict()
o["Rolf"] = 6
o["Jose"] = 12
o["Jen"] = 3

print(o)

o.move_to_end("Rolf")
print(o)

o.move_to_end("Jen", last=False)
print(o)

o.popitem()
print(o)


account = ("checking", 1850.90)

print(account[0])
print(account[1])

Account = namedtuple("Account", ["name", "balance"])
account = Account("checking", 1850.90)

print(account.name)
print(account.balance)


friends = deque(("Rolf", "Charlie", "Jen", "Anna"))
friends.append("Jose")
friends.appendleft("Anthony")
print(friends)
friends.pop()
print(friends)
friends.popleft()
print(friends)
