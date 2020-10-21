#!/usr/bin/python3
WHITE = " "
BLK = "#"
 
 
def get_led(blk: bool):
    return [[BLK if blk else WHITE for n in range(3)] for x in range(5)]
 
 
def num_one():
    led = get_led(False)
    led[0][2] = BLK
    led[1][2] = BLK
    led[2][2] = BLK
    led[3][2] = BLK
    led[4][2] = BLK
    return led
 
 
def num_two():
    led = get_led(True)
    led[1][0] = WHITE
    led[1][1] = WHITE
    led[3][1] = WHITE
    led[3][2] = WHITE
    return led
 
 
def print_three():
    led = get_led(True)
    led[1][0] = WHITE
    led[1][1] = WHITE
    led[3][0] = WHITE
    led[3][1] = WHITE
    return led
 
 
def num_four():
    led = get_led(True)
    led[0][1] = WHITE
    led[1][1] = WHITE
    led[3][0] = WHITE
    led[3][1] = WHITE
    led[4][0] = WHITE
    led[4][1] = WHITE
    return led
 
 
def num_five():
    led = get_led(True)
    led[1][1] = WHITE
    led[1][2] = WHITE
    led[3][0] = WHITE
    led[3][1] = WHITE
    return led
 
 
def num_six():
    led = get_led(True)
    led[1][1] = WHITE
    led[1][2] = WHITE
    led[3][1] = WHITE
    return led
 
 
def num_seven():
    led = get_led(False)
    led[0][0] = BLK
    led[0][1] = BLK
    led[0][2] = BLK
    led[1][2] = BLK
    led[2][2] = BLK
    led[3][2] = BLK
    led[4][2] = BLK
    return led
 
 
def num_eight():
    led = get_led(True)
    led[1][1] = WHITE
    led[3][1] = WHITE
    return led
 
 
def num_nine():
    led = get_led(True)
    led[1][1] = WHITE
    led[3][0] = WHITE
    led[3][1] = WHITE
    return led
 
 
def num_zero():
    led = get_led(True)
    led[1][1] = WHITE
    led[2][1] = WHITE
    led[3][1] = WHITE
    return led
 
 
def num_digital(led):
    for n in led:
        for i in n:
            print(i, end='')
        print('')
 
 
digital = {
    1: num_one,
    2: num_two,
    3: num_three,
    4: num_four,
    5: num_five,
    6: num_six,
    7: num_seven,
    8: num_eight,
    9: num_nine,
    0: num_zero,
}
 
 
def num_led(i: int):
    ss = str(abs(i))
    for s in ss:
        i = int(s)
        if i in digital:
            led = digital.get(i)
            num_digital(led())
            print('')
        else:
            print('Cannot find int ', i)
 
 
Number = input(Enter ur number:) 
print_led(Number)