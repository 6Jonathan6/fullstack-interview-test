from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .utils import git_wrapper
# Create your views here.


class BranchesList(viewsets.ViewSet):
    """
        List  all branches in the repository
    """

    def list(self, request):
        return Response(git_wrapper.get_branches())
