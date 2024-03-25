
# READING TO A FILE

# f=open('my.txt','r')
# # print(f)
# # 'r' mode is default in this

# text=f.read()
# print(text)
# f.close()


# f=open('my.txt','rb') # 'rb' reads the file as a binary file
# text=f.read()
# print(text)
# f.close()


# f=open('my.txt','rt') # 'rt' reads the file as txt file
# text=f.read()
# print(text)
# f.close()

# WRITING TO A FILE
# s=open('my.txt2','w')
# text=s.write("hello Prashant")
# # print(text)
# s.close()
# # the obove function will make a txt file when w mode is used

# # APPENDING IN A FILE

# s=open('my.txt','a')
# text=s.write(" hello Prashant ")
# # print(text)
# s.close()

# f = open('my.txt', 'r')
# while True:
#   line = f.readline()
#   if not line:
#     break
#   print(line)
  
f = open('my.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1}")
  print(f"Marks of student {i} in English is: {m2}")
  print(f"Marks of student {i} in SST is: {m3}")

  print("\n")



# f = open('my.txt2', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()  
