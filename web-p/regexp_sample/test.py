import re
from regexp import calculate


def findall(regexp):
    text = """
    x=-1a=1c-=bx-=+101x-=yb+=10c-=b-101x=y-100c-=+101a=+1
    """

    return re.findall(regexp, text)


result = calculate({'a': 10, 'b': 20, 'c': 30}, findall)
correct = {"a": -98, "b": 196, "c": -686}
if result == correct:
    print ("Correct")
else:
    print ("Incorrect: %s != %s" % (result, correct))
