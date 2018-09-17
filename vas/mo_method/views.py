from django.shortcuts import render
from django.http import HttpResponse
from .models import Mo


# Create your views here.
def detail(request):
    param1 = request.GET.get('text')
    param2 = request.GET.get('from')
    param3 = request.GET.get('to')
    param4 = request.GET.get('smsId')
    param5 = request.GET.get('userid')

    Mo.objects.create(text=param1, fromKey=param2, to=param3, smsId=param4, userid=param5)

    return HttpResponse('درخواست با موفقیت ثبت شد.')


def data(request):
    mos = Mo.objects.all()
    mo_texts = list()

    for mo in mos:
        mo_texts.append(mo.text)

    response_html = '<br>'.join(mo_texts)

    return HttpResponse(response_html)
