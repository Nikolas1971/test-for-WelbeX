from django.shortcuts import render
from .models import TestTable
from .forms import Form
from django.core.paginator import Paginator


def index(req):
    model = TestTable
    all_records = TestTable.objects.all()

    if req.method == 'POST':
        form = Form(req.POST)
        # фильтрация
        if form.is_valid():
            field = form.cleaned_data['choose_field']
            condition = form.cleaned_data['choose_condition']
            filter_value = form.cleaned_data['filter_value']
            records_num = form.cleaned_data['num_of_recs']
            
            for record in all_records: # если фильтр сброшен
                    record.visible = True
                    record.save()
            if field == '0' or condition == 'cond0':
                pass
            else:
                if field == '1': # Фильтр по названию
                    if condition == 'cond1': #условие "равно"
                        for record in all_records:
                            if record.name != filter_value:
                                record.visible = False
                                record.save()
                    if condition == 'cond2': #условие "содержит"
                        for record in all_records:
                            if not filter_value in record.name:
                                record.visible = False
                                record.save()
                    if condition == 'cond3': #условие "больше"
                        for record in all_records:
                            if record.name < filter_value:
                                record.visible = False
                                record.save()
                    if condition == 'cond4': #условие "меньше"
                        for record in all_records:
                            if record.name > filter_value:
                                record.visible = False
                                record.save()
                if field == '2': # Фильтр по количеству
                    filter_value=int(filter_value)
                    if condition == 'cond1': #условие "равно"
                        for record in all_records:
                            if record.number != filter_value:
                                record.visible = False
                                record.save()
                    if condition == 'cond2': #условие "содержит"
                        for record in all_records:
                            if not str(filter_value) in str(record.number):
                                record.visible = False
                                record.save()
                    if condition == 'cond3': #условие "больше"
                        for record in all_records:
                            if record.number <= filter_value:
                                record.visible = False
                                record.save()
                    if condition == 'cond4': #условие "меньше"
                        for record in all_records:
                            if record.number >= filter_value:
                                record.visible = False
                                record.save()
                if field == '3': # Фильтр по расстоянию
                    filter_value=int(filter_value)
                    if condition == 'cond1': #условие "равно"
                        for record in all_records:
                            if record.distance != filter_value:
                                record.visible = False
                                record.save()
                    if condition == 'cond2': #условие "содержит"
                        for record in all_records:
                            if not str(filter_value) in str(record.distance):
                                record.visible = False
                                record.save()
                    if condition == 'cond3': #условие "больше"
                        for record in all_records:
                            if record.distance <= filter_value:
                                record.visible = False
                                record.save()
                    if condition == 'cond4': #условие "меньше"
                        for record in all_records:
                            if record.distance >= filter_value:
                                record.visible = False
                                record.save()

            # Отображение опеределенного количества записей
            if records_num == 'num1':
                num_of_recs = 5
                TestTable.display_number = 5
            if records_num == 'num2':
                num_of_recs = 10
                TestTable.display_number = 10
            if records_num == 'num3':
                num_of_recs = 100
                TestTable.display_number = 100
            if records_num == 'num4':
                filtered_records = model.objects.filter(visible=True).values()
                return render(req, 'index.html', {'form':form, 'page_obj':filtered_records})
            else:
                filtered_records = model.objects.filter(visible=True)
                paginator = Paginator(filtered_records, num_of_recs)
                page_number = req.GET.get('page')
                if page_number == None:
                    page_number = 1
                page_obj = paginator.get_page(page_number)
                return render(req, 'index.html', {'page_obj': page_obj})

    else:
        form = Form()
        model = TestTable
        
        filtered_records = model.objects.filter(visible=True)
        
        page_number = req.GET.get('page')
        if page_number == None:
            num_of_recs = TestTable.rec_num(model)
            page_number = 1
        else:
            num_of_recs = TestTable.display_number
        paginator = Paginator(filtered_records, num_of_recs)
        page_obj = paginator.get_page(page_number)
        return render(req, 'index.html', {'form':form, 'page_obj':page_obj})
