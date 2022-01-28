import math


def solution(w, h):
    scale = w * h
    gcd = math.gcd(w, h)
    w, h = w / gcd, h / gcd
    reduce = gcd * (1 + (w - 1) + (h - 1))
    return scale - reduce
