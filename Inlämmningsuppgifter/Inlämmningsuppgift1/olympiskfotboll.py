#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# range() creates a large list so it is going to be slow.
# <= >= comparisons should be much faster here. Will try and remember to time them using python3 -m timeit later.
# In [3]: %timeit year < 1950 or year > 2050
# 24.2 ns ± 0.577 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
# In [4]: %timeit for year in range(1950, 2050): True
# 1.29 µs ± 9.23 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# Input is supposed to be a number so make it an integer.
year = int(input("Ange ett år mellan 1950 och 2050: "))
# if the number is less than 1950 or it is greater than 2050: exit.
if year < 1950 or year > 2050:
    print("Du verkar ha svårt att följa instruktioner")
    exit()
elif year == 2020:  # Covid
    print("Olympiska spelen uppskjutna till 2021")
elif (year % 2 == 0) == True and (year % 4 == 0) == False: # If devisable by 2 and not 4.
    # print("DEBUG: " + str(year) + " är jämnt")
    print("Fotbolls-VM")
elif (year % 4 == 0) == True and (year % 2 == 0) == True:  # If devisible by 4 and 2.
    # print("DEBUG: " + str(year) + " är jämnt delbart med 4")
    print("Olympiska spel")
else:
    # print("DEBUG: " + str(year) + " är ojämnt")
    print("Ingenting särskilt detta år")
