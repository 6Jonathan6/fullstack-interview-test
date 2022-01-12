from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .utils import git_wrapper
from django.http import Http404
import sys

# Create your views here.


class BranchesList(viewsets.ViewSet):
    """
        List  all branches in the repository
    """

    def list(self, request):
        return Response(git_wrapper.get_branches())

    def retrieve(self, request, pk):
        try:
            return Response(git_wrapper.get_commits_by_branch(pk))
        except Exception as e:
            error = sys.exc_info()
            print('e', error)
            if('fatal: bad revision' in str(error)):
                raise Http404()
            else:
                raise e


class CommitDetail(viewsets.ViewSet):
    """
        Shows files and author data of a commit
    """

    def retrieve(self, request, pk):
        try:
            return Response(git_wrapper.get_commit_by_sha(pk))
        except Exception as e:
            error = sys.exc_info()
            if('BadName' in str(error)):
                raise Http404()
            raise e
