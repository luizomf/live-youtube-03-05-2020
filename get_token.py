token = 'Bearer '

with open('token.txt', 'r') as file:
    token += file.read()
