timetable = {'mon':[],'tue':[],'wed':[],'thurs':[],'fri':[]}

def init():
    for i in range(len([9,10,11,12])):
        for j in timetable.keys():
            timetable[j].append(None)

def insert(day,course,slot):
    if timetable[day][slot-9] == None:
        timetable[day][slot-9] = course
        return course

def remove(day,slot):
    timetable[day][slot-9] = None

def replace(day, slot, course):
    timetable[day][slot-9] = course

def display():
    print(timetable)
    print()

init()
display()
insert('mon','DSA',11)
insert('tue','LD',9)
insert('wed','DM',12)
insert('fri','EM3',10)
insert('thurs','ISE',9)
display()
remove('wed',12)
display()
replace('thurs',9,'DSA')
replace('mon',11,'ISE')
display()