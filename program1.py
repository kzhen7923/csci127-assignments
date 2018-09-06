def hello_name(name):
  return "Hello " + name + "!"


def make_abba(a, b):
  return a + b + b +a

def make_tags(tag, word):
  return "<"+tag+">" + word +"</"+tag+">"

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  if a_smile and  b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  else: 
    return False


def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  else:
    return a + b

def makes10(a, b):
  if a==10 or b==10:
    return True
  if a + b == 10:
    return True
  else:
    return False

def combo_string(a, b):
  if len(a) > len (b):
    return b+ a + b
  if len(a) < len (b):
    return a + b + a
