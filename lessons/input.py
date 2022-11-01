

def tostring(x:str) -> float:
    new_s = x.strip("$")
    print(new_s)
    new_f = float(new_s)
    print(new_f)

    new_f = (float(x.strip("$")))
    return new_f

string1: str = "$6.38532"
print("float:", tostring(string1))