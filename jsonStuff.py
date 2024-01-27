# jsonStuff.py
# dH 1/26/24
import json

print("\n\n Welcome to JSON Examples!\n\n")

input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Dennis"
    },
    { "id" : "009",
      "x"  : "7",
      "name" : "Jose"
    }
]'''

info = json.loads(input)

print('User count:', len(info))
print()

for item in info:
    print("Name", item['name'])
    print("Id", item['id'])
    print("x value", item['x'])
    print()
