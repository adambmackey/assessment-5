log_file = open("um-server-01.txt") #creates a varialbe, assigns that variable to a .txt file and opens it


def sales_reports(log_file): #a function that takes in one argument
    for line in log_file: # a for loop that will loop through the .txt file opened above, I believe "line" referes to each line in the .txt file.
        line = line.rstrip()  # line is a varible that is then given a method to remove an trailing spaces
        day = line[0:3] # day is assigned to the third column.
        if day == "Mon": #if statement that asks if the day is Tue.
            print(line) #print the result. 


sales_reports(log_file)# runs the function. 

# 
