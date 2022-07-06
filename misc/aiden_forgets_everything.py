
def asdf(start, end, step):
    return_value = []
    i = start
    while i <= end:
        return_value.append(i)
        i = i + step
    return return_value
# end asdf

for i in asdf(1, 100, 2):
    print(i)
