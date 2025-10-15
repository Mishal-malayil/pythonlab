
names=["Mishal","Niranjan","Rinshad","Ashwin"]
count=0
for name in names:
    count += name.lower().count('a')

print(f"List of names:{names}")
print(f"Total occurance of 'a': {count}")
