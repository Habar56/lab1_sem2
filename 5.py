from re import I


school={"1a":200, "2b":300}

def change_st():
    a = input().split()
    school[a[0]] = a[1]

def add_klass():
    a = input().split()
    school[a[0]] = a[1]

def dell_klass():
    a = input()
    del school[a]

def show_klass():
    klasses = []
    members = 0
    for i in school:
        members += int(school[i])
    
    print(members)
    print(school)
    for i in school:
        print(i)

show_klass()
dell_klass()
show_klass()
add_klass()
show_klass()
change_st()
show_klass()