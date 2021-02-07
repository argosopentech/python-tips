from collections import defaultdict

# Defaults to empty list
list_dict = defaultdict(list)
list_dict['key'].append('Hello')
list_dict['key'].append('World')
print(list_dict) # {'key': ['Hello', 'World']}

# Setting your own default with lambda functions
lambda_dict = defaultdict(lambda: 'Hello ')
lambda_dict['key1'] += 'World'
lambda_dict['key2'] += 'Moon'
lambda_dict['key1'] += '!'
lambda_dict['key2'] += '!'
print(lambda_dict) # {'key1': 'Hello World!', 'key2': 'Hello Moon!'}

