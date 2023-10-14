from rest_framework import viewsets, permissions
from .serializers import DictionarySerializer


class DictionaryView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DictionarySerializer

    def get_queryset(self):
        user = self.request.user

        # .model Dictionary related name
        return user.dictionaries.all()
