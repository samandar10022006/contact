from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
            return redirect('messages_list')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})


class MessagesListView(ListView):
    model = ContactMessage
    template_name = 'messages_list.html'
    context_object_name = 'messages'
    ordering = ['-created_at']

