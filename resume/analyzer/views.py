from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ResumeSerializer
from .validators import validate_resume
from .analyzer_service import analyze_resume


class ResumeUploadView(APIView):

    def post(self, request):
        uploaded_file = request.FILES.get("file")

        valid, message = validate_resume(uploaded_file)

        if not valid:
            return Response(
                {
                    "success": False,
                    "message": message,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():

            resume = serializer.save()

            analysis = analyze_resume(
                resume.file.path # type: ignore
            )

            return Response(
                {
                    "success": True,
                    "message": "Resume uploaded and analyzed successfully.",
                    "data": serializer.data,
                    "analysis": analysis,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )