#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:35:40 2017

@author: Ian
"""
annual_salary=float(input("Enter the starting salary:  "))
semi_annual_raise=0.07
r=0.04
total_cost=1000000
down_payment=total_cost*0.25
def getMoneyInThreeYears(saving_rate):
     portion_saved =saving_rate/10000
     months_salary=annual_salary/12
     current_savings=0
     months=0
     while months<=36:
         current_savings=current_savings+(current_savings*r/12)
         current_savings=current_savings+(months_salary*portion_saved)
         months=months+1
         if months%6==0:
             months_salary=months_salary*(1+semi_annual_raise)
     return current_savings
 
high=10000
low=0
flag=True
if getMoneyInThreeYears(high)<down_payment:
    print("It is not possible to pay the down payment in three years.")
    flag=False
best_rate=(high+low)/2
steps=0
while flag:
    steps=steps+1
    current_rate=best_rate
    if abs(down_payment- getMoneyInThreeYears(current_rate))<=100:
        break
    elif down_payment- getMoneyInThreeYears(current_rate)>0:
        low=current_rate
    else :
        high=current_rate
        
        
    best_rate=(high+low)/2
if flag:
    print("Best savings rate:  ",best_rate/10000)
    print("Steps in bisection search:  ",steps)