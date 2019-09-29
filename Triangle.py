def validInput(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif (c < a+b) or (b < c+a) or (a < b+c):
        return True
    else:
        return False


def classifyTraingle(a,b,c):
    result = 'NotATriangle'
    if validInput(a,b,c):
        result = ''
        if a == b and c == a:
            result += 'Equilateral'
        elif ((a**2)+(b**2)) == (c**2) or ((a**2)+(c**2)) == (b**2) or ((c**2) + (b**2)) == (a**2):
            result += 'Right'
        elif (a != b) and (b!=c) and (c!=a):
            result += 'Isoceles'
        else:
            result += 'Scalene'

    return result



