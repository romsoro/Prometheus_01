def computepay(hours, rate):
    # print(f'In computepay, {hours} hours, and {rate} $')

    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + ((hours - 40) * rate * 1.5)
    # print('Returning:', pay)
    return pay


hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

price = computepay(h, r)
print('Pay:', price)
