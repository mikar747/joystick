WSJoyStick.onKey(KEY.F, function () {
    basic.showString("F")
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
WSJoyStick.JoyStickInit()
basic.forever(function () {
    if (WSJoyStick.Listen_Dir(DIR.U)) {
        basic.showArrow(ArrowNames.North)
    }
    if (WSJoyStick.Listen_Dir(DIR.D)) {
        basic.showArrow(ArrowNames.South)
    }
    if (WSJoyStick.Listen_Dir(DIR.L)) {
        basic.showArrow(ArrowNames.West)
    }
    if (WSJoyStick.Listen_Dir(DIR.R)) {
        basic.showArrow(ArrowNames.East)
    }
})
