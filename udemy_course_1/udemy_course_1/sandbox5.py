def hundred_numbers():
    nums = []
    i = 0
    while i < 100:
        yield i
        # nums.append(i)
        i += 1
    # return nums


g = hundred_numbers()
print(next(g))
print(next(g))
print(next(g))

# print(hundred_numbers())
#
# print([x * 2 for x in hundred_numbers()])

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):  # next(my_object)
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


my_gen = FirstHundredGenerator()
print(my_gen.number)
# noinspection PyTypeChecker
next(my_gen)
# noinspection PyTypeChecker
next(my_gen)
print(my_gen.number)
