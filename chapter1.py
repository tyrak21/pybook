# import os
# print(os.environ['home'])

# from datetime import datetime
# time_now = datetime.today()
# right_this_minute = time_now.minute
# print(right_this_minute)



# import sys
# print(sys.version)


# from os import getcwd
# where_am_I = getcwd()
# print(where_am_I)


from datetime import datetime
import time
import random
#
# odds = [1,   3,  5,  7,  9, 11, 13, 15, 17, 19,
#         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#         41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
#
# for num in range(5):
#
#     rigth_this_minute = datetime.today().minute
#
#     if rigth_this_minute in odds:
#         print("This minute seems a little odd.")
#     else:
#         print("Not an odd minute")
#     t = random.randint(1, 60)
#     time.sleep( t )

# f = list(range(99,0,-1))
# print(f)



word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()
