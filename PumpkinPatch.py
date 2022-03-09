#Michael Brooks
#Pumpkin Patch
#Takes a .dat file for pumpkins and converts it to a readable and printable report.
#10/24/2021
from datetime import date
pumpkinFile = ''
pumpkinReportFile = ''
page = 1
lineNumber = 0

def main():
    global pumpkinFile
    global pumpkinReportFile
    totalQuantity = 0
    totalStoreCost = 0
    line = init()
    headings()
    storeName, patchName, quantity, price, storeCost = processLine(line)

    #Read and callPrintLine until EOF
    while line != '':
        storeName, patchName, quantity, price, storeCost = processLine(line)
        printLine(storeName, patchName, quantity, price, storeCost)
        line = read()
        totalQuantity += quantity
        totalStoreCost += storeCost

    footing(totalQuantity, totalStoreCost)

    pumpkinFile.close()
    pumpkinReportFile.close()



def init():
    global pumpkinFile
    global pumpkinReportFile

    #Open report and data file
    try:
        pumpkinFile = open(r'PUMPKIN.DAT')
        line = read()
    except:
        print("Data file could not be read")
        line = ''

    try:
        pumpkinReportFile = open('PumpkinReport.prt', 'a')
        #Erasing the old report
        pumpkinReportFile.truncate(0)
    except:
        print("Report file could not be read")

    return line


def processLine(line):
    storeName = line[0:9]
    patchName = getPatch(line[10])
    quantity = int(line[11:14])
    priceString = line[14:17]
    #Add a . for easy conversion to float
    priceString = priceString[:1] + "." + priceString[1:]
    price = float(priceString)
    storeCost = quantity * price
    return(storeName, patchName, quantity, price, storeCost)

def getPatch(patchId):
    patchName = ""
    if(patchId == "N"):
        patchName = "Name       "
    elif(patchId == "S"):
        patchName = "Skunk Creek"
    elif(patchId == "B"):
        patchName = "Back 40    "
    else:
        patchName = "Unkown     "
    return patchName

def read():
    global pumpkinFile
    line = pumpkinFile.readline()
    return line

def countLine():
    global page
    global lineNumber
    lineNumber += 1
    if(lineNumber > 25):
        page += 1
        lineNumber = 0
        headings()

def headings():
    global pumpkinReportFile
    global page
    today = date.today().strftime("%d/%m/%Y")
    pumpkinReportFile.write("Date: " + today + format("", "14s") + "Great Pumpkin Ranch" + format("", "22s") + "Page: " + format(page, "3") + "\n")
    pumpkinReportFile.write(format("", "33s") + "Sales Report" + "\n")
    pumpkinReportFile.write("Store Name" + format("", "9s") + "Patch Name" + format("", "11s") + "Quantity" + format("", "10s") + "Price" + format("", "7s") + "Store Cost" + "\n")

def printLine(storeName, patchName, quantity, price, storeCost):
    global pumpkinReportFile

    pumpkinReportFile.write(storeName + format(" ", "10s") + patchName + format(" ", "15s") + format(quantity, "3") + format(" ", "11s") + format(price, "3.2f") + format("", "9s") + format(storeCost, "8,.2f") +"\n")

def footing(totalQuantity, totalStoreCost):
    global pumpkinReportFile
    pumpkinReportFile.write(format("", "3s") + "Grand Totals" + format("", "28s") + format(totalQuantity, "5,") + format("", "22s") + format(totalStoreCost, "10,.2f"))
main()