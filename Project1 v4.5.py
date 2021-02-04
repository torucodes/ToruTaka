# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:16:13 2021

@author: torut
"""

import sys
import os.path
import csv

fileName = "inventory.csv"

def init():
    if os.path.isfile(fileName):
        print ("File " + fileName + " found")
    else:
        with open(fileName, 'w') as csvFile:
            print(fileName + " created.")
            csvFile.close()
def addItem(itemName, itemAmt, itemPrice):
    #Add Item in CSV
    itemFull = itemName + "," + itemAmt + "," +  itemPrice
    
    with open(fileName, 'a',  newline='') as csvFile:
        fileWriter = csv.writer(csvFile, delimiter=',',
                             quoting=csv.QUOTE_MINIMAL)
        fileWriter.writerow(itemFull.split())
        print("Item " + itemName + " added.")
    csvFile.close()
        

def listItem():
    #List Items in CSV
    with open(fileName, 'r', newline='') as csvFile:
        #fileReader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        print("Name,Amount,Price")
        for row in csvFile:
            if row.isspace():
                continue
            print(row.strip())            
    csvFile.close()
    
def updateItem(item):
    #Update Entered Item in CSV
    lines = list()
        
    with open(fileName, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field.startswith(item):                    
                    lines.remove(row)
                    print("Item " + item + " deleted.")

    with open(fileName, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for x in lines:
            if not lines:
                continue
            writer.writerow(x)
    
def deleteItem(item):
    #Delete Item in CSV
    lines = list()
        
    with open(fileName, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field.startswith(item):                    
                    lines.remove(row)
                    print("Item " + item + " deleted.")

    with open(fileName, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for x in lines:
            if not lines:
                continue
            writer.writerow(x)

def createEntry():
    itemName = input("Enter Item Name: ")
    itemAmt = input("Enter Item Amount: ")
    itemPrice = input("Enter Item Price: ")
    addItem(itemName, itemAmt, itemPrice)
def readEntry():
    listItem()
def updateEntry():
    print("NOTE: Items not found will have new entries created.")
    searchItem = input("Enter Item to be Updated: ")
    newAmt = input("Enter New Amount: ")
    newPrice = input("Enter New Price: ")
    deleteItem(searchItem)
    addItem(searchItem,newAmt,newPrice)
def deleteEntry():
    searchItem = input("Enter Item to be Deleted: ")
    deleteItem(searchItem)

#Main Program
init()

while(True):
    print("\n======================")
    print("1. Create a new entry")
    print("2. Display all entries")
    print("3. Update an entry")
    print("4. Delete an entry")
    print("5. Exit program")
    print("======================")
    choice = input("Choice: ")
    if choice == '1':
        print("======================")
        print("Creating New Entry: ")
        print("======================")
        createEntry()
        print("======================\n")
    elif choice == '2':
        print("======================")
        print("Displaying All Entries: ")
        print("======================")
        readEntry()
        print("======================\n")
    elif choice == '3':
        print("======================")
        print("Update Entry: ")
        print("======================")
        updateEntry()
        print("======================\n")
    elif choice == '4':
        print("======================")
        print("Delete Entry: ")
        print("======================")
        deleteEntry()
        print("======================\n")
    elif choice == '5':
        sys.exit(0)
    else:
        print("Input correct option")


