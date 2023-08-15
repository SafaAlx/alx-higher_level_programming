#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, i learnt C!"
length, first = multiple_returns(sentence)
print("lenth: {:d} - First character: {}".format(length, first))
