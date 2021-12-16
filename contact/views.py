from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)