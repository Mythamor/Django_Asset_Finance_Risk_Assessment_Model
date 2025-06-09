from django.db import models
from django.contrib.auth.models import User


class LoanQuestion(models.Model):
    question = models.CharField(max_length=500, unique=True)
    order = models.IntegerField()
    has_options = models.BooleanField(default=False)

    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f'{self.order}.{self.question}'


class LoanQuestionOptions(models.Model):
    question = models.ForeignKey(
        LoanQuestion, related_name='options', on_delete=models.CASCADE
        )
    option = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.option} for {self.question.question}'
    
 
class BorrowerResponse(models.Model):
    borrower = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
    question = models.ForeignKey(LoanQuestion, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(LoanQuestionOptions, on_delete=models.CASCADE, null=True)
    response_text = models.PositiveBigIntegerField(blank=False, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        if self.selected_option:
            return f'{self.borrower.username} - {self.question.question}: {self.selected_option.option}'
        else:
            return f'{self.borrower.username} - {self.question.question}: {self.response_text}'