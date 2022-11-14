from django.contrib import admin
from .models import Employee, WorkProject, Passport, Client, VIPClient, Membership

admin.site.register(Employee)
admin.site.register(WorkProject)
admin.site.register(Passport)
admin.site.register(Client)
admin.site.register(VIPClient)
admin.site.register(Membership)


