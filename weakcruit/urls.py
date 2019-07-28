from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
    path('people/', myapp.views.people, name="people"),
    path('people2/', myapp.views.people2, name="people2"),
    path('people3/', myapp.views.people3, name="people3"),
    path('people/seoul/', myapp.views.seoul, name="seoul"),
    path('people/jeju/', myapp.views.jeju, name="jeju"),
    path('company/', myapp.views.company, name="company"),
    path('recruit/', myapp.views.recruit, name="recruit"),
    path('companyinfo/', myapp.views.companyinfo, name="companyinfo"),
]
