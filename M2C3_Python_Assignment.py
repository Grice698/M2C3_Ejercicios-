# Excersise 1:  Create a string, number, list, and boolean, each stored in their own variable

name = 'John'
number = 13
list = [1, 2, 3, 4]

user_age = 13

boolean = True


# Excersise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

first_three_letters = name[:3]

print(first_three_letters)


# Excersise 3: Use an index to grab the first element from your list.

list_first_element = list[0]

print(list_first_element)


# Excersise 4: Create a new number variable that adds 10 to your original number.

new_number = number + 10

print(new_number)


# Excersise 5: Use an index to get the last element in your list.

list_last_element = list[-1]

print(list_last_element)


# Excersise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(',')

print (list_of_names)



# Excersise 7: Get the first word from your string using indexes. 
 
names = 'harry,alex,susie,jared,gail,conner'
first_word = names[0:5]

print(first_word)


# Use the upper function to transform the letters into uppercase.

first_word_uppercase = first_word.upper()

print(first_word_uppercase)


# Create a new string that takes the uppercase word and the rest of the original string

uppercase_plus_original = first_word_uppercase , names 

print(uppercase_plus_original)



# Excersise 8: Use string interpolation to print out a sentence that contains your number variable.

sentence_minor_users = f"""
Hello {name},

We've been informed that you're {number}. Therefore, you are not allowed to enter our website.

""".strip()

print(sentence_minor_users)


# Excersise 9

print('Hello world!')


# Cadena, búsqueda y reemplazo

string = "Hola, saludos a todos"

word_found = string.find("Hola")

print(word_found)

replace_hola = string.replace("Hola", "Adiós")

print(replace_hola)