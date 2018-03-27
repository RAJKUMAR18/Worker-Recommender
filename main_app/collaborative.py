from django.db import models
import  pickle
from .models import ClientRatings, WorkerRatings

class ClientRatesWorker(models.Model):
    def __init__(self):
        pass

    def get_worker_rating(self):
        pass

    def set_worker_rating(self):
        pass

class WorkerRatesCLient(models.Model):
    def __init__(self):
        pass

    def get_client_rating(self):
        pass

    def set_client_rating(self):
        pass

class InitializeModel(models.Model):
    def __init__(self):
        print('Initializing models')
        self.clientsratingbyworker()
        self.workersratingbyclient()

    def pickler(self, toBeDumped, filename):
        with open(str(filename) + '.pkl', 'wb') as file:
            file.write(pickle.dumps(toBeDumped))

    def unpickleLoader(self, filename):
        with open(filename + '.pkl', 'rb') as f:
            unpickled = pickle.loads(f.read())
        return unpickled

    def clientsratingbyworker(self):
        print('clientsraitingbyworker')
        clientsrating = self.unpickleLoader('workerratesclients')
        for i in range(len(clientsrating)):
            temp = ClientRatings()
            temp.worker_id = clientsrating[i][0]
            temp.clientID1 = clientsrating[i][1]
            temp.clientR1 = clientsrating[i][2]
            temp.clientID2 = clientsrating[i][3]
            temp.clientR2 = clientsrating[i][4]
            temp.clientID3 = clientsrating[i][5]
            temp.clientR3 = clientsrating[i][6]
            temp.clientID4 = clientsrating[i][7]
            temp.clientR4 = clientsrating[i][8]
            temp.clientID5 = clientsrating[i][9]
            temp.clientR5 = clientsrating[i][10]
            temp.save()

    def workersratingbyclient(self):
        print('workersratingbyclient')
        workersrating = self.unpickleLoader('clientratesworkers')
        for i in range(len(workersrating)):
            temp = WorkerRatings()
            temp.client_id = workersrating[i][0]
            temp.workerID1 = workersrating[i][1]
            temp.workerR1 = workersrating[i][2]
            temp.workerID2 = workersrating[i][3]
            temp.workerR2 = workersrating[i][4]
            temp.workerID3 = workersrating[i][5]
            temp.workerR3 = workersrating[i][6]
            temp.workerID4 = workersrating[i][7]
            temp.workerR4 = workersrating[i][8]
            temp.workerID5 = workersrating[i][9]
            temp.workerR5 = workersrating[i][10]
            temp.save()

def main():
    initiaze = InitializeModel()

if __name__ == '__main__':
    main()
