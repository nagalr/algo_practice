

# return the intersection-values
# of two sets as a List

def test(n1, n2):
    return list(set(n1).intersection(set(n2)))


n1 = []
n2 = []

n1.append(1)
n1.append(2)
n1.append(3)
n1.append(4)

n2.append(3)
n2.append(1)
n2.append(7)
n2.append(8)

print(test(n1, n2))
