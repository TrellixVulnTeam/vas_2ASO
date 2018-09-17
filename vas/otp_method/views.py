from django.shortcuts import render
from django.http import HttpResponse
from .models import Otp
import textwrap


# Create your views here.
def detail(request):
    param1 = request.GET.get('otpId')
    param2 = request.GET.get('statusId')
    param3 = request.GET.get('receipient')

    Otp.objects.create(otpId=param1, statusId=param2, receipient=param3)

    return HttpResponse('درخواست با موفقیت ثبت شد.')


def data(request):

    otps = Otp.objects.all()
    otp_ids = list()

    for otp in otps:
        otp_ids.append(otp.otpId)

    response_html = '<br>'.join(otp_ids)

    return HttpResponse(response_html)


