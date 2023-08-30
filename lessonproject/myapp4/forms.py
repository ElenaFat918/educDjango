from django import forms
import datetime

from django.core import mail


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)  # создаем поле для сохранения имени с макимальным к-вом букв 50
    email = forms.EmailField()  # создаем поле для хранения е-мейл
    age = forms.IntegerField(min_value=0,
                             max_value=120)  # создаем поле для хранения целого числа со значением от 0 до 120

    def clean_name(self):  # пользовательская валидация данных.
        """Плохой пример. Подмена параметра min_length."""
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Имя должно содержать не менее 3 символов')
            return name

    def clean_email(self):  # пользовательская валидация данных.
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or mail.endswith('corp.mail.ru')):
            raise forms.ValidationError('Используйте корпоративную почту')
            return email


"""
В методе clean_name() проверяется длина имени, и если она меньше трех символов,
то выбрасывается исключение ValidationError с соответствующим сообщением. Это
антипаттерн. Мы написали пять строк кода, которые делают тоже самое, что и
параметр min_length=3.
Для поля email встроенные механизмы Django проверяют, что введённый текст
похож на электронную почту, с собакой, точкой и т.п. Далее в методе clean_email()
мы проверяем окончание почты. Если оно не совпадает с одним из корпоративных
окончаний, выбрасывается соответствующее сообщение.
"""


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)  # текстовое поле ограничено 50 символами
    email = forms.EmailField()  # возраст должен быть не меньше 18
    age = forms.IntegerField(
        min_value=18)  # для поля is_active прописали отсутсвие “галочки” по умолчанию. Oбязательно прописывать для логического поля параметр required
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(
        initial=datetime.date.today)  # при вводе дня рождения нам заранее демонстрируется текущая дата
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F',
                                                        'Female')])  # выбор пола показывается как поле с выбором из двух вариантов. При этом пользователь видит Male и Female, а в переменную сохраняются M или F.


class ImageForm(forms.Form):
    image = forms.ImageField()


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    # позволяет использовать стили Bootstrap для оформления полей формы.
    # определяет текст-подсказку, отображаемый в поле формы до того, как пользователь введет данные.
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # позволяет использовать стили Bootstrap для оформления полей формы.
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # birthdate = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'class': 'form-control'}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # вручную поменяли тип поля на “дата”. Теперь браузер рисует кнопку календаря,дату можно выбирать, а не вводить
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    # вместо раскрывающегося списка у нас перечень значений с возможностью выбрать одно из них
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    # текст сообщения можно вводить в несколько строк.


"""       💡 Внимание! Можно не создавать новые представления, маршруты и
шаблон. Достаточно добавить строку импорта класса формы в views.py и
заменить старую форму на новую в представлении.
"""
