from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TokenSerializer
from .models import Token

# Create your views here.

class ReciveToken(APIView):
    def post(self, request):
        try:
           token = request.data.get('token')
           unique_Id = request.data.get('unique_Id')
           if Token.objects.filter(token=token).exists():
               return Response({'error': 'El token ya existe en la base de datos'}, status=400)
           data = {'token': token, 
                   'unique_Id': unique_Id
                   }
           serializer = TokenSerializer(data=data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           else:
               return Response(serializer.errors, status=400)
        except KeyError:
            return Response({'error': 'El Token es requerido'}, status=400)
    def get(self, request):
        tokens = Token.objects.all()
        serializer = TokenSerializer(tokens, many=True)
        return Response(serializer.data)

class SendToken(APIView):
    def get(self, request, unique_id):
        # unique_id = request.query_params.get('unique_id')
        print(unique_id)
        if not unique_id:
            return Response({'error': 'El parametro unique_id es requerido'}, status=400)
        token = Token.objects.filter(unique_Id=unique_id).first()
        if not token:
            return Response({'error': 'Token no encontrado'}, status=404)
        serializer = TokenSerializer(token)
        return Response(serializer.data)
        

