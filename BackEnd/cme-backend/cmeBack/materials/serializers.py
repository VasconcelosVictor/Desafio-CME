from rest_framework import serializers
from .models import  Materiais
from dateutil import parser

class MateriaisSerializer(serializers.ModelSerializer):
    # data = serializers.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Materiais
        fields = '__all__'

    # def validate_data(self, value):
    #     try:
    #         # Parse a data no formato brasileiro
    #         value = parser.parse(value, dayfirst=True)
    #     except ValueError:
    #         raise serializers.ValidationError("Formato de data inválido. Use DD/MM/AAAA.")
    #     return value