def get_sound_level(number):
    if number < 10:
        print('I can\'t hear you')
    elif number < 20:
        print('You\'re still dang quiet')
    elif number <50:
        print('Not bad')
    elif number < 60:
        print('I can hear you perfectly')
    elif number <70:
        print('Getting uncomfortable')
    else:
        print('Too loud!!!')
    return str(number) + (' db')

print(get_sound_level(55))
print(get_sound_level(30))

def helper_hi():
    print('Glad to see ya \'round here')
    print('How art thou?')

def hi(name):
    print('Hello ' + name)
    helper_hi()

hi('Victoria')
