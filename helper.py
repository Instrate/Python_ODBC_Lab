def datetimeToStr(date):
    res = ""
    res += str(date.year) + "-"
    if (date.month < 10):
        res += "0"
    res += str(date.month) + "-"
    if (date.day < 10):
        res += "0"
    res += str(date.day)
    return res

def typeToFormat(type):
    if(type.find("char") != -1):
        return "поле"
    elif(type.find("date") != -1):
        return "YYYY-MM-DD"
    elif(type.find("enum") != -1):
        return "номінальне"
    else:
        return "число"