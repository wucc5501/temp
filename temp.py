n=input()
a=n.split(' ')
a.sort()
dict1 = {}
for i in a:
      if i not in dict1.keys():
             dict1[i] = a.count(i)
for k in dict1.keys():
      if dict1[k]==max(dict1.values()):
            print(k)