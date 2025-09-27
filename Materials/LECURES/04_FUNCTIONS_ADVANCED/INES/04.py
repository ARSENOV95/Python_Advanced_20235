def rectangle(lenght,width):
    if not isinstance(lenght, int) or not isinstance(width, int):
        return "Enter valid values!"
    
    def area():
        return lenght * width
    
    def parameter():
        return 2*(lenght * width)
    

    return f"Rectangle area: {area(lenght,width)}\nRectangle perimeter: {parameter(lenght,width)}"

