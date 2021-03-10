from django.http import JsonResponse
from rest_framework.decorators import api_view
import dataworkshop.findout.QueryRunner as QueryRunner
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def home(request):
    search = request.data['query']
    runner = QueryRunner.QueryRunner(search)

    data = runner.run()
    return Response(data)