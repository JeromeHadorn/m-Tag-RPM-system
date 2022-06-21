MAX_ITERATIONS = 10^6
DEFAULT_SYMBOL = '_'
def underline(input):
    return '{:s}'.format('\u0332'.join(input+' '))[:-1]