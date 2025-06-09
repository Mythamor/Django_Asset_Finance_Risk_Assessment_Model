from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import LoanQuestion, LoanQuestionOptions, BorrowerResponse


# Create your views here.
def index(request):
    """Home Page"""

    return render(request, 'car_loan/welcome.html')


def get_loan(request, username, question_id):
    """Display a single question and collect the response."""
    
    user = get_object_or_404(User, username=username )
    
    question = get_object_or_404(LoanQuestion, id=question_id)
    questions = LoanQuestion.objects.filter(id=question_id)
    
    
    if request.method == "POST":
        
        if question.has_options:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if not selected_option_id:
                return render(request, 'car_loan/home.html', {
                    'questions': questions,
                    'error_message': "Please select an option"
                })
            selected_option = LoanQuestionOptions.objects.get(id=selected_option_id)
            response_text = None
            
        else:
            selected_option = None
            response_text = request.POST.get(f'open_question_{question.id}')
            if not response_text:
                return render(request, 'car_loan/home.html', {
                    'questions': questions,
                    'error_message': "Please enter a response"
                })

        
        # Save borrower response
        BorrowerResponse.objects.create(
                borrower=user, 
                question=question, 
                selected_option=selected_option,
                response_text=response_text
        )
        
        next_question = LoanQuestion.objects.filter(order__gt=question.order).order_by('order').first()
        if next_question:
            return redirect('get_loan', username=username, question_id=next_question.id)
        else:
        
            return redirect('home')
    
    
    return render(request, 'car_loan/home.html', {
        'questions': questions,
        'username': username
        
        })




# Predict function
# def predict(form_data)
# Pickled model
# Get response from form
# Jsonify the data from the form




    
