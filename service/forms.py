from django import forms

class Form (forms.Form):
    FIELD_CHOICES =(
        ("0", "----------"),
        ("1", "Название"),
        ("2", "Количество"),
        ("3", "Расстояние"),
    )
    CONDITION_CHOICES =(
        ('cond0', '--------'),
        ('cond1', 'равно'),
        ('cond2', 'содержит'),
        ('cond3', 'больше'),
        ('cond4', 'меньше'),
    )
    NUM_REC = (
        ('num1', '5'),
        ('num2', '10'),
        ('num3', '100'),
        ('num4', 'все')
    )

    choose_field = forms.ChoiceField (
        label='Выберите поле фильтрации', choices=FIELD_CHOICES, required=False)
    choose_condition = forms.ChoiceField (
        label='Выберите условие фильтрации', choices=CONDITION_CHOICES, required=False)
    filter_value = forms.CharField (label='Введите значение фильтра', required=False)
    num_of_recs = forms.ChoiceField (
        label='Количество отображаемых надписей', choices=NUM_REC, required=False)