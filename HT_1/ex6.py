def exists_value(value, object):
    return (value in object)

print(exists_value(-1,[1, 5, 8, 3]))
print(exists_value(5,(1, 5, 8, 3)))

