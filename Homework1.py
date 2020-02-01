'''
Created on Jan 29, 2020

@author: Nick
'''


import random
import csv

gate1 = "yes"
initial_price_list = []     #Initializes the lists used to input data into the .csv
number_of_days_list = []
final_price_list = []


def stock_calc(price, days):  #Function used to run the stock price "day to day"
    """Runs the stock calculation simulation for n price and n number of days"""
    
    negative_count = 0
    positive_count = 0
    even_count = 0
    for i in range(0,days):
        
        random_percent = 1 + (round(random.uniform(-.02,.02), 2)) #Generates a float that is then added/subtracted to
        updated_price = price - (price * random_percent)          #1 to generate a decimal percent
        updated_price = abs(updated_price) 
        print(random_percent)
        print(updated_price)
        if random_percent < 1:            #Keeps track of the positive/negative/even percentage "day to day"
            negative_count += 1
            price = price - updated_price
        elif random_percent > 1:
            positive_count += 1
            price = price + updated_price
        else:
            even_count += 1
        
        
        
        print(price)
        i += 1
    return price, negative_count, positive_count, even_count   #Returns values for the print statement at the end of a given simulation
        

while gate1.lower() == "yes":
    
    stock_price = float(input("What is the initial price of the stock? "))    #Each block takes the user input for stock price and number of days,
    initial_price_list.append(stock_price)                                    #then calls the stock_calc function to run the simulation
    
    number_of_days = int(input("How many days would you like to simulate? "))
    number_of_days_list.append(number_of_days)
    
    updated_price, negative_count, positive_count, even_count = stock_calc(stock_price, number_of_days)
    updated_price = round(updated_price, 2)
    final_price_list.append(updated_price)
    
    
    print("After " + str(number_of_days) + " days, " + str(updated_price) + " is the new stock price.")  #Print statement required for the homework.
    print("The stock price increased " + str(positive_count) + " times(s), decreased " + str(negative_count) +
          " times(s), and stayed the same " + str(even_count) + " times(s).")  
    
    gate1 = input("Would you like to perform another simulation (yes/no)? ")
    
with open("randomwalk.csv", "w") as file:           #Generates a .csv file to store the information required (Price, days, final price)
    writer = csv.writer(file, lineterminator = "\n")
    row1 = ["Initial price", "Number of days simulated", "Final Price"]
    writer.writerow(row1)
    for i in range(0, len(initial_price_list)):
        row = [initial_price_list[i], number_of_days_list[i], final_price_list[i]]
        writer.writerow(row)
    
                
            
    
    