"""a, b = 0, 1

while a < 10:
    print (a, end = ' , ')
    a, b = b, a + b


animals = ["cats", "giraffe", "hippopotamus"]

for w in animals:
    print (w, len(w), end = ' , ')


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')"""


for x in range(1, 10):
    if (x % 2 == 0):
        print("it's an even number", x)
        continue
    print("it's an odd number", x)