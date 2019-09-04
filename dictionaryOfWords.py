
# Create a dictionary with key value pairs to represent words (key) and its definition (value)

word_definitions = dict()

word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Cool"] = "A descriptor word for a cucumber"
word_definitions["Chill"] = "The act of sinking into the couch and watching Netflix"


# Use square bracket lookup to get the definition of two words and output them to the console with `print()`

print(word_definitions["Cool"])
print(word_definitions["Chill"])

for (key, value) in word_definitions.items():
    print(f"The definition of {key} is {value}")


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""