from sys import argv,exit
import csv
from time import sleep 
#opens csv file and interates over every row of it
def main():
    
    if len(argv) != 3: #checks if correct number of command line arguments are inputed.
        print("Usage: python dna.py data.csv sequence.txt")
        exit()
        
    csv_path = argv[1]
    #opens csv path.
    with open(csv_path) as csv_file: 
        reader = csv.DictReader(csv_file)
        dict_list =list(reader)
        fieldnames = reader.fieldnames  
        #gets columms of csv file
    
    text_path = argv[2]
    with open(text_path) as file: # opens txt path
        reader = csv.reader(file)
        text = list(reader)
        sequence = ''.join(text[0]) #converts list to string for easier working.
            
    
    count_max = {} #sets a dict that will receive the biggest sequences and their STR.
    counter = 0
    fieldnames.pop(0) #deletes 'name' key from dict for easier handling
    for i in fieldnames:
        dna = i  #gets a STR for each loop
        counter = 1
        count_max[dna] = 0
        for j in range(len(sequence)):
            if sequence[j: j + len(dna)] == dna:  #if sequence is equal to STR and the next sequence is also equal, start count
                if sequence[(j + len(dna)): (j + len(dna) + len(dna))] == dna:
                    counter += 1
        
                    count_max[dna] = counter
                    if counter > count_max[dna]:  # if a new bigger sequence is found replaces last biggest sequence
                        count_max[dna] = counter
                

    
    counter = 0
    
    for i in range(0, len(dict_list)): 
        counter = 0
        for key in fieldnames:
            if int(count_max[key]) == int(dict_list[i][key]): # sets a counter everytime a number is equal in both dicts
                counter += 1
            
            if counter == len(fieldnames) - 1: # if every STR is equal, determine match
                print(dict_list[i]["name"])
                print()
                exit()            
    
    print("No match.\n")
            
if __name__ == "__main__":
    
    main()    
    