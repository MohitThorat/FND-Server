from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from FNDRest.models import FakeText
from FNDRest.serializers import FNDSerializer,TextSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import textdistance

@api_view(['GET','POST'])
def faketext_list(request,format = None):
    """
    List all code fake messages, or create a new message.
    """
    if request.method == 'GET':
        faketexts = FakeText.objects.all()
        serializer = FNDSerializer(faketexts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FNDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
def faketext_detail(request, pk,format = None):
    """
    Retrieve, update or delete a fake message.
    """
    try:
        faketext = FakeText.objects.get(pk=pk)
    except FakeText.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FNDSerializer(faketext)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FNDSerializer(faketext, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        faketext.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def fakeTextDetect(request,format = None):

    serializer = TextSerializer(data = request.data)
    if serializer.is_valid():
        # print()
        # print(serializer)
        all_data = FakeText.objects.all()
        max_similarity = -1
        feedback_1 = ""
        feedback_2 = ""
        for data in all_data:
            similarity = textdistance.ratcliff_obershelp(serializer.data['fake_text'],data.fake_text)
            if max_similarity < similarity:
                max_similarity = similarity
                feedback_1 = data.feedback_one
                feedback_2 = data.feedback_two


        if max_similarity*100 > 60:
            #Most likely fake news.
            content = {'Description': 'Strong Likeley hood of fake news.', 'Feedback 1':feedback_1, 'Feedback 2': feedback_2}
            return Response(content,status=status.HTTP_200_OK)

        #Less likely fake news
        content = {'Description': 'Less Likeley hood of fake news.'}
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


