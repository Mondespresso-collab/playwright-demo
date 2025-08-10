#!/bin/python3

import math
import os
import random
import re
import sys

def maxsetHourglass(array_s):
    rarray = array_s
#    if len(rarray) >3:
    rowcount = len(rarray) - 2
    colcount = len(rarray[0]) - 2
#    elif len(rarray)==3:
#             rowcount = len(rarray)-2
#             colcount = len(rarray[0])-2
    return rowcount, colcount

     
TopRow=[]
Middle=[]
BottomROw=[]
sumhourg=[]
arr = []
countrowcol=0

if __name__ == '__main__':
    while True:
        try: 
            arr.clear()    
            sumhourg.clear()
            print("\nHow many rows do you want to enter? (Minimum 3, or type 'exit' to quit):")
            row_input = input("Rows: ").strip()
            if row_input.lower() == 'exit':
                print("Exiting program.")
                exit()
            if int(row_input)  < 3:
                continue       
#            TopRow.clear
#            Middle.clear
#            BottomROw.clear    
            for i in range(int(row_input)):
                arr.append(list(map(int, input().rstrip().split())))
                        
            rows,cols = maxsetHourglass(arr)     
            for i in range(rows):
                    if len(arr)<3 or len(arr[0])<3 or len(arr[2])<3:
                        print("Minimum 3 rows and 3 columns")
                        continue
                    for j in range (cols):

                        TopRow=arr[i][j] + arr[i][j+1] + arr[i] [j+2]
                        Middle=arr[i+1][j+1]
                        BottomROw=arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                        sumhourg.append(int(TopRow) + int(Middle) + int(BottomROw))  
            print(f"value {max(sumhourg)}:  Hourglass = {sumhourg.index(max(sumhourg))+1}")

        except ValueError:
            print("❌ Invalid format: Please enter space-separated integers.")    
             
