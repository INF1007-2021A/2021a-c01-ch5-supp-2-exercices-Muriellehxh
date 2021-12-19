#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from ctypes import alignment


def get_num_letters(text):

    n= 0
    for el in text:
        if el.isalnum() is False:
            text = text.replace(el, "")
        else:
            n+=1

    return n


def get_word_length_histogram(text):

    list_splited = list(t for t in text.split(' '))
    longest_word = max(list_splited, key=len)  # revise!!

    print(text)
    t = text

    list_histogram = []
    for ind in range(0, len(longest_word)):
        ind_value = 0
        for word in list_splited:
            isletter = True
            if word == '':
                isletter = False

            length = 0
            for char in word:

                if char==word and char.isalnum() is False:
                    isletter = False
                elif char == '-':
                    continue
                else:
                    length += 1

            if length == ind and isletter:
                ind_value +=1
        list_histogram.append(ind_value)

    return list_histogram


def format_histogram(histogram):
    ROW_CHAR = "*"
    n = 0

    stars_n_stuff = ''
    for el in histogram:
        if n == 0:
            n += 1
        else:
            n +=1
            stars_n_stuff += f"{histogram.index(el)} {ROW_CHAR*el}" + "\n"

    return stars_n_stuff



def format_horizontal_histogram(histogram):
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"

    return ""


if __name__ == "__main__":
    spam = "a aa-aa \t aa9  "
    print(get_num_letters(spam))
    eggs = get_word_length_histogram(spam)
    print(eggs, "\n")
    print(format_histogram(eggs), "\n")
    print(format_horizontal_histogram(eggs))
