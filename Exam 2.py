#   Filename:           Exam 2
#   Created by:         jasongreen
#   Date:               Saturday, February 02, 2019
#   Time of Creation:   14:09
#   ---

# import math
# days = int(input("How many days? "))
# months = days / 30
# days = days % 30
#
# if months < 1:
#     months = math.floor(months)
#     print("There are {} days left!".format(days))
# elif months == 1:
#     print("There's only one month left! 30 days to be exact!")
# else:
#     months = math.floor(months)
#     print("There are {} months and {} days remaining!".format(months, days))

flat_rate = 15
rate_over_1000 = 0.0175
rate_over_2000 = 0.02
rate_over_3000 = 70
total_charge = 0

cubic_feet = int(input("How many cubic feet of H20 have you used? "))

if cubic_feet <= 1000:
    total_charge = flat_rate
    print("Your bill comes out to ${}.".format(total_charge))
elif 1000 < cubic_feet <= 2000:
    total_charge = flat_rate + ((cubic_feet - 1000) * rate_over_1000)
    print("Your bill comes out to ${}.".format(total_charge))
elif 2000 < cubic_feet <= 3000:
    total_charge = flat_rate + (1000 * rate_over_1000) +\
                   ((cubic_feet - 2000) * rate_over_2000)
    print("Your bill comes out to ${}.".format(total_charge))
elif cubic_feet > 3000:
    total_charge = flat_rate + (1000 * rate_over_1000) + \
                   (1000 * rate_over_2000) + rate_over_3000
    print("Your bill comes out to ${}.".format(total_charge))


