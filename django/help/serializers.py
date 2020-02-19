from rest_framework import serializers

from help.models import Question, HelpContentImage


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('contents', 'id', 'title', 'created_at', 'updated_at')
        read_only_fields = ('id',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpContentImage
        fields = ('id', 'image')
