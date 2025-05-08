# Let Y be the year for which the date of Easter is desired

# Algorithm E
def algoE(year):
    # Golden number
    g = (year % 19) + 1
    # Century
    c = (year//100) + 1
    # Corrections, where x is the number of years in which leap year was dropped, z syncs Easter with the moon's orbit
    x = ((3*c)//4) - 12
    z = ((8*c+5)//25)-5
    # Find sunday
    d = ((5*year)//4) - x - 10
    # Epact
    e = (11*g+20+z-x) % 30
    if e == 25 and g > 11:
        e += 1
    elif e == 24:
        e += 1
    # Find full moon
    n = 44 - e
    if n < 21:
        n += 30
    # Advance to sunday
    n = n + 7 - ((d+n) % 7)
    # get month
    if n > 31:
        date = n - 31
        return f"{date} April"
    else:
        return f"{n} March"


print(algoE(2025))
