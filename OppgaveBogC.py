#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:11:30 2021

@author: -anders-
"""

class Multichoice:
    def __init__(self, question,alt, answer):
        self.question = question
        self.alt = alt
        self.answer = answer
        
    def __str__(self):
        return self.question + str(self.alt)
    
    def check_answer(self):
        the_answer = int(input("Type in what you think is right: "))
        if the_answer == self.answer:
            return 2
        else:
            return 0
        

        
if __name__ == "__main__": 
    question = Multichoice("What is the tallest mountain? \n" ,("1) Mount Everest \n""2) K2 \n""3) Kilimanjaro"), 1)
    question2 = Multichoice("What is the biggest ocean? \n" ,("1) Atlantic Ocean \n""2) Pacific Ocean \n""3) Indian Ocean"), 2)
    
    print(question)
    if question.check_answer() == 2:
        print("Right answer!!!")
    else:
        print("Wrong answer :(")
    print("\n")
    print(question2)
    if question2.check_answer() == 2:
        print("Right answer!!!")
    else:
        print("Wrong answer :(")
        
