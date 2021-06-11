
def to_hex(num):
    letters = "abcdef"
    secondDigit = 0
    if num <= 9:
        return str(num)
    elif num <= 16:
        return letters[num - 10]
    else:
        firstDigit = num // 16
        if firstDigit > 9:
            firstDigit = letters[firstDigit-10]

        if num % 16 > 9:
            secondDigit = letters[num%16 - 10]
        return str(firstDigit) + str(secondDigit)
        


def hex_code(red, green, blue):
    red,blue,green = str(to_hex(red)), str(to_hex(blue)), str(to_hex(green))
    try:
        red[1]
    except IndexError:
        red = "0" + red

    try:
        blue[1]
    except IndexError:
        blue = "0" + blue

    try:
        green[1]
    except IndexError:
        green = "0" + green


    return "#"+red+green+blue
        
print(hex_code(10,32,255))

    
