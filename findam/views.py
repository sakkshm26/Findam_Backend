from .models import Cs,Blockchain,Electronics,Entrepreneurship,Web3
from .serializers import CsSerializer,BlockchainSerializer,ElectronicsSerializer,EntrepreneurshipSerializer,Web3Serializer
from rest_framework import viewsets
# Create your views here.

class CsModelViewSet(viewsets.ModelViewSet):
    queryset = Cs.objects.all()
    serializer_class = CsSerializer

class BlockchainModelViewSet(viewsets.ModelViewSet):
    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer

class ElectronicsModelViewSet(viewsets.ModelViewSet):
    queryset = Electronics.objects.all()
    serializer_class = ElectronicsSerializer

class EntrepreneurshipModelViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneurship.objects.all()
    serializer_class = EntrepreneurshipSerializer

class Web3ModelViewSet(viewsets.ModelViewSet):
    queryset = Web3.objects.all()
    serializer_class = Web3Serializer