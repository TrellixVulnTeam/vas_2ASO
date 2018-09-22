# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import Otp
import requests
import textwrap


# Create your views here.
def detail(request):
    param1 = request.GET.get('otpId')
    param2 = request.GET.get('statusId')
    param3 = request.GET.get('recipient')

    Otp.objects.create(otpId=param1, statusId=param2, recipient=param3)

    return HttpResponse('درخواست با موفقیت ثبت شد.')


def data(request):
    otps = Otp.objects.all()
    otp_ids = list()

    for otp in otps:
        otp_ids.append(otp.otpId)

    response_html = '<br>'.join(otp_ids)

    return HttpResponse(response_html)


def push_otp(request):
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/">
<soap:Header/>
<soap:Body>
<tem:XmsRequest>
<!--Optional:-->
<tem:requestData><![CDATA[<xmsrequest>
<userid>59344</userid>
<password>Gx6yJrRk!T0p</password>
<action>PushOtp</action>
<body>
<serviceid>680</serviceid>
<recipient mobile="PHONE_NUMBER" originator="405002" cost="COST_NUMBER"></recipient>
</body>
</xmsrequest>]]></tem:requestData>
</tem:XmsRequest>
</soap:Body>
</soap:Envelope>'''

    headers = {"Content-Type": "text/xml"}

    param1 = request.GET.get('mobile')
    param2 = request.GET.get('cost')

    return HttpResponse(requests.post('http://ws.smartsms.ir/sms.asmx',
                                      data=xml.replace('PHONE_NUMBER', param1).replace('COST_NUMBER', param2),
                                      headers=headers))


def charge_otp(request):
    xml = '''<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/">
<soap:Header/>
<soap:Body>
<tem:XmsRequest>
<!--Optional:-->
<tem:requestData><![CDATA[<xmsrequest>
<userid>59344</userid>
<password>Gx6yJrRk!T0p</password>
<action>chargeotp</action>
<body>
<serviceid>680</serviceid>
<recipient mobile="PHONE_NUMBER" originator="405002" pin="PIN_CODE">OTP_ID</recipient>
</body>
</xmsrequest>]]></tem:requestData>
</tem:XmsRequest>
</soap:Body>
</soap:Envelope>
'''

    headers = {"Content-Type": "text/xml"}

    param1 = request.GET.get('mobile')
    param2 = request.GET.get('pin')
    param3 = request.GET.get('otpid')

    return HttpResponse(requests.post('http://ws.smartsms.ir/sms.asmx',
                                      data=xml.replace('PHONE_NUMBER', param1).replace('PIN_CODE', param2).replace(
                                          'OTP_ID', param3), headers=headers))
