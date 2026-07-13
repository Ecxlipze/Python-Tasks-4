from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeSerializer
from .validators import validate_resume

class ResumeUploadView(APIView):

    def post(self, request):
        uploaded_file = request.FILES.get("file")
        valid, message = validate_resume(uploaded_file)

        if not valid:
            return Response(
                {"success": False, "message": message},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Resume uploaded successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )