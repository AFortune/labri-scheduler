import datetime
def halfList(list, firstSecond):
    firstHalf = []
    secondHalf = []   
    firstHalf = list[0:((len(list)-1)/2)]
    secondHalf = list[((len(list) -1)/2): len(list)]
    
    if firstSecond == "firstHalf":
        return firstHalf
        
    elif firstSecond == "secondHalf":
        return secondHalf
  
arrayPeeps = ["aaron","david","Katrina", "Joseph", "Wyatt","Andrew", "Greg", "Wesley", "George", "ten", "eleven", "twelve", "George", "ten", "eleven", "twelve","12"]
arrayJobs = ["Grounds", "Cleaning"]

def simpleAssign(listP, listJ):
    resultdict = dict.fromkeys(listJ, [])
    for 
        
        
    #return resultdict

def cycleAssignment(dict, jobList, namelist):
    while x == 0:
        print 1
    
testdict = {
    "Grounds": ["aaron", "wyatt"],
    "Cleaning": ["david", "joe"],

}
def thisweeksdates():
    date = datetime.date.today() + datetime.timedelta(days = 1)
    dateList = []
    dayCount = 0
    while dayCount < 7:
        fileDateString = "oldschedules/" + date.strftime('%A' ) + " " + date.strftime('%B' ) +  " " + str(date.day) + ".docx"
        dateList.append(fileDateString)
        date = date + datetime.timedelta(days = 1)
        dayCount += 1
    return dateList


# print testdict.keys()[0]
simpleAssign(arrayPeeps, arrayJobs)
