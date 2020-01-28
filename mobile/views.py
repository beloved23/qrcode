from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Download, HbbActivation, Agent, Product, Url
from django.conf import settings
import json
import base64


def get_device_url(os_type, app_type):
    url_obj = Url.objects.get(product=app_type)
    download_url = getattr(url_obj, os_type.lower(), 'android_url')
    return download_url


class Webairtel(View):

    def get(self, requests):
        """
        :param requests:
        :return:
        """
        influencer = requests.GET['influencer']
        decoded_info = "Airtel"
        final_url = "http://download.airtel.ng/checkinfluencer/?anchor=" + influencer
        return HttpResponseRedirect(final_url)


class Airtel(View):

    def get(self, requests):
        """
        :param requests:
        :return:
        """
        context = dict()
        ua = requests.META['HTTP_USER_AGENT']
        msisdn = requests.META.get('x-up-calling-line-id',None)
        device = ""
        if requests.Windows or requests.Linux:
            device = "Windows"
        if requests.Android:
            device = "Android"   
        if requests.iPhone  or requests.iPad:
            device = "iOS"
        if requests.iMac :
            device = "Mac"
        influencer = requests.GET['anchor']
        app = requests.GET.get('app', 'selfcare')
        print(app)
        decoded_info = "Airtel"
        if influencer:
            decoded_info = base64.b64decode(influencer)
        context['influencer'] = influencer
        app = requests.GET.get('app', 'selfcare')
        context['app'] = app
        product = Product.objects.get(name=app.lower())
        if msisdn is None or len(msisdn) < 10:
            return render(requests,'airtel/enter_msisdn.html',context)
        device_type_url = get_device_url(device, product) #DEVICE['%s_%s' % (app,device)]
        res = Download.objects.create(msisdn=msisdn,device=device,influencer=str(decoded_info), app=product)
        if msisdn:
            res.msisdn = msisdn
            res.status = True
        else:
            res.msisdn = "NA"
            res.status = False
        res.save()
        data = {}
        return HttpResponseRedirect(device_type_url)


# class EnterMsisdn(View):
#
#     def get(self, request):
#         app = request.GET.get('app', 'selfcare')
#         context = dict()
#         context['app'] = app
#         return render(request,'airtel/enter_msisdn.html', context)
#
#     def post(self, request):
#         msisdn = request.POST.get('msisdn', None)
#         if msisdn is not None:
#             device = ""
#             if request.Windows or request.Linux:
#                 device = "Windows"
#             if request.Android:
#                 device ="Android"
#             if request.iPhone or request.iPad:
#                 device = "iOS"
#             if request.iMac:
#                 device = "Mac"
#             influencer = request.POST.get('influencer', None)
#             decoded_info = "Airtel"
#             app = request.POST.get('app', 'selfcare')
#             if influencer:
#                 decoded_info = base64.b64decode(influencer)
#             product = Product.objects.get(name=app.lower())
#             device_type_url = get_device_url(device, product)
#             msisdn = '234%s' % msisdn[-10:]
#             if msisdn is None or len(msisdn) < 10:
#                 context = dict()
#                 context['app'] = app
#                 return render(request, 'airtel/enter_msisdn.html', context)
#             res = Download.objects.create(device=device, msisdn=msisdn, influencer=str(decoded_info), app=product)
#             if msisdn:
#                 res.msisdn = msisdn
#                 res.status = True
#             else:
#                 res.msisdn = "NA"
#                 res.status = False
#             res.save()
#             data = {}
#             return HttpResponseRedirect(device_type_url)
#         else:
#             return redirect('enter_msisdn')
                
