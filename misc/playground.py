seq = ["foo", 4, "bar", 9, "baz", 0, "que", 9]

print(seq[::2])

def words(s):
    print('Starting...')
    for word in s.split():
        yield word

for word in words('hello world'):
    print(word)

print(int(6.9))

var = {"a": 1, "b": 2, "c": 3}
print(var.popitem())

tasks = {
    'Mon': 'Go to work',
    'Tue': 'Go to work',
    'Wed': 'Go to work',
    'Thu': 'Go to work',
    'Fri': 'Go to work',
    'Sat': 'Go to work',
    'Sun': 'Go to work',
}

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

sorted(days)

for day in days:
    tasks[day]= 'Go to work'

print(int(float('6.9')))

if 8 > 4 & 8 != None:
    print("true")
else:
    print("false")