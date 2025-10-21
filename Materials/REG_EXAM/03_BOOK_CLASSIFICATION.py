def classify_books(*args,**kwards):
    result = ''

    fiction = []
    non_fiction = []

    for code,book in kwards.items():
        for genre,title in args:
            if book == title:
                if genre == 'fiction':
                    fiction.append((code,book))
                elif genre == 'non_fiction':
                    non_fiction.append((code,book))
            
    
    fiction = sorted(fiction,key = lambda x: x[0])
    #non_fiction = sorted (non_fiction,key = lambda x: -x[0])
    
    if fiction:
        result += 'Fiction Books:\n'
        for code,book in  sorted(fiction,key = lambda x: x[0]):
            result += f'~~~{code}#{book}\n'

    if non_fiction:
        result += 'Non-Fiction Books:\n'
        for code,book in sorted(non_fiction,reverse= True):
            result += f'***{code}#{book}\n'


    return result
 
   





print(classify_books(("fiction", "Brave New World"),("non_fiction", "The Art of War"),NF3421NN="The Art of War",FF1234UU="Brave New World"))
print(classify_books(("non_fiction", "The Art of War"),("fiction", "The Great Gatsby"),("non_fiction", "A Brief History of Time"),("fiction", "Brave New World"),
                     FF1234HH="The Great Gatsby", NF3845UU="A Brief History of Time", NF3421NN="The Art of War", FF1234UU="Brave New World" ))

print(classify_books(("fiction", "Brave New World"),("fiction", "The Catcher in the Rye"),("fiction", "1984"),
                     FICCITRZZ="The Catcher in the Rye",FIC1984XX="1984",FICBNWYYY="Brave New World"))

print(classify_books(("non_fiction", "Sapiens"),("non_fiction", "Homo Deus"),("non_fiction", "The Selfish Gene"),
NF123ABC="Sapiens",
NF987XYZ="Homo Deus",
NF456DEF="The Selfish Gene"
))

