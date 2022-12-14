def my_function():
    basic.show_string("F")
WSJoyStick.on_key(KEY.F, my_function)

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        MotorDriver.motor_run(Motor.A, Dir.FORWARD, 10)
        MotorDriver.motor_run(Motor.B, Dir.FORWARD, 10)
    if receivedNumber == 2:
        MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 10)
        MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 10)
    if receivedNumber == 3:
        MotorDriver.motor_run(Motor.A, Dir.FORWARD, 10)
        MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 10)
    if receivedNumber == 4:
        MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 10)
        MotorDriver.motor_run(Motor.B, Dir.FORWARD, 10)
radio.on_received_number(on_received_number)

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
radio.set_group(1)

def on_forever():
    if WSJoyStick.Listen_Dir(DIR.NONE):
        basic.clear_screen()
        MotorDriver.motor_stop(Motor.A)
        MotorDriver.motor_stop(Motor.B)
    else:
        if WSJoyStick.Listen_Dir(DIR.U):
            basic.show_arrow(ArrowNames.NORTH)
            radio.send_number(1)
        if WSJoyStick.Listen_Dir(DIR.D):
            basic.show_arrow(ArrowNames.SOUTH)
            radio.send_number(2)
        if WSJoyStick.Listen_Dir(DIR.L):
            basic.show_arrow(ArrowNames.WEST)
            radio.send_number(3)
        if WSJoyStick.Listen_Dir(DIR.R):
            basic.show_arrow(ArrowNames.EAST)
            radio.send_number(4)
basic.forever(on_forever)
