from django.contrib import admin
from csv_export.views import CSVExportView
from .models import LoanQuestion, LoanQuestionOptions, BorrowerResponse

@admin.register(LoanQuestion)
class LoanQuestionAdmin(admin.ModelAdmin):
    list_display = ('order', 'question', 'has_options')
    list_filter = ['order']
    
    
class DataAdmin(admin.ModelAdmin):
    actions = ("export_data_csv",)

    def export_data_csv(self, request, queryset):
        view = CSVExportView(queryset=queryset, fields="__all__")
        return view.get(request)

    export_data_csv.short_description = "Export CSV for selected Data records"
    
    
    
@admin.register(LoanQuestionOptions)
class LoanQuestionAdmin(admin.ModelAdmin):
    list_display = ('option', 'question')
    

@admin.register(BorrowerResponse)
class BorrowerResponseAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'question', 'selected_option', 'response_text', 'pub_date')
    list_filter = ['question']
