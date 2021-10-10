# from unsorted import numbers // 규칙이 생기는 문제 = 결과가 똑같이 나옴
# def nextint(a, b):
#   cnt = (b - a) + 1
#   num = numbers.pop(0)
#   return a + num % cnt 

from random import randint as nextint
from random import seed as random_seed

random_seed('Hello world')

count = 1000
lang = 'py'

def getChar(upper):
  code = ord('a') + nextint(0, 25)
  if upper: code -= ord('a') - ord('A')
  return chr(code)

def getName():
  name_length = nextint(5, 9)
  name = getChar(True)
  for i in range(name_length):
    name += getChar(False)
  return name


def mk_city_py_dict():
  name = getName()
  x = nextint(1000000, 2000000)
  y = nextint(1000000, 2000000)
  return {
    "name": name, "x": x, "y":y
  }

def mk_city_obj():
  name = getName()
  x = nextint(1000000, 2000000)
  y = nextint(1000000, 2000000)
  return '  City("%s", %d, %d),' % (name, x, y)

for i in range(count):
  city = mk_city_obj()
  print(city)

# py ./mkcity.py > city_data.txt