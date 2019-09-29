def valid_input(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif (c > (a + b)) or (b > (c + a)) or (a > (b + c)):
        return False
    else:
        return True


def classify_triangle(a, b, c):
    result = 'NotATriangle'
    if valid_input(a, b, c):
        result = ''
        if a == b and c == a:
            result = result + 'Equilateral'
        elif ((a**2)+(b**2)) == (c**2) or ((a**2)+(c**2)) == (b**2) or ((c**2) + (b**2)) == (a**2):
            result = result + 'Right'
        elif (a != b) and (b != c) and (c != a):
            result = result + 'Isoceles'
        else:
            result = result + 'Scalene'

    return result



