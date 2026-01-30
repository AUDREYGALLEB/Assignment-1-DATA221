'''
Write a function that takes the radii of two circles and performs the following:
• Validates that both radii are positive integers.
• Computes the area of each circle.
• Returns the percentage of the larger circle’s area that can be covered by the smaller circle.
If invalid input is provided, return a meaningful message instead of performing the calculation.
'''

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    try:            # trying to compare values (this will fail if input is not a number)
        if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:                # checking if both radii are positive whole numbers
            return "invalid: both radii must be positive integers."
        if radiusOfCircle1 != int(radiusOfCircle1) or radiusOfCircle2 != int(radiusOfCircle2):
            return "invalid: both radii must be integers."
    except:
        return "invalid: both radii must be integers."

    pi = 3.14159

# area of each circle
    areaOfCircle1 = pi * radiusOfCircle1 * radiusOfCircle1
    areaOfCircle2 = pi * radiusOfCircle2 * radiusOfCircle2

    if areaOfCircle1 < areaOfCircle2:       #finding small circle and large circle
        smaller_area = areaOfCircle1
        larger_area = areaOfCircle2
    else:
        smaller_area = areaOfCircle2
        larger_area = areaOfCircle1

    # percentage of larger circle that can be covered by the smaller circle
    percentage_of_larger_circle_coverage = (smaller_area / larger_area) * 100

    return percentage_of_larger_circle_coverage

print(circleAreaCoverage(3,2))      # this is only an example output