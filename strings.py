
my_string = "Mi string"
my_other_string = "Mi otro String"

#print(len(my_string))
#print(len(my_other_string))
#print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string)

#Formato
name, lastname, age = "Hector", "Sanchez", 32
# %s es variable tipo string %d es variable tipo int
#no se puede concatenar a enteros solo cadenas
print("Mi nombre es {}{} y mi edad es {}".format(name, lastname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, lastname, age))
print("Mi nombre es "+ name +"" + lastname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")


#desempaqueado de caracteres
language = "python"

a, b, c, d, e, f = languaje
#print(b)
#print(e)
#print(b,e)

#Division
#-2 cuenta hacia atras

language_slice = language[1:3]
print(language_slice)

languaje_slice = language[0:5]
print(language_slice)

language_slice = languaje[-2]  
print(languaje_slice)


languaje_slice = language_slice [0:2:2]
print(language_slice)



#reverse 
reversed_language = language[::-1]
print(reversed_language)

print(language.capitalize()) #empieza con mayuscula
print(language.upper()) #Todas con minusculas
print(language.count("t")) 
print(language.isnumeric)
print("1".isnumeric())
print(language.lower()) #minuscula
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py") #No es lo mismo