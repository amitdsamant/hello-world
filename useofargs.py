

def simple_function(arg1, *args):
    print('first arg:', arg1)
    for arg in args:
        print('another argument', arg)


if __name__ == '__main__':
    simple_function('amit','pradnya','amol','arg3')
