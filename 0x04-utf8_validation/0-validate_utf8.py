#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Method that determines if a given data set 
    represents a valid UTF-8 encoding"""
    remainder = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if remainder == 0:
            while mask & byte:
                remainder += 1
                mask = mask >> 1
            if remainder == 0:
                continue
            if remainder == 1 or remainder > 4:
                return False
        else:
            if not (byte & mask_1 and not (byte & mask_2)):
                return False
        remainder -= 1
    if remainder == 0:
        return True
    return False
