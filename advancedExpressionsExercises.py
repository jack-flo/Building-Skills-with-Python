# Wind Chill (using Farenheit)

def calculateWindChill(v, t):
    windChill = 35.74 + 0.6215 * t - 35.75 * \
        (pow(v, 0.16)) + 0.4275 * t * (pow(v, 0.16))
    return windChill


print(calculateWindChill(15, -2))

print(~100)
