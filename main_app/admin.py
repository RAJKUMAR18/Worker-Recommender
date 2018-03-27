from django.contrib import admin

# Register your models here.
from main_app.models import ClientRatings, WorkerRatings

admin.site.register(ClientRatings)
admin.site.register(WorkerRatings)
