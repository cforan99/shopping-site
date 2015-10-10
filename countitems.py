ids = [3, 6, 9, 6, 12, 3, 15, 6, 18, 18, 18, 18]
dir(ids)
# OUT: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
help(ids)
ids.count(6)
# OUT: 3
ids.sort()
ids
# OUT: [3, 3, 6, 6, 6, 9, 12, 15, 18, 18, 18, 18]
for id in ids
# OUT:   File "<input>", line 1
# OUT:     for id in ids
# OUT:                 ^
# OUT: SyntaxError: invalid syntax
for id in ids:
    



pass
# OUT:   File "<input>", line 7
# OUT:     pass
# OUT:        ^
# OUT: IndentationError: expected an indented block
cart = {}
for id in ids:
    if id not in cart:
        cart[id] = ids.count(id)
    else:
        contine
        
    

# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 5, in <module>
# OUT: NameError: name 'contine' is not defined
for id in ids:
    if id not in cart:
        cart[id] = ids.count(id)
    else:
        continue
        
    


cart
# OUT: {3: 2, 6: 3, 9: 1, 12: 1, 15: 1, 18: 4}
cart = {}
cart
# OUT: {}
for id in ids:
    if id not in cart:
        cart[id] = {'count': ids.count(id)}
    else:
        continue
        
    


cart
# OUT: {3: {'count': 2}, 6: {'count': 3}, 9: {'count': 1}, 12: {'count': 1}, 15: {'count': 1}, 18: {'count': 4}}
