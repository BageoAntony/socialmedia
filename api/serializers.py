
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import post,comment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class commentSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    question=serializers.CharField(read_only=True)
    votecount=serializers.CharField(read_only=True)
    class Meta:
        model=comment
        fields=["id","question","answer","user","created_date","votecount"]
    
    def create(self,validated_data):
        ques=self.context.get("question")
        usr=self.context.get("user")
        return ques.answers_set.create(user=usr,**validated_data)


class postSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    question_answers=commentSerializer(read_only=True,many=True)
    
    class Meta:
        model=post
        fields=[
            "id",
            "title",
            "description",
            "image",
            "user",
            "question_answers"
        ]