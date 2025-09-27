def rectangle(l,w):
    if not (isinstance(l,int) and  isinstance(w,int)):
        return "Enter valid values!"
    
    def area(x :int,y :int):
        return x*y

    def perameter(x:int,y:int):
        return (x+y)*2
    
    return f'Rectangle area: {area(l,w)}\nRectangle perimeter: {perameter(l,w)}' # can return t string with both functions

print(rectangle(2, 10))