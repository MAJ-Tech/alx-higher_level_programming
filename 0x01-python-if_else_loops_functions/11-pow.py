#!/usr/bin/python3


def pow(a, b):
     res = 1
     if b < 0:
          a = 1/a
          b = -b
     while b > 0:
          if b % 2 == 1:
               res *= a
          a *= a
          b //= 2
     return res

                    
