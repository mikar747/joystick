def my_function():
    basic.show_string("F")
WSJoyStick.on_key(KEY.F, my_function)

def my_function2():
    basic.show_string("A")
WSJoyStick.on_key(KEY.A, my_function2)

def my_function3():
    basic.show_string("P")
WSJoyStick.on_key(KEY.P, my_function3)

def my_function4():
    basic.show_string("E")
WSJoyStick.on_key(KEY.E, my_function4)

def my_function5():
    basic.show_string("D")
WSJoyStick.on_key(KEY.D, my_function5)

def my_function6():
    basic.show_string("B")
WSJoyStick.on_key(KEY.B, my_function6)

def my_function7():
    basic.show_string("C")
WSJoyStick.on_key(KEY.C, my_function7)

WSJoyStick.joy_stick_init()

def on_forever():
    if WSJoyStick.Listen_Dir(DIR.U):
        basic.show_arrow(ArrowNames.NORTH)
    if WSJoyStick.Listen_Dir(DIR.D):
        basic.show_arrow(ArrowNames.SOUTH)
    if WSJoyStick.Listen_Dir(DIR.L):
        basic.show_arrow(ArrowNames.WEST)
    if WSJoyStick.Listen_Dir(DIR.R):
        basic.show_arrow(ArrowNames.EAST)
basic.forever(on_forever)
