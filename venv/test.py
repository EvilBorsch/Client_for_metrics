data="put palm.cpu 10.6 1501864247\nput loh.gpu 10.8 35012164247\nput palm.cpu 10.7 2501864447\nput palm.cpu 10.8 35012164247\n"
items=data.split("\n")
data={}
for item in items[:-1]:
    item=item.split()
    print(item)
    if item[1] not in data:
        data[item[1]]=[]
    data[item[1]].append( (item[2],item[3]) )
#print(data)
#print(items)