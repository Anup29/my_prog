"""
For Henry Davids, the output should be:

Mr. Henry Davids

For Mary George, the output should be:

Ms. Mary George

Input Format: The first line contains the integer N, the number of people. N lines follow each containing the space separated values of the first name, last name, age, and sex, respectively.

Constraints: 1 ≤ N ≤ 10

Output Format: Output N names on separate lines in the format described above in ascending order of age.

Sample Input

3

Mike Thomson 20 M

Robert Bustle 32 M

Andria Bustle 30 F

Sample Output

Mr. Mike Thomson

Ms. Andria Bustle

Mr. Robert Bustle
"""
def name_decorator(format_func):
    def wrapper(person):
        first_name = person['first_name']
        last_name = person['last_name']
        sex = person['sex']
        if sex == 'M':
            title = 'Mr.'
        else:
            title = 'Ms.'
        return f"{title} {format_func(first_name, last_name)}"
    return wrapper

@name_decorator
def format_name(first_name, last_name):
    return f"{first_name} {last_name}"

def format_names_by_age(n, people):
    # Parse input and store details in a list of dictionaries
    people_list = []
    for person in people:
        first_name, last_name, age, sex = person.split()
        age = int(age)
        people_list.append({'first_name': first_name, 'last_name': last_name, 'age': age, 'sex': sex})

    # Sort the list by age
    people_list.sort(key=lambda x: x['age'])

    # Format the names and print them
    for person in people_list:
        print(format_name(person))

# Read input
# N = int(input().strip())
# people = [input().strip() for _ in range(N)]
people = ["Mike Thomson 20 M", "Robert Bustle 32 M", "Andria Bustle 30 F"]
N = len(people)

# Format and print names
format_names_by_age(N, people)
