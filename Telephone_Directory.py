Tellephone_Dictionary = []

def add():
    name = input("Enter the Name: ")
    num = int(input("Enter the Number: "))
    grp = [name,num]
    for i in range(len(Tellephone_Dictionary)):
        if Tellephone_Dictionary[i][0] == grp[0]:
            raise Exception("Record already exist")
        else:
            Tellephone_Dictionary.insert(i,grp)
            return
    Tellephone_Dictionary.append(grp)
    return

def updates():
    old_name = input("Enter the old name: ")
    updated_name = input("Upgraded name is: ")
    new_num = int(input("New Number given: "))
    for i in range(len(Tellephone_Dictionary)):
        if Tellephone_Dictionary[i][0] == old_name:
            Tellephone_Dictionary[i][0] = updated_name
            Tellephone_Dictionary[i][1] = new_num
            Tellephone_Dictionary.sort()
            return
    raise Exception("Record not found")

def searching():
    find = input("Enter name or number on whome you want to search: ")
    option=1 if find.isdigit() else 0
    for i in range(len(Tellephone_Dictionary)):
        if Tellephone_Dictionary[i][option]==find:
            print("Your search: ",find,"is",Tellephone_Dictionary[i][1-option])
            return
    print("Your record does not exist")
    return

def deleting():
    dels = input("Enter name or number that you want to delete: ")
    option=1 if dels.isdigit() else 0
    for i in range(len(Tellephone_Dictionary)):
        if Tellephone_Dictionary[i][option]==dels:
            Tellephone_Dictionary.pop(i)
            Tellephone_Dictionary.sort()
            return
    print("Rocord does not exist")
    return

if __name__ == "__main__":
    while(True):
        print("1.Insert\n2.Delete\n3.Update\n4.Search")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add()
            print(Tellephone_Dictionary)
        elif choice == 2:
            deleting()
            print(Tellephone_Dictionary)
        elif choice == 3:
            updates()
            print(Tellephone_Dictionary)
        elif choice == 4:
            searching()
        else:
            exit()