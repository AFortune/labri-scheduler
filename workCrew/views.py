#from django.shortcuts import render
import docCreator
import os
import zipfile
import StringIO
from django.http import HttpResponse
import datetime
# Create your views here.
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
def index(request):
    docCreator.docCreator()
    
    filenames = thisweeksdates()

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "thisweek"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = StringIO.StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    output = 'success'
    return resp

def allergies(request):
    output = "placeholder"
    return HttpResponse(output)