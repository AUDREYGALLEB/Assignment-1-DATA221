'''
Write a function that converts a given number of seconds since midnight into:
• Hours
• Minutes
• Seconds
• AM or PM
The function should return a formatted string. If the input is invalid, return an appropriate
message.
'''

def timeConversion(seconds_starting_from_midnight):
    try:
        # checks if input is an int
        # try to compare input to 0 to see if it behaves like a number
        # invalid msgs
        if seconds_starting_from_midnight < 0 or seconds_starting_from_midnight >= 86400:
            return "invalid: input must be between 0 and 86399."
        if seconds_starting_from_midnight != int(seconds_starting_from_midnight):
            return "invalid: input must be an integer."
    except:
        return "invalid: input must be an integer."

    seconds_starting_from_midnight = int(seconds_starting_from_midnight)    #ensures int
    hours = seconds_starting_from_midnight // 3600          # calculate hours, minutes, and seconds
    remaining_seconds = seconds_starting_from_midnight % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    if hours < 12:          # finds am/pm
        period = "AM"
    else:
        period = "PM"

    if hours == 0:      # 24hr -> to reg time
        hours = 12
    elif hours > 12:
        hours = hours - 12

    return f"{hours} {minutes} {seconds} {period}"      # return formatted string

print(timeConversion(19067))        # output