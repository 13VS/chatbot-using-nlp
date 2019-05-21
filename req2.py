from pylibgen import Library
l = Library()
ids = l.search('harry')
for id in ids:
    b1=l.lookup(id,fields=["*"])
    for b in b1:
        print(b.__dict__)
