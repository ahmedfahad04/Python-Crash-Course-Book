num = {'ziddan':'10','shuvro':'333','bafil':'7','arafath':'11','sharif':'20'}

# loop using only keys
for item in num.keys():
    print(item.title())

# loop using only values
for item in num.values():
    print(item)

# loop using both keys and values
for key, value in num.items():
    print("\nKeys: "+key.title()+"("+value+")")
    


