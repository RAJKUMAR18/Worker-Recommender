from utils import BuildAndTrain
class ModelLoading():
    def __init__(self):
        bnt = BuildAndTrain()
        kneighborsOfUserQuery, finalCluster = bnt.modelling(service=service, userquery=vectorized_user_query)
