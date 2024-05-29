# This program simulates a line within an ATM machine. The user inputs the number of clients, the max number of time,
# with their transaction, and their arrival time. The program will output a table with the information of each client like so:
# | Client | Time between arrivals | Arrival time | Transaction time | Start time | End time | Waiting time | Innactivity time |
# The program will also output the average waiting time and the average innactivity time, as well as the probability of waiting time 
# and the percentage of innactivity time.
# The first client will naturally have 0 as his waiting time and innactivity time and his time between arrivals will be 0 as well,
# because he is the first client. The program will also output the total time the simulation took.

import random
import numpy as np
import pandas as pd

# Function that simulates the ATM line
def ATMLine(numClients, maxTime):
    # Variables
    clients = []
    time = 0
    totalWaitingTime = 0
    totalInnactivityTime = 0
    totalTransactionTime = 0
    totalArrivalTime = 0
    totalStartTime = 0
    totalEndTime = 0
    totalInnactivityTime = 0
    totalWaitingTime = 0
    totalInnactivityTime = 0
    # Loop for each client
    for i in range(numClients):
        # Variables
        timeBetweenArrivals = random.randint(0, maxTime)
        arrivalTime = time + timeBetweenArrivals
        transactionTime = random.randint(1, 10)
        # If the client arrives before the ATM is free
        if arrivalTime < totalEndTime:
            waitingTime = totalEndTime - arrivalTime
            totalWaitingTime += waitingTime
            startTime = totalEndTime
            endTime = startTime + transactionTime
        # If the client arrives after the ATM is free
        else:
            waitingTime = 0
            startTime = arrivalTime
            endTime = startTime + transactionTime
        innactivityTime = arrivalTime - totalEndTime
        # Add the client to the list
        clients.append([i + 1, timeBetweenArrivals, arrivalTime, transactionTime, startTime, endTime, waitingTime, innactivityTime])
        # Update the total times
        totalTransactionTime += transactionTime
        totalArrivalTime += arrivalTime
        totalStartTime += startTime
        totalEndTime += endTime
        totalInnactivityTime += innactivityTime
        time = arrivalTime
    # Create the table
    df = pd.DataFrame(clients, columns = ['Client', 'Time between arrivals', 'Arrival time', 'Transaction time', 'Start time', 'End time', 'Waiting time', 'Innactivity time'])
    # Calculate the averages
    avgWaitingTime = totalWaitingTime / numClients
    avgInnactivityTime = totalInnactivityTime / numClients
    # Calculate the probability of waiting time
    probWaitingTime = totalWaitingTime / totalTransactionTime
    # Calculate the percentage of innactivity time
    percInnactivityTime = totalInnactivityTime / totalEndTime
    # Output the table
    print(df)
    # Output the averages
    print
    print("Average waiting time: ", avgWaitingTime)
    print("Average innactivity time: ", avgInnactivityTime)
    print("Probability of waiting time: ", probWaitingTime)
    print("Percentage of innactivity time: ", percInnactivityTime)
    print("Total time: ", totalEndTime)

# Main
numClients = int(input("Enter the number of clients: "))
maxTime = int(input("Enter the max time between clients: "))
ATMLine(numClients, maxTime)

