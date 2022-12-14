WSJoyStick.onKey(KEY.F, function () {
    basic.showString("F")
})
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        MotorDriver.MotorRun(Motor.A, Dir.forward, 10)
        MotorDriver.MotorRun(Motor.B, Dir.forward, 10)
    }
    if (receivedNumber == 2) {
        MotorDriver.MotorRun(Motor.A, Dir.backward, 10)
        MotorDriver.MotorRun(Motor.B, Dir.backward, 10)
    }
    if (receivedNumber == 3) {
        MotorDriver.MotorRun(Motor.A, Dir.forward, 10)
        MotorDriver.MotorRun(Motor.B, Dir.backward, 10)
    }
    if (receivedNumber == 4) {
        MotorDriver.MotorRun(Motor.A, Dir.backward, 10)
        MotorDriver.MotorRun(Motor.B, Dir.forward, 10)
    }
})
WSJoyStick.onKey(KEY.A, function () {
    basic.showString("A")
})
WSJoyStick.onKey(KEY.P, function () {
    basic.showString("P")
})
WSJoyStick.onKey(KEY.E, function () {
    basic.showString("E")
})
WSJoyStick.onKey(KEY.D, function () {
    basic.showString("D")
})
WSJoyStick.onKey(KEY.B, function () {
    basic.showString("B")
})
WSJoyStick.onKey(KEY.C, function () {
    basic.showString("C")
})
radio.setGroup(1)
WSJoyStick.JoyStickInit()
basic.forever(function () {
    if (WSJoyStick.Listen_Dir(DIR.NONE)) {
        basic.clearScreen()
        MotorDriver.MotorStop(Motor.A)
        MotorDriver.MotorStop(Motor.B)
    } else {
        if (WSJoyStick.Listen_Dir(DIR.U)) {
            basic.showArrow(ArrowNames.North)
            radio.sendNumber(1)
        }
        if (WSJoyStick.Listen_Dir(DIR.D)) {
            basic.showArrow(ArrowNames.South)
            radio.sendNumber(2)
        }
        if (WSJoyStick.Listen_Dir(DIR.L)) {
            basic.showArrow(ArrowNames.West)
            radio.sendNumber(3)
        }
        if (WSJoyStick.Listen_Dir(DIR.R)) {
            basic.showArrow(ArrowNames.East)
            radio.sendNumber(4)
        }
    }
})
