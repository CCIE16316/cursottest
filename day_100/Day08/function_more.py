def greet(name,sport,wife): # ()里面的叫parameter，其实就是占位符。也叫形参。
    print(f"Hello {name}!")
    print(f"I think you like to play {sport}!")
    print(f"Your wife is {wife}.") 
    # Formatted String Literals = f-String


greet("jinkin","football","Aries")
# ()里面的叫argument，这里就是实际值。
# 这里的实参会传递给占位符（形参）

# 其实就是实际的参数传递给了占位符，可以理解成占位符就是一个局部变量，函数里面就可以调用这个变量的值。