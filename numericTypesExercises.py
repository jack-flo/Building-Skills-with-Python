# Celcius to Farenheit


def celciusToFarenheit(x):
    farenheit = (x-32) * 100/(212-32)
    print(round(farenheit, 2), "C")


celciusToFarenheit(18)


# Loan Repayment
def mortgagePayment(principle, r, n):
    numberOfPayments = n * 12
    interestRate = (r / 100) / 12
    payment = principle * \
        (interestRate / (1 - (1 + interestRate)**-numberOfPayments))
    return round(payment, 2)


print("$", mortgagePayment(110000, 7.25, 30))


# Surface AIr Consumption Rate
def findSACR(depth, startPres, endPres, time):
    SACR = ((33 * (startPres - endPres)) / (time * (depth + 33)))
    return round(SACR, 1)


print("Shallow Dive: ", findSACR(30, 3000, 1500, 60))
print("Medium Dive: ", findSACR(60, 3000, 500, 60))
print("Deep Dive: ", findSACR(100, 3000, 500, 15))


# Force on a Sail
def sailForce(area, windSpeed):
    force = (windSpeed**2) * 0.004 * area
    return force


print("Sail Force: ", sailForce(61, 15))
