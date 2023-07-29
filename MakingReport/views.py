from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import MarkList

def marklist_view(request):
    marklists = MarkList.objects.all()
    return render(request, 'Student/marklist.html', {'marklists': marklists})
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def pdf_view(request):
    marklists = MarkList.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="marklist.pdf"'

    p = canvas.Canvas(response)
    p.drawString(200, 800, "Student Mark List")
    p.drawString(30, 750, "Name")
    p.drawString(150, 750, "Roll Number")
    p.drawString(250, 750, "Math Marks")
    p.drawString(350, 750, "Science Marks")
    p.drawString(450, 750, "English Marks")

    y = 700
    for marklist in marklists:
        y -= 20
        p.drawString(30, y, marklist.name)
        p.drawString(150, y, marklist.roll_number)
        p.drawString(250, y, str(marklist.marks_math))
        p.drawString(350, y, str(marklist.marks_science))
        p.drawString(450, y, str(marklist.marks_english))

    p.showPage()
    p.save()

    return response
