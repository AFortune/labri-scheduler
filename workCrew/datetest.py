def halfList(list, firstSecond):
    firstHalf = []
    secondHalf = []   
    firstHalf = list[0:((len(list)-1)/2)]
    secondHalf = list[((len(list) -1)/2): len(list)]
    
    if firstSecond == "firstHalf":
        return firstHalf
        
    elif firstSecond == "secondHalf":
        return secondHalf
  
array = ["aaron","david","Katrina", "Joseph", "Wyatt","Andrew", "Greg", "Wesley", "George", "ten", "eleven", "twelve", "George", "ten", "eleven", "twelve","12"]
print halfList(array, "firstHalf")
print ' '.join(halfList(array, "secondHalf"))

def cycleAssignment(dict, jobList, namelist):
    while x == 0:
        print 1
    
testdict = {
    "Grounds": ["aaron", "wyatt"],
    "Cleaning": ["david", "joe"],

}


print testdict.keys()[0]