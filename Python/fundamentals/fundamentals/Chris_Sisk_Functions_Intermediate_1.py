'''
#1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1
x[1][0]=15
print(x)

#1.2
students[0]['last_name']='Bryant'
print(students)

#1.3
sports_directory['soccer'][0]='Andres'
print(sports_directory)

#1.4
z[0]['y']=30
print(z)


#2
def iterateDictionary(some_list):
    for x in range(0, len(some_list)):
        name=""
        count=0
        for y in some_list[x]:
            name+=y+" - "+some_list[x][y]
            if(count == 0):
                name+=", "
                count+=1
            else:
                count=0
        print(name)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel


#3
def iterateDictionary2(key_name, Some_list):
    for x in range(0, len(Some_list)):
        print(Some_list[x][key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)
'''

#4
def printInfo(some_dict):
    for x in some_dict:
        print(str(len(some_dict[x]))+" "+str.upper(x))
        for y in range(0, len(some_dict[x])):
            print(some_dict[x][y])
        if (x != list(dojo)[-1]):
            print()


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
# output:
'''
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''