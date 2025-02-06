def unique_el(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


plist = []
while True:
    number = input("Enter the list of numbers(enter 'q' to stop): ")
    if number == 'q': 
        break

    try:
        number = int(number)
        plist.append(number)
        print ("List contains: ", plist)
    except ValueError:
        print ("Enter the list of numbers(enter 'q' to stop): ")

print(unique_el(plist))