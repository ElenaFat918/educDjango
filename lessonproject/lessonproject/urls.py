"""
URL configuration for lessonproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('lessonapp.urls')),
    path('les3/', include('myapp3.urls')),
    # path('', index('myapp3.urls')),
    path('les4/', include('myapp4.urls')),
]

"""
● Импортируется модуль admin из пакета django.contrib. 
С встроенной админкой мы будем работать в рамках курса. 
● Импортируется функция path и модуль include из пакета django.urls. 
Обе функции нужны для формирования url адресов, на которые будет отвечать сервер 
● Создается список urlpatterns, который будет содержать маршруты (routes) для обработки URL-адресов. 
● Добавляется маршрут для административной панели Django, который будет обрабатывать URL-адрес, 
начинающийся с префикса "admin/" и передавать управление в модуль admin.site.urls. 
● Добавляется маршрут для приложения myapp, который будет обрабатывать пустой URL-адрес 
и передавать управление в модуль myapp.urls. Маршрут включается с помощью функции include. 

Добавляется маршрут для приложения myapp3, который будет обрабатывать
URL-адрес les3 в качестве префикса. В случае его совпадения передавать
управление в модуль myapp3.urls. Маршрут включается с помощью функции include,
а дальнейшая обработка адреса происходит в urls.py приложения. 
"""
