from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .models import TestObject
from django.db import transaction
import threading


#API for long running task
class Task(APIView):
    stop = False


    def get(self, request):

        def work():
            transaction.set_autocommit(False)
            for i in range(1, 100000):
                TestObject.objects.create(name='Pranjal', phone='9874563211')   #create operation on model
            if not Task.stop:
                transaction.commit()   #save operations only when task is not interrupted

        thread = threading.Thread(target=work)
        thread.start()

        return Response("Started", HTTP_200_OK)

#API for stopping task
class StopTask(APIView):
    def get(self, request, *args, **kwargs):
        Task.stop = True
        return Response("Stopped", HTTP_200_OK)



