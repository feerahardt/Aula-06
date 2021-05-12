def letra(nota):
    if nota >= 9:
        return 'A'
    elif nota >= 8:
        return 'B'
    elif nota >= 7:
        return 'C'
    elif nota >= 6:
        return 'D'
    else:
        return 'F'


print(letra(8))
