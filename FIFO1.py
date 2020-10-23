import random

class page:

    #initializes the page with a given name for the page number
    def __init__(self, pgNum):
        self.pageNumber = pgNum

    #returns page number
    def getPageNumber(self):
        return self.pageNumber

    #sets page number to given value
    def setPageNumber(self, tmpPgNum):
        self.pageNumber = tmpPgNum

class FIFO:
    '''
    pageList = []
    capacity = 0
    pageFaults = 0

    '''
    #initializes FIFO memory system with a given list and capacity 
    def __init__(self, pageList, cap):
        self.pageList = []
        self.capacity = cap
        self.pageFaults = 0

    #returns list associated with FIFO 
    def getPageList(self):
        return self.pageList

    #returns capacity of list 
    def getCapacity(self):
        return self.capacity

    #returns number of page faults
    def getPageFaults(self):
        return self.pageFaults

    def setCapacity(self, cap):
        self.capacity = cap

    #checks whether or not the list is full
    def full(self):
        #if the length of the list is equal to the capacity value...
        if(len(self.pageList)==self.getCapacity()):
            print("Memory is full.")
            return True
        else:
            return False

    #finds if a given page number is already in the list
    def find(self, number):
    # If the page we are searching for is already in the queue, this method will return true
        for i in self.pageList:
            if(i.getPageNumber()==number):
                return True 
        return False

    #adds a given page to the list
    def addPage(self, tmpPage):
        print("swapping in page " + str(tmpPage.getPageNumber()) +"...")
        tmpPageNum = tmpPage.getPageNumber()

        #runs find method to see if page being added is already in memory
        if(self.find(tmpPageNum)):
            print("page " + str(tmpPage.getPageNumber()) + " is already in memory.")
            return False

        #runs full method to see if list is full and must swap out a page
        if(self.full()):
            self.removePage()
        self.pageList.append(tmpPage)

        #adds page fault
        self.pageFaults+=1

        print("page " + str(tmpPage.getPageNumber()) + " was added.")
        print("total page faults: " + str(self.getPageFaults()))
        return True

    #removes page from list of memory
    def removePage(self):
        removedPage = self.pageList.pop(0)
        print("page " + str(removedPage.getPageNumber()) + " has been removed.")



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
FIFO1 = FIFO(memoryList, 3)
length = len(files)
 
#random distribution
print("\nFIFO IN RANDOM DISTRIBUTION:")
#adds a random page to FIFO memory 10 times to test random distribution
for i in range(0,length):
    ranNum = random.randint(0,length-1)
    FIFO1.addPage(files[ranNum])

#strongly biased towards lower numbers
print("\nFIFO BIASED TOWARDS LOWER NUMBERS:")
memoryList2 = []
FIFO2 = FIFO(memoryList2, 3)

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
    FIFO2.addPage(files2[ranNum]) 

#strongly biased towards 3<k<10, otherwise exponential (0 will be added the same amount as 3<k<10)
print("\nFIFO BIASED TOWARDS 3<K<10:")
memoryList3 = []
FIFO3 = FIFO(memoryList3, 3)

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
    FIFO3.addPage(files3[ranNum]) 





    

