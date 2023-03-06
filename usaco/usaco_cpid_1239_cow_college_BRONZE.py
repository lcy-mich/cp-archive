from sys import stdin, stdout
from time import perf_counter
from random import randint

n,maxvalue, charge = int(stdin.readline()),0, 0
tuition = list(map(int, stdin.readline().split()))

start = perf_counter()
for i in tuition:
    agree = sum(map(lambda x: 1 if i <= x else 0, tuition))
    if agree * i == maxvalue*charge:
        if agree > maxvalue:
            maxvalue,charge = agree,i
        continue
    if agree*i >= maxvalue*charge:
        maxvalue,charge = agree,i


stdout.write(f"{maxvalue*charge} {charge} time: {perf_counter()-start}")
