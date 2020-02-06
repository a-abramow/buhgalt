# from rest_framework.generics import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import viewsets
from .models import Wallet
from .serializers import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
