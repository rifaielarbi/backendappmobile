from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.core.mail import send_mail
from .serializers import SupportRequestSerializer

class SupportRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = SupportRequestSerializer(data=request.data)
        if serializer.is_valid():
            
            support_request = serializer.save(user=request.user)

        
            send_mail(
                subject=f"[Support] {support_request.subject}",
                message=f"Message de {request.user.username} :\n\n{support_request.message}",
                from_email=' topen.for.working@gmail.com',
                recipient_list=[' topen.for.working@gmail.com'],  
                fail_silently=False,
            )

            return Response({
                'success': True,
                'message': 'Votre message a été envoyé et enregistré avec succès.'
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

