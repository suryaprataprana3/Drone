def map(x, in_min=0, in_max=1, out_min=1000, out_max=2000):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min