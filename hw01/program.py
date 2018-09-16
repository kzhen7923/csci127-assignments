def capitalize(name):
    """
    input:name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    """
    return name.title()
    
print(capitalize("harry potter"))

def init(name):
    """
    Input: name --> string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first initial and
    capitalized last name"
    """
    first = name[0:1]
    space_index = name.find(" ")
    last = name[space_index:]
    str = first.title() + "." + last.title()
    return str

print(init("Jane Doe"))


def part_pig_latin(name):
    """
    Input: a string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end
    "ay"
    so: "hello" --> "ellohay"
    """
    str = name[1:] + name[0:1] + "ay"
    return str

print(part_pig_latin("waffle"))


def make_out_word(out, word):
  str = out[0:2] + word + out[2:4]
  return str

print(make_out_word("<<>>","moon"))


def make_tags(tag, word):
  str = "<" + tag + ">" + word + "</" + tag + ">"
  return str

print(make_tags("i","orange"))
      
