items={}

def addItems(key,value):
    global items
    items[key]=value
    return items,True

def removeItems(key):
    global items
    value=items.pop(key,None)
    return items

def totalItems():
    global items
    for x in items:
        #count+=1
        return x




