list1=list(map(int,input("Enter the first list fo integers:").split()))
list2=list(map(int,input("Enter the second list fo integers:").split()))

if len(list1)==len(list2):
    print("Both are the same length.")
else:
    print("The List are different length.")

if sum(list1)==sum(list2):
    print("Both list have same sum.")
else:
    print("Both list don't have same sum.")

commonvalues= set(list1) & set(list2)

if commonvalues:
    print(f"Common value founded: {commonvalues}")
else:
    print(f"No common value founded.")
