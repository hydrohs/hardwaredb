GIGABYTE = 1024 #1024MB in 1GB
TERABYTE = GIGABYTE**2
GHZ_THRESHOLD = 1000

def get_size(size):
    if size >= TERABYTE:
        return f'{int(size / TERABYTE)}TB'
    elif size >= GIGABYTE:
        return f'{int(size / GIGABYTE)}GB'
    else:
        return f'{size}MB'
    
def get_frequency(speed):
    if speed >= GHZ_THRESHOLD:
        return f'{speed / GHZ_THRESHOLD}GHz'
    else:
        return f'{speed}MHz'
    
def get_ramspeed(speed, type):
    if type in ('FPM', 'EDO'):
        return f'{speed}ns'
    else:
        return f'{speed}MHz'