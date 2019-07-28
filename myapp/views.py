from django.shortcuts import render

def home(request):
    active = 'home'
    context = {'active':active}
    return render(request, 'home.html', context)

def people(request):
    active = 'people'
    context = {'active':active}
    return render(request, 'people.html', context)

def people2(request):
    active = 'people2'
    context = {'active':active}
    return render(request, 'people2.html', context)

def people3(request):
    active = 'people3'
    context = {'active':active}
    return render(request, 'people3.html', context)

def seoul(request):
    active = 'seoul'
    context = {'active':active}
    return render(request, 'region/seoul.html', context)

def jeju(request):
    active = 'jeju'
    context = {'active':active}
    return render(request, 'region/jeju.html', context)

def company(request):
    active = 'company'
    context = {'active':active}
    return render(request, 'company.html', context)

def recruit(request):
    active = 'recruit'
    context = {'active':active}
    return render(request, 'recruit.html', context)

def companyinfo(request):
    active = 'recruit'
    context = {'active':active}
    return render(request, 'companyinfo.html', context)