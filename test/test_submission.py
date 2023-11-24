# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 03:09:09 2023

@author: JoelT
"""
for i in range(5):
    print(i)


def testKeyBoardInterrupt():
    raise KeyboardInterrupt("Testing Ctrl + C")


def testSystemExit():
    raise SystemExit("Testing interpreted exit")


def testOtherException():
    raise UserWarning("This is a warning")
