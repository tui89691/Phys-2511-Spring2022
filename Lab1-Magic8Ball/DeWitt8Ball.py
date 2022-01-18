# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random as ra
import time as tm

y=["Indubitably","Absolutely","Perhaps","Eh, the outlook isn't great","Less likely things have happened", "No","That's a hard pass"]
x=input("Ask me your question, but be patient. Good things come to those who wait. Enter your question: ")
print("I see... Give me a moment.")
tm.sleep(3)
print("So you come before me, asking: ",x)
tm.sleep(2)
print("Very well.")
tm.sleep(2)
print("Yes, your fortune is clear now. The answer is...")
tm. sleep (3)
print(ra.choice(y))
