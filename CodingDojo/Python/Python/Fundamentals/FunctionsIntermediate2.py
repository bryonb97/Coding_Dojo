x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]


# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(students):
  for person in students:
      print("first_name - {}, last_name - {}".format(person["first_name"], person["last_name"]))

iterateDictionary(students)

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
  for person in some_list:
    print(person[key_name])

iterateDictionary2("first_name", students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
  location_count = 0
  instructor_count = 0
  for locations in dojo["locations"]:
    location_count = len(locations)
  print("{} LOCATIONS".format(location_count))
  print("{}".format(dojo[locations]))

  for instructors in dojo["instructors"]:
    instructor_count = len(locations)
  print("{} INSTRUCTORS".format(instructor_count))
  print("{}".format(dojo[instructors]))    

printInfo(dojo)


def print_info(some_dict):
  for key in some_dict.keys():
    print(f"{len(some_dict[key])} {key.upper()}")
    for item in some_dict[key]:
      print(item)
    # this prints a new line
    print('\n')

print_info(dojo)