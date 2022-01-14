from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from .utils import git_wrapper
from .serializers import PullRequestSerializerCreate, PullRequestSerializerUpdate
from .models import PullRequestModel
from django.http import Http404
import sys

# Create your views here.


class BranchesList(viewsets.ViewSet):
    """
        List  all branches in the repository
    """

    def list(self, request):
        pk = request.GET.get('pk')
        if(pk):
            return self.retrieve(request, pk)
        return Response(git_wrapper.get_branches())

    def retrieve(self, request, pk):
        try:
            print('skopfajsdfjadio', pk)
            print(request)
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


class PullRequest(viewsets.ModelViewSet):
    serializer_class = PullRequestSerializerCreate
    queryset = PullRequestModel.objects.all()

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            serializer_class = PullRequestSerializerUpdate
        return serializer_class
