from django.shortcuts import render
from django.http import HttpResponse
from .models import Sub


# Create your views here.
def detail(request):
    param1 = request.GET.get('text')
    param2 = request.GET.get('keyword')
    param3 = request.GET.get('channel')
    param4 = request.GET.get('from')
    param5 = request.GET.get('to')
    param6 = request.GET.get('NotificationId')
    param7 = request.GET.get('userid')

    Sub.objects.create(text=param1, keyword=param2, channel=param3, fromKey=param4, to=param5, NotificationId=param6,
                       userid=param7)

    return HttpResponse('درخواست با موفقیت ثبت شد.')


def data(request):
    subs = Sub.objects.all()
    subs_text = list()

    for sub in subs:
        subs_text.append(sub.text)

    response_html = '<br>'.join(subs_text)

    return HttpResponse(response_html)
