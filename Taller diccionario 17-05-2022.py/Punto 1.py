l=[12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64,23]
d={}
for i in l:
    a=l.count(i)
    d.update({i:a})
print(d)