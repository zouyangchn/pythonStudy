l = ['A', 'B', 'C', 'D', 'E']
print([l[0], l[1], l[2]])

r = []
n = 3
for i in range(n):
    r.append(l[i])
print(r)
print(l)
print(l[2:4])
print(l[:3])
print(l[-1])
print(l[-1:])
print(l[-2:-1])
print(l[-2:])
print(l[:-1])

m = list(range(100))
print(m)
print(m[:10])
print(m[10:20])
print(m[-10:])
print(m[-10:-5])
print(m[:10:2])
print(m[1:100:2])
print(m[:100:5])
print(m[3:100:3])
print(m[::])

n = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(n[:3])

a = 'abcdefghijkl'
print(a[:18:2])


def trim(vstr):
    if (len(vstr) == 0 or (vstr[0] != ' ' and vstr[-1] != ' ')):
        return vstr
    else:
        return trim(vstr[0] == ' ' and vstr[1:] or vstr[:-1])


print(trim('    helll   '))

print('' or 'gty')
