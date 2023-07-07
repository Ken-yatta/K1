# A program to calculate BODY MASS INDEX
import math
while True:
    print("This is a program used to calculate your BMI.")
    input1= input("Would you like to use Imperial or Metric measurements? ")
    output= ["your BMI is ", "so you have a healthy BMI.", "so you are a tad bit overweight.", "so you are obese.", "you are underweight, your BMI is, ", ".", "Sorry, I didn't understand that. Please enter a number." ]
    while True:
        try:
            
        
            if input1== 'metric':
                height=float(input("Enter your height in cm: "))
                weight=float(input("Enter your weight in kg: "))
                BMI= weight/ (height**2) * 703
                
                if BMI>= 19 and BMI <=24:
                    print(output [0], BMI, output [1])
                elif BMI >=25 and BMI <=29:
                    print(output [0], BMI, output [2])
                elif BMI>= 30 and BMI<39:
                    print(output [0], BMI, output [3])
                elif BMI>39:
                    print(output [0], BMI, output [4])
                elif BMI<19:
                    print(output [5], BMI, output [6])
                    
            elif input1== 'imperial':
                height=float(input("Enter your height in inches: "))
                weight=float(input("Enter your weight in lbs: "))
                BMI= weight/ (height**2) *703
                if BMI>= 19 and BMI <=24:
                    print(output [0], BMI, output [1])
                elif BMI >=25 and BMI <=29:
                    print(output [0], BMI, output [2])
                elif BMI>= 30 and BMI<39:
                    print(output [0], BMI, output [3])
                elif BMI>39:
                    print(output [0], BMI, output [4])
                elif BMI<19:
                    print(output [5], BMI, output [6])
        
            break
        except ValueError:
            print(output [7])
            continue
    
    