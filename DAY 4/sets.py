# SETS ARE UNCHANGEABLE,WE CAN NOT REPLACE ANY ELEMENT OF A SET WITH THE NEW ELEMENT.
# NO NEED TO MAINTAIN AND WORRY ABOUT ORDER.
# s={2,4,6,7,9,0,1,8,"anku",True,False,"cricket"}
# print(s)
# for i in s:
#     print(i)
    
# s1={2,3,4,5,7,9,1} 
# s2={4,8,7,0} 
# # adding two sets.
# print(s1.union(s2))
# print(s1.intersection(s2)) 

states1={"Punjab","Haryana","Goa","Bihar","Assam"}
states2={"HP","UK","UP","MP","AP","Goa","Punjab"}
statesN={"JK","TN","WB"}
statesM={"HP","UK","AP"}



states3=states1.union(states2)
print(states3)

states4=states1.intersection(states2)
print(states4)

states5=states1.symmetric_difference(states2)
print(states5)

states5.add("Rajasthan")
print(states5)

states5.discard("Rajasthan")
print(states5)
    #    OR
    
# states5.remove("Rajasthan")
# print(states5)    


print(states1.isdisjoint(states2))
print(states2.isdisjoint(statesN))
print(states1.issuperset(states2))
print(states1.issubset(states2))
print(states2.issuperset(statesM))
print(statesM.issubset(states2))

statesM.pop()
print(statesM)
# s1.update(s2)
# print(s1)


# how to create empty set.
# harry=set()
# print(type(harry))