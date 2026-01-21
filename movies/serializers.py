from django.db.models import Avg
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
      rate = serializers.SerializerMethodField(read_only=True)

      class Meta:
            model = Movie
            fields = '__all__'

      def get_rate(self, obj):
            rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]

            return round(rate, 1) if rate is not None else None

      def validate_release_date(self, value):
            if value.year < 1900:
                  raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
            return value
      
      def validate_resume(self, value):
            if len(value) > 500:
                  raise serializers.ValidationError("Resumo não deve ter mais de 200 caracteres.")
            return value
      