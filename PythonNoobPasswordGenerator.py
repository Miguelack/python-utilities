import random

lowerCaseInput = "abcdefghijklmnñopqrstuvwxyz"
upperCaseInput= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
integerInput = "0123456789"
specialInput = "!#$%&()*+,-./:;<=>?@[\]_{|}"

typeOfCombination = lowerCaseInput + upperCaseInput + integerInput + specialInput

internalLongPasswordByUser=int(input("how long you want your pass?\n"))

password = "".join(random.sample(typeOfCombination, internalLongPasswordByUser))

print ("Tu contraseña es:", password)
