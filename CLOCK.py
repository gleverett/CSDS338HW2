import random

class page:

    #initializes the page with a given name for the page number
    def __init__(self, pgNum):
        self.pageNumber = pgNum
        self.secChance = False

    #returns page number
    def getPageNumber(self):
        return self.pageNumber

    #sets second chance boolean value
    def getSecChance(self):
        return self.secChance

    #sets page number to given value
    def setPageNumber(self, tmpPgNum):
        self.pageNumber = tmpPgNum

    #sets second chance boolean value to given boolean value
    def setSecChance(self, tmpSecChance):
        self.secChance = tmpSecChance

class CLOCK:
    '''
    currentPages = []
    capacity = 0
    pageFaults = 0
    '''

    #constructor for CLOCK replacement algorithm
    def __init__(self, currentPages, cap):
        self.currentPages = []
        self.capacity = cap
        self.pageFaults = 0

    #returns list with the current pages in memory
    def getCurrentPages(self):
        return self.currentPages

    #returns capacity of list
    def getCapacity(self):
        return self.capacity

    #returns number of page faults
    def getPageFaults(self):
        return self.pageFaults

    #sets capacity of list
    def setCapacity(self, cap):
        self.capacity = cap

    #checks to see whether the memory is at capacity or not
    def full(self):
        #if the length of the list is equal to the capacity value...
        if(len(self.currentPages)==self.getCapacity()):
            print("Memory is full.")
            return True
        else:
            return False

    #finds if a given page number is already in the list
    def find(self, number):
    # If the page we are searching for is already in the queue, this method will return true
        for i in self.currentPages:
            if(i.getPageNumber()==number):
                #if we hit the page we are looking for, it will be given a second chance, therefore setting its value to true
                newSecChance = True
                i.setSecChance(newSecChance)
                return True 
        return False

    #tries to add a page to memory
    def addPage(self, tmpPage):
        print("swapping in page " + str(tmpPage.getPageNumber()) +"...")
        tmpPageNum = tmpPage.getPageNumber()

        #determines whether or not page is already in memory
        if(self.find(tmpPageNum)):
            print("page " + str(tmpPage.getPageNumber()) + " is already in memory.")
            return False
        
        #determines whether or not memory is full
        if(self.full()):
            self.removePage(tmpPage)
            return True

        #if neither of the above are true, a new page will be added to memory without making further adjustments
        self.currentPages.append(tmpPage)
        self.pageFaults+=1
        print("page " + str(tmpPage.getPageNumber()) + " has been added.")
        print("total page faults: " + str(self.getPageFaults()))

    #method to remove a page from memory and replace the removed page
    def removePage(self, pageToAdd):
        #checks each page in memory, if their second chance value is set to true, loop sets it to false and moves to next page
        for i in self.currentPages:
            if(i.getSecChance() == True):
                tmpSecChance = False
                i.setSecChance(tmpSecChance)
            #if second chance value of a page is false, this page will be replaced
            elif(i.getSecChance() == False):
                print("page " + str(i.getPageNumber()) + " has been removed.")
                index = self.currentPages.index(i)
                self.currentPages.append(pageToAdd)
                self.pageFaults+=1
                print("page " + str(pageToAdd.getPageNumber()) + " has been added.")
                print("total page faults: " + str(self.getPageFaults()))
                return True

        #if all pages had a second chance value of true, we replace the first page in memory with the new page
        self.currentPages[0] = pageToAdd
        self.pageFaults+=1
        print("page " + str(pageToAdd.getPageNumber()) + " has been added.")
        print("total page faults: " + str(self.getPageFaults()))

                
                
#initialize 10 different pages 
page0 = page(0)
page1 = page(1)
page2 = page(2)
page3 = page(3)
page4 = page(4)
page5 = page(5)
page6 = page(6)
page7 = page(7)
page8 = page(8)
page9 = page(9)
#add all pages to an array that pages will be randomly chosen from to add to memory
files = [page(1), page(2), page(3), page(4), page(5), page(6), page(7), page(8), page(9)]

#initialize a new memory list for FIFO algorithm and initialize FIFO for random distribution
memoryList = []
CLOCK1 = CLOCK(memoryList, 3)
length = len(files)
 
#random distribution
print("\nCLOCK IN RANDOM DISTRIBUTION:")
#adds a random page to FIFO memory 10 times to test random distribution
for i in range(0,length):
    ranNum = random.randint(0,length-1)
    CLOCK1.addPage(files[ranNum])

#strongly biased towards lower numbers
print("\nCLOCK BIASED TOWARDS LOWER NUMBERS:")
memoryList2 = []
CLOCK2 = CLOCK(memoryList2, 3)

#adds files more as their number gets lower
files2 = []
for i in range(0,512):
    if (i==0):
        files2.append(page9)
    elif(i<=2):
        files2.append(page8)
    elif(i<=4):
        files2.append(page7)
    elif(i<=8):
        files2.append(page6)
    elif(i<=16):
        files2.append(page5)
    elif(i<=32):
        files2.append(page4)
    elif(i<=64):
        files2.append(page3)
    elif(i<=128):
        files2.append(page2)
    elif(i<=256):
        files2.append(page1)
    elif(i<=512):
        files2.append(page0)

length2 = len(files2)
for i in range(0,10):
    ranNum = random.randint(0,length2-1)
    CLOCK2.addPage(files2[ranNum]) 

#strongly biased towards 3<k<10, otherwise exponential (0 will be added the same amount as 3<k<10)
print("\nCLOCK BIASED TOWARDS 3<K<10:")
memoryList3 = []
CLOCK3 = CLOCK(memoryList3, 3)

#adds files exponentially again, but for pages 3<k<10, they will all be added as much as page 0
files3 = []
for i in range(0,30):
    if(i<=16):
        files3.append(page0)
        files3.append(page4)
        files3.append(page5)
        files3.append(page6)
        files3.append(page7)
        files3.append(page8)
        files3.append(page9)
    elif(i<=24):
        files3.append(page1)
    elif(i<=28):
        files3.append(page2)
    elif(i<=30):
        files3.append(page3)

length3 = len(files3)
for i in range(0,10):
    ranNum = random.randint(0,length3-1)
    CLOCK3.addPage(files3[ranNum]) 




