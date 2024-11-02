from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Turn
from .serializers import TurnSerializer
from django.contrib.auth.models import User


class AsignarTurnView(generics.CreateAPIView):
    serializer_class = TurnSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        usuarios = User.objects.all()
        ultimo_turn = Turn.objects.last()
        if ultimo_turn:
            ultimo_usuario = ultimo_turn.usuario
            siguiente_usuario = usuarios[(list(usuarios).index(
                ultimo_usuario) + 1) % len(usuarios)]
        else:
            siguiente_usuario = usuarios.first()

        turn = Turn.objects.create(usuario=siguiente_usuario)
        serializer = self.get_serializer(turn)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListaTurnsView(generics.ListAPIView):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer
    permission_classes = [IsAuthenticated]
