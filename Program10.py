#********************************************************************
#
#  Developer:         Renee White
#
#  Program #:         10
#
#  File Name:         Program10.py
#
#  Description:       This program reads a survey's results into three lists and
#                     performs an analysis based on those results
#
#********************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#***************************************************************

def main():
    developerInfo()
    income, number, members = survey()
    avg(income,number)
    pv(income,number,members)
    
    
#***************************************************************
#
#  Function:     survey
# 
#  Description:  Reads the survey results and creates an outfile
#
#  Parameters:   None
#
#  Returns:      income,Num,member 
#
#***************************************************************
    
def survey():
    inFile = open('program10.txt', 'r')
    outFile = open('program10-out.txt', 'w')
    
    outFile.write('Welcome Back, Friend!\n')
    outFile.write('\n')
    outFile.write('The Township Income Survey Results Are In:\n')
    outFile.write('\n')
    outFile.write('\n')
    income = []
    Num = []
    member = []
    
    outFile.write(str("%12s %12s %16s\n" % ("Account #","Income","Members")))
    
    lineRead = inFile.readline()       # Read first record
    while lineRead != '':              # While there are more records
       words = lineRead.split()        # Split the records into substrings
       acctNum = int(words[0])         # Convert first substring to integer
       annualIncome = float(words[1])  # Convert second substring to float
       members = int(words[2])         # Convert third substring to integer
       income.append(annualIncome)
       Num.append(acctNum)
       member.append(members)
       
       print("%10d  %15.2f  %10d" % (acctNum, annualIncome, members))
       outFile.write(str("%10d   %16.2f   %12d\n" % (acctNum, annualIncome, members)))

       lineRead = inFile.readline()    # Read next record
    outFile.write('\n')
    outFile.write('\n')
    
    # Close the file.
    inFile.close() # Close file
    return income, Num, member
    
#***************************************************************
#
#  Function:     avg
# 
#  Description:  Performs an analysis of the average income
#
#  Parameters:   income,number
#
#  Returns:      Nothing 
#
#***************************************************************

def avg(income,number):
    total = 0
    outFile = open('program10-out.txt', 'a')
    for value in income:
        total += value
    average = total / len(income)
    outFile.write('The average household income is: ')
    outFile.write(str(format(average,'.2f')))
    outFile.write('\n')
    outFile.write('\n')
    outFile.write('These are the households that exceed the average: ')
    outFile.write('\n')
    outFile.write('\n')
    outFile.write(str("%12s %16s\n" % ("Account #","Income")))
    for n, i in zip(number, income):
        if i > average:
            outFile.write('\n')
            outFile.write(str("%10d" %(n)))
            outFile.write(str("%25.2f" %(i)))

#***************************************************************
#
#  Function:     pv
# 
#  Description:  Calculates and displays households below poverty level
#
#  Parameters:   income,number,members
#
#  Returns:      Nothing 
#
#***************************************************************

def pv(income,number,members):
    outFile = open('program10-out.txt', 'a')
    outFile.write('\n')
    outFile.write('\n')
    outFile.write('These are the households that are below the poverty level: ')
    outFile.write('\n')
    outFile.write('\n')
    outFile.write(str("%12s %16s\n" % ("Account #","Income")))
    for people in members:
        people = people - 2
        if people > 0 or people < 0:
            povertyLevel = 16460.00 + 4320.00 * (people)
        else:
            povertyLevel = 16460.00 + 4320.00
    for num, inc in zip(number, income):
        if inc < povertyLevel:
            outFile.write('\n')
            outFile.write(str("%10d" %(num)))
            outFile.write(str("%24.2f" %(inc)))
            Money = []
            Money.append(inc)
            outFile.write('\n')
            Divide = 14 / 31
    Percent = Divide / 100
    outFile.write('\n')
    outFile.write('The percentage of households below poverty level is: ')
    outFile.write('\n')
    outFile.write('\n')
    outFile.write(str(Percent))
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  prints programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************

def developerInfo():
    print('Name:     Renee White')
    print('Program:  10')
    print()
    # End of the developerInfo function

# Call the main function.
main()
