from django.shortcuts import render
from .forms import ContactForm,StudentForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def student_view(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = StudentForm()

    return render(request, 'student.html', {'form': form})
