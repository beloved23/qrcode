from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Download, HbbActivation, Agent, Product, Url
from django.conf import settings
import json
import base64
import redis
# from device_detector import DeviceDetector
# from device_detector import SoftwareDetector


AGENT_LIST = ['8022221569']


class LoginAirtel(View):
    def post(self, request):
        context = {}
        msisdn = request.POST['msisdn']
        if msisdn and len(msisdn) >= 10:
            try:
                Agent.objects.get(msisdn=msisdn[-10:])
                #if msisdn[-10:] in AGENT_LIST:
                #redirect("enter_hbb")
                request.session['agent'] = msisdn
                return redirect('enter_hbb')
            except Exception, ex:
                print str(ex)
                context.update({'message': 'Your phone number is not whitelisted'})
        else:
            context.update({'message': 'Wrong msisdn'})
        return render(request, 'airtel/agent_login.html', context)

    def get(self, request):
        """
        :param requests:
        :return:
        """
        # msisdn = requests.GET['hbb']
        # alt = requests.GET['alt']
        # if msisdn and alt:
        #     store = redis.Redis('172.24.2.68', password="8aB4wnwfn7Fj?ZB")
        #     store.sadd("HBB_SELF_CARE_KYC", '%s|%s' % (msisdn, alt))
        #     message ="Inserted"
        # else:
        #     message = "Enter hbb and alt number"
        if request.session.get('agent'):
            return redirect('enter_hbb')
        context = {}
        return render(request, 'airtel/agent_login.html', context)


class GoriAirtel(View):

    def post(self, request):
        context = {}
        msisdn = request.POST['msisdn']
        alt = request.POST['alt_msisdn']
        if msisdn and alt:
            if len(msisdn) and len(alt):
                store = redis.Redis('172.24.2.68', password="8aB4wnwfn7Fj?ZB")
                store.sadd("HBB_SELF_CARE_KYC", '%s|%s' % (msisdn, alt))
                agent = request.session['agent']
                HbbActivation.objects.create(msisdn=msisdn[-10:], alter_msisdn=alt[-10:], agent_msisdn=agent[-10:])
                context.update({'message': 'Request was successfull'})
        else:
            context.update({'message': 'Enter hbb and alt number'})
        return render(request, 'airtel/agent_activation.html', context)

    def get(self, request):
        """
        :param requests:
        :return:
        """
        if not request.session.get('agent'):
            return redirect('enter_login')
        context = {}
        return render(request, 'airtel/agent_activation.html', context)


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


class EnterMsisdn(View):

    def get(self, request):
        app = request.GET.get('app', 'selfcare')
        context = dict()
        context['app'] = app
        return render(request,'airtel/enter_msisdn.html', context)

    def post(self, request):
        msisdn = request.POST.get('msisdn', None)
        if msisdn is not None:
            device = ""
            if request.Windows or request.Linux:
                device = "Windows"
            if request.Android:
                device ="Android"
            if request.iPhone or request.iPad:
                device = "iOS"
            if request.iMac:
                device = "Mac"
            influencer = request.POST.get('influencer', None)
            decoded_info = "Airtel"
            app = request.POST.get('app', 'selfcare')
            if influencer:
                decoded_info = base64.b64decode(influencer)
            product = Product.objects.get(name=app.lower())
            device_type_url = get_device_url(device, product)
            msisdn = '234%s' % msisdn[-10:]
            if msisdn is None or len(msisdn) < 10:
                context = dict()
                context['app'] = app
                return render(request, 'airtel/enter_msisdn.html', context)
            res = Download.objects.create(device=device, msisdn=msisdn, influencer=str(decoded_info), app=product)
            if msisdn:
                res.msisdn = msisdn
                res.status = True
            else:
                res.msisdn = "NA"
                res.status = False
            res.save()
            data = {}
            return HttpResponseRedirect(device_type_url)
        else:
            return redirect('enter_msisdn')
                
