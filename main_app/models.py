from django.db import models
import csv
# Create your models here.
class ClientRatings(models.Model):
    worker_id = models.IntegerField()

    clientID1 = models.IntegerField()
    clientR1 = models.IntegerField()

    clientID2 = models.IntegerField()
    clientR2 = models.IntegerField()

    clientID3 = models.IntegerField()
    clientR3 = models.IntegerField()

    clientID4 = models.IntegerField()
    clientR4 = models.IntegerField()

    clientID5 = models.IntegerField()
    clientR5 = models.IntegerField()


class WorkerRatings(models.Model):
    client_id = models.IntegerField()

    workerID1 = models.IntegerField()
    workerR1 = models.IntegerField()

    workerID2 = models.IntegerField()
    workerR2 = models.IntegerField()

    workerID3 = models.IntegerField()
    workerR3 = models.IntegerField()

    workerID4 = models.IntegerField()
    workerR4 = models.IntegerField()

    workerID5 = models.IntegerField()
    workerR5 = models.IntegerField()
