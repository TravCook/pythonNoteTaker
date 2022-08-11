from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import NotesSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from noteTaker.models import Users, Notes
from noteTaker.serializers import UserSerializer, NotesSerializer

# Create your views here.
@csrf_exempt
def noteApi(request):
    #gets all notes
    if request.method=='GET':
        notes = Notes.objects.all()
        notes_serializer = NotesSerializer(notes, many=True)
        return JsonResponse(notes_serializer.data, safe=False)
    elif request.method=='POST':
        note_data=JSONParser().parse(request)
        notes_serializer = NotesSerializer(data=note_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse("Note Added", safe=False)
        return JsonResponse("Note Failed to Add", safe=False)
    elif request.method=='PUT':
        note_data = JSONParser().parse(request)
        note = Notes.objects.get(noteID=note_data['noteID'])
        notes_serializer=NotesSerializer(note, data=note_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse("Note Updated", safe=False)
        return JsonResponse("Failed to update note", safe=False)
    elif request.method =='DELETE':
        note=Notes.objects.get(noteID=id)
        note.delete()
        return JsonResponse("Deleted Note", safe=False)