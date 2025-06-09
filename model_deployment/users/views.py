from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from car_loan.models import LoanQuestion


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} created!')
             # Get the first question 
            first_question = LoanQuestion.objects.order_by('order').first()
            if first_question:
                return redirect('get_loan', username=username, question_id=first_question.id)
            #else:
            #    return render(request, 'users/register.html', {'form': form})
        #else:
            #messages.error(request, f'An error occurred during registration!')
    else:
        form = UserRegisterForm()

       
    return render(request, 'users/register.html', {'form': form})