from rest_framework import viewsets
from help.serializers import QuestionSerializer, ImageSerializer
from help.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter()

    def perform_create(self, serializer):
        serializer.save()


class HelpImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save()
