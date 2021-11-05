#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:07:11 2021

@author: Anders
"""


objektet=list()

class svar:
    def __init__(self, spørsmåler, rettsvarr, alternativer):
        self.spørsmåler=spørsmåler
        self.rettsvarr=int(rettsvarr)
        self.alternativer=alternativer
        self.score1=0
        self.score2=0
    def korrekt_svar_tekst(self):
        self.alternativer=self.alternativer.replace("[","")
        self.alternativer=self.alternativer.replace("]","")
        self.alternativer=self.alternativer.split(",")
        print(f"Rett svar er: {self.alternativer[int(self.rettsvarr)]}")
    def svaralternativer(self):
        print(f"{self.spørsmåler}, {self.alternativer}")
    def rettspiller1(self):
        try:
            a=input("Spiller 1 guess: ")
            if int(a)-1==int(self.rettsvarr):
                return True
            else:
                return False
        except:
            print("Spiller 1 skrev et tall som ikke kunne brukest")
            return False
    def rettspiller2(self):
        try:
            b=input("Spiller 2 guess: ")
            if int(b)-1==int(self.rettsvarr):
                return True
            else:
                print("Spiller 2=feil")
                return False
        except:
            print("Spiller 2 skrev et tall som ikke kunne brukest")
            return False
        
def main():  
    score1=0
    score2=0
    with open ("sporsmaalsfil.txt", "r") as m:
        with open ("objekt.txt", "w") as ik:
            for lines in m:
                lines=lines.strip()
                lines=lines.split(":")
                objektet.append(lines[0])
                spørsmåler=lines[0]
                rettsvarr=lines[1]
                alternativer=lines[2]
                lines=svar(spørsmåler, rettsvarr, alternativer)
                lines.svaralternativer()
                a=lines.rettspiller1()
                b=lines.rettspiller2()
                if a==True:
                    print("Spiller1=rett")
                    score1+=1
                else:
                    print("Spiller1=feil")
                if b==True:
                    print("Spiller2=rett")
                    score2+=1
                else:
                    print("Spiller2=feil")
                lines.korrekt_svar_tekst()
                def spørsmål():
                    ik.write("-------------------------\n")
                    for objekter in objektet:
                        ik.write(f"{objekter}\n") 
                spørsmål()
        print(f"Spiller1 score: {score1}")
        print(f"Spiller2 score: {score2}")
            
                
            

if __name__=="__main__":
        main()