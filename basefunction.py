import random
import string
length = int(input('\n Wie lang soll das Passwort sein?'))
pw_symbols = string.ascii_letters + string.digits + string.punctuation
temp = random.sample(pw_symbols, length)
password = "".join(temp)
print('Ihr generiertes Passwort lautet \n' + password)
