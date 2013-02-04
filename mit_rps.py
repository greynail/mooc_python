#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:28:28 2013
modified 4th Fib 2012 to help use Git and gitHub
rock paper scissors 
@author: graham naylor;
For use in linux console. Enter rock paper or scissors (or their initial!).. use:  ./mit_rps.py
"""
import os # to allow to clear the console (see rps_player_one()). Works on Linux 
PLAYER1_WIN = [[1,3],[2,1],[3,2]]# rock =1, paper = 2, scissor = 3
PLAYER2_WIN = [[1,2],[2,3],[3,1]]# should be tuples to avoid mutation, but,,,



def rps_player_one():
    os.system('clear')# the 'clear' is linux orientated , i think its 'cls' for windows.
    x = raw_input("\nPlayer 1! rock paper or scissors: ")
    rps_entry_check(x)
    x = x.lower()
    x = x[0]
    decode_list = [x,]#create list with first element being player ones entry
    rps_player_two(decode_list)#send the list to player two, for their answer to become second element

def rps_player_two(decode_list):
    x = raw_input("Player 2!; rock, paper, or scissors: ")
    rps_entry_check(x)
    x = x.lower()
    x = x[0]
    decode_list += x #finalise the list entries
    rps_response_repository(decode_list)#send the final list to have elements converted into coresonding numbers

def rps_response_repository(decode_list):
    data = [rps_response_decode(item) for item in decode_list]# create a list, 'data', of integers from the function argument
    rps_decision(data)
    
def rps_decision(data):
    reciprocal = reduce(rps_reciprocalof_listelements, data)#if reciprocal of 1 returned, list elements are equal..
    if (reciprocal == 1):                                   #reduce takes each of the elements in 'data' and sends them
        rps_players_tie()                                   #to rps_reciprocalof_listelements
    else:
        for item in PLAYER1_WIN[:]:# loop over a slice copy '[:]' of PLAYER1_WIN
            if item == data:
                rps_player1_wins()
        for item in PLAYER2_WIN[:]:#loop over a slice copy
            if item == data:
                rps_player2_wins()
    
               
def rps_reciprocalof_listelements(x,y):
    return x * 1/y# reciprocal of like elements in list returns 1, i.e there was a draw.
    
                
def rps_response_decode(decode_list):
    for item in decode_list:
        if item == 'r':
            return 1
        elif item == 'p':
            return 2
        elif item == 's':
            return 3
        else:
            return(0)# i think this should probably call rps_restart_question()
            
def rps_entry_check(x):
    if any([i>'z' or i<'a' for i in x]): #check to see if entry is alphabetic
        print "Please enter rock, paper or scissors..\n"
        restart = raw_input("\nRestart (y/Y), else q to quit : ")
        if (restart == 'y' or restart == 'Y'):
            rps_player_one()
        else:
            exit()

def rps_restart_question():
    restart = raw_input("\nEnter y or Y to restart, else q to quit : ")
    if (restart == 'y' or restart == 'Y'):
        rps_player_one()
    else:
        exit()

def rps_player1_wins():
    print "Player 1 Wins"
    rps_restart_question()
    
def rps_player2_wins():
    print "Player 2 Wins"
    rps_restart_question()
    
def rps_players_tie():
    print "It's a tie"
    rps_restart_question()  
    

rps_player_one()