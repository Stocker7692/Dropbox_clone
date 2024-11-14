# files/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse, Http404
from .models import File
from .serializers import FileSerializer

@api_view(['GET', 'POST'])
def file_list_upload(request):
    if request.method == 'GET':
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        file_obj = File(
            name=file.name,
            file=file,
            content_type=file.content_type,
            size=file.size
        )
        file_obj.save()
        serializer = FileSerializer(file_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def file_download(request, pk):
    try:
        file_obj = File.objects.get(pk=pk)
    except File.DoesNotExist:
        raise Http404("File not found")

    return FileResponse(file_obj.file, as_attachment=True, filename=file_obj.name)
