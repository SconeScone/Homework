def dots(r, x0, y0):  #
    count = 0
    for x in range(-r - y0, r + y0 + 1):
        for y in range(-r - x0, r + x0 + 1):
            if (((x - x0)**2) + (y - y0)**2) <= r**2:
                count += 1
    return count
