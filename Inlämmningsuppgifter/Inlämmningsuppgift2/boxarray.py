#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Jonas Pettersson <5558916-fuzebox@users.noreply.gitlab.com>
# @Date: 2021-01-14 20:05:24
# @Last Modified by: Jonas Pettersson <5558916-fuzebox@users.noreply.gitlab.com>
# @Last Modified time: 2021-01-14 20:35:10


lista = [x for x in range(0,100)]
i = 0
while i < 100:
    print("{:^2}".format(lista[i]), end=" ")
    i=i+1
    if i % 10 == 0:
        print("")


# [print(f"{x:<2}", end=" ") if x else print() for x in range(0,100,10)]
# [print(f"{x:<2}", end="") for x in range(9,100,10) if x in range(0,100,1)]
# Äh ger upp på den så länge.
