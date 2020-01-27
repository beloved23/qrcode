from django.contrib import admin

# Register your models here.
from .models import Download, HbbActivation, Agent, Product, Url
# Register your models here.
from django.http import HttpResponse, HttpResponseRedirect
import csv


class DownloadAdmin(admin.ModelAdmin):
    list_display = ('msisdn', 'status', 'device', 'influencer', 'app', 'date_created')
    list_filter = ('status','app__name', 'device', 'date_created')
    search_fields = ('msisdn', 'influencer')
    actions = ['download_selected', ]

    def download_selected(self, request, queryset):
        headers = ['msisdn', 'status', 'device', 'influencer', 'date_created']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=Download.csv'
        writer = csv.writer(response)
        writer.writerow([header.upper() for header in headers])
        for obj in queryset:
            line = []
            for header in headers:
                line.append(getattr(obj, header))
            writer.writerow(line)
        return response


class HbbActivationAdmin(admin.ModelAdmin):
    list_display = ('msisdn', 'alter_msisdn', 'agent_msisdn', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('msisdn', 'alter_msisdn')
    actions = ['download_selected', ]

    def download_selected(self, request, queryset):
        headers = ['msisdn', 'alter_msisdn', 'agent_msisdn', 'date_created']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=HBBApp.csv'
        writer = csv.writer(response)
        writer.writerow([header.upper() for header in headers])
        for obj in queryset:
            line = []
            for header in headers:
                line.append(getattr(obj, header))
            writer.writerow(line)
        return response


class AgentAdmin(admin.ModelAdmin):
    list_display = ('msisdn', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('msisdn',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class UrlAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'android', 'ios', 'windows', 'mac')


admin.site.register(HbbActivation, HbbActivationAdmin)
admin.site.register(Download, DownloadAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Url, UrlAdmin)