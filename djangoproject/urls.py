"""djangoproject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from papers import views

# nq --> number of questions
urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoint 1 --> /mcq/board/subject/year/month/variant/nq
    path('mcq/<str:board>/<str:subject>/<str:year>/<str:month>/<str:variant>/<int:nq>/', views.getOnePaper.as_view()),

    # Endpoint 2 --> /mcq/board/subject/year/month/variant/question-number
    path('mcq/<str:board>/<str:subject>/<str:year>/<str:month>/<str:variant>/<int:question_number>/', views.getEndpointTwo.as_view()),

    # Endpoint 3 --> mcq/board/subject/topic/number-of-questions
    path('mcq/<str:board>/<str:subject>/<str:topic>/<int:nq>/', views.getEndpointThree.as_view()),

    # Endpoint 4 --> mcq/board/subject/number-of-questions
    path('mcq/<str:board>/<str:subject>/<int:nq>/', views.getEndpointFour.as_view())
    
]