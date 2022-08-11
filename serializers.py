from rest_framework import serializers
from noteTaker.models import Users, Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = (
            "noteTitle",
            "noteBody",
            "noteID",
            "dateModified",
            "userID"
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "userID",
            "userName",
            "userPass"
        )