import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.shared import qn
from docx.shared import Pt
from workCrew.models import Student, Job, Day_Info 
import random
import datetime
#import arrow




def docCreator():
    weekdays = Day_Info.objects.all().order_by('order')
    #theDate = datetime.date.today() #this may need to be replaced by a prompt of some kind
    #strDate = theDate.strftime('%m/%d/%Y')
    #intDay = int(theDate.day)
    theDay = datetime.date.today()
    weekList = []
    weekdayNumber = theDay.weekday()
    wkcounter = 0
    while wkcounter < 7:
        weekList.append(weekdayNumber)
        if weekdayNumber == 6:
            weekdayNumber = 0
        else:
            weekdayNumber += 1
        wkcounter += 1
    weekdays3 = [weekdays[i] for i in weekList]
    theDayDay = theDay.day
    theDayMo = theDay.month
    theDayYear = theDay.year
    for weekday in weekdays3: #this area allows for the program to be run any day
        #intDay = intDay + 1
        
        checkDate = datetime.date(theDayYear,theDayMo,theDayDay)
        theDayDay += 1
        amJobs = Job.objects.filter(day__contains = weekday).filter(time='am')
        pmJobs = Job.objects.filter(day__contains = weekday).filter(time='pm')
        #jobs = Job.objects.all()
        students = Student.objects.filter(arrival_Date__lt=checkDate)
        arrivals = Student.objects.filter(arrival_Date = checkDate)
        departures = Student.objects.filter(departure_Date = checkDate)
        strArrivals = ""
        strDepartures = ""
        for a in arrivals:
            strArrivals += (a.first_Name + " ")
            
        for d in departures:
            strDepartures += (d.first_Name + " ")
       
       
        jobnames = []
        jobnamesB = []
        
        studentnames = []  
        strstudentnames = ""
        mealplace = ["a","b"]
        
        schdictAM = {}
        schdictPM = {}
        mealdict = {}
        
        for s in students:
            studentnames.append(s.first_Name)
            strstudentnames += (s.first_Name + " ")
        
        
        random.shuffle(studentnames)
        a = 0    
        b = 3
        
        for j in amJobs:
            jobnames.append(j.work_Name)
            schdictAM[j.work_Name] = studentnames[a:b]
            del studentnames[a:b]
            a+=3
            b+=3
        
        
        q = 0    
        r = 3
        for jb in pmJobs:
            jobnamesB.append(jb.work_Name)
            schdictPM[jb.work_Name] = studentnames[q:r]
            q+=3
            r+=3
        
        c = 0
        d = 0
        if len(studentnames) -1 > 14:        
            d = (len(studentnames)-1) /2
            
        else:
            d = len(studentnames)-1
            
        for m in mealplace:
            mealdict[m] = studentnames[c:d]
            
            if d == len(studentnames)-1:
                break 
            c = d
            d = len(studentnames)-1 # comeback
        
        lunch = ""
        for m in mealdict:
            #lunch += m         
            for ele in mealdict[m]:
                lunch += (ele + " ")

        workAM = ""
        
        for w in schdictAM:           
            
            if workAM != "":
                workAM += "\n"            
            workAM += (w + "- ")
            
            for wele in schdictAM[w]:
                workAM += (wele + "  ") 
                # if wele == "Morning Grounds":
                    # break
                
        
        workPM = ""
        
        for w in schdictPM:                      
            if workPM != "":
                workPM += "\n"            
            workPM += (w + "- ")
                
            for wele in schdictPM[w]:
                workPM += (wele + "  ") 
                    # if wele == "Morning Grounds":
                        # break
        
        
        
        document = docx.Document()#creating document
        
        
        #assign day
        pweekday = checkDate.strftime('%A' ) + " " + checkDate.strftime('%B' ) +  " " + str(checkDate.day) 
        #pweekday = str(weekdays) + str(weekdays3)
        day = document.add_paragraph(pweekday)
        day_format = day.paragraph_format
        day_format.space_after = Pt(18)
        day_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        #breakfast infor
        breakfastTime = document.add_paragraph("8:00am Breakfast -(everyone expected)")
        breakfastTime_format = breakfastTime.paragraph_format
        breakfastTime_format.space_after = Pt(18)
        breakfastTime_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        locationB = document.add_paragraph("At Chalet Bellevue")
        locationB_format = locationB.paragraph_format
        locationB_format.space_after = Pt(18)
        locationB_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        tableB = document.add_table(rows=1, cols=1)
        tableB.borders={'All':Pt(.2)}
        row1B = tableB.rows[0]
        cell1B = row1B.cells[0]
        cell1B.text = strstudentnames
        
        arrivals = document.add_paragraph("Arrivals: " + strArrivals)
        arrivals_format = arrivals.paragraph_format
        arrivals_format.space_before = Pt(18)
        arrivals_format.space_after = Pt(0)
        arrivals_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        departures = document.add_paragraph("Departures: " + strDepartures)
        departures_format = departures.paragraph_format
        departures_format.space_after = Pt(18)
        departures_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        
        
        if weekday.Lunch_A != 'none':
            lunchTime = document.add_paragraph("1:00 Lunch-(everyone expected)")    
            lunchTime_format = lunchTime.paragraph_format
            lunchTime_format.space_after = Pt(18)
            lunchTime_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            locationLa = document.add_paragraph("At Chalet " + weekday.Lunch_A)#plus the location  
            locationLa_format = locationLa.paragraph_format
            locationLa_format.space_after = Pt(18)
            locationLa_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            tableLa = document.add_table(rows=1, cols=1)
            row1La = tableLa.rows[0]
            cell1La = row1La.cells[0]
            cell1La.text = strstudentnames
        else:
            locationLa = document.add_paragraph("Packed lunches are in the student fridge")
            locationLa_format = locationLa.paragraph_format
            locationLa_format.space_after = Pt(18)
            locationLa_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        
        
        if len(studentnames) > 14 and weekday.Lunch_B != 'none':
            locationLb = document.add_paragraph("At Chalet " + weekday.Lunch_B)#plus the location         
            locationLb_format = locationLb.paragraph_format
            locationLb_format.space_after = Pt(18)
            locationLb_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            tableLb = document.add_table(rows=1, cols=1)
            row1Lb = tableLb.rows[0]
            cell1Lb = row1Lb.cells[0]
            cell1La.text = lunch[0: int(round((len(lunch)/2 -1)))] # comeback to this
            cell1Lb.text = lunch[ int(round((len(lunch))/2 )):len(lunch) - 1]
        
        dinnerTime = document.add_paragraph("6:30 Dinner -(everyone expected)")    
        dinnerTime_format = dinnerTime.paragraph_format
        dinnerTime_format.space_before = Pt(40)
        dinnerTime_format.space_after = Pt(18)
        dinnerTime_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        locationD = document.add_paragraph("At Chalet Bellevue with " + weekday.dinner)
        locationD_format = locationD.paragraph_format
        locationD_format.space_after = Pt(18)
        locationD_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        tableD = document.add_table(rows=1, cols=1)
        row1D = tableD.rows[0]
        cell1D = row1D.cells[0]
        cell1D.text = strstudentnames
        
        workPara = document.add_paragraph("Work Assignments: if your name is not down for a work crew, you have a study day:")    
        workPara_format = workPara.paragraph_format
        workPara_format.space_before = Pt(20)
        workPara_format.space_after = Pt(6)
        workPara_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        tablew = document.add_table(rows=1, cols=2)
        cell1w = tablew.rows[0].cells[0]
        cell1w.text = ("am\n \n 7:30 Breakfast Prep: \n 7:50 Trash out- \n 9:30am: \n \n" + workAM)
        cell2w = tablew.rows[0].cells[1]
        cell2w.text = ("pm\n \n 3:00pm:\n \n" + workPM + "\nInternet collection at dinner- \nNight Office- \nDay Off- ")
        document.save('oldschedules/' + pweekday +'.docx')