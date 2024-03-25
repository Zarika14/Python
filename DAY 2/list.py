m=[12,45,23,76,89,1,2,3,4,5,6,7,8,9,10]
print(m)
# m.append(7)
# m.remove(10)
m.remove(10)
# m.sort()
print(m)
m.sort(reverse=False)
print(m)
m.reverse()
print(m.index(8))
print(m.count(8)) #counts no.of occurences of element
m.insert(13,50)

l=[120,567,890]
m.extend(l) #all the elements of l will get inserted at the end of m.

k=l+m
print(k)
print(m)


# lst=[i*i for i in range(10)]
# print(lst)

# lst=[i*i for i in range(10) if i%2==0]

# print(lst)
    