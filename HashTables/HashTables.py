import pandas as pd

# Using curly braces
student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# Using the dict() function
employee_ages = dict(John=28, Sarah=33, Mike=40)

departments = {
    'Sales': {'John': 70000, 'Alice': 68000},
    'IT': {'Sarah': 75000, 'Charlie': 72000}
}

# Accessing a value
print(student_grades['Alice'])  # Output: 85

# Accessing items in a nested dictionary
print(departments['IT']['Sarah'])  # Output: 75000

# Updating a single value
student_grades['Alice'] = 88

# Updating values in a nested dictionary
departments['Sales']['John'] = 71000

# Removing an item from a dictionary
del student_grades['Charlie']

# Removing an item from a nested dictionary
del departments['IT']['Charlie']

# Dictionary data
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Grade': [85, 90, 78]}

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)


