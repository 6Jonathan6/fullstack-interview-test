from rest_framework import serializers
from .models import PullRequestModel
from .utils.git_wrapper import get_branches, merge_branches


def validate_branch_name(branch_name):
    branches = get_branches()
    if(branch_name in branches):
        return True
    else:
        raise serializers.ValidationError('Branch does not exist')


def open_pr_exists(pr_base_branch_name, pr_compare_branch_name):
    result = PullRequestModel.objects.filter(
        base_branch_name=pr_base_branch_name, compare_branch_name=pr_compare_branch_name, status='OP')
    if(result.count() > 0):
        raise serializers.ValidationError('An open pull request for these branches {compare_name} ---> {base_name} already exists'.format(
            base_name=pr_base_branch_name, compare_name=pr_compare_branch_name))


def has_commit_message(message):
    if(len(message) == 0):
        raise serializers.ValidationError(
            'Commit message cannot be empty in a MERGED pull request')


class PullRequestSerializer(serializers.ModelSerializer):
    base_branch_name = serializers.CharField(validators=[validate_branch_name])
    compare_branch_name = serializers.CharField(
        validators=[validate_branch_name])

    def create(self, validated_data):
        open_pr_exists(validated_data.get('base_branch_name'),
                       validated_data.get('compare_branch_name'))
        if(validated_data.get('status') == 'MR'):
            has_commit_message(validated_data.get("merge_commit_message"))
            merge_branches(validated_data.get('base_branch_name'),
                           validated_data.get('compare_branch_name'),
                           validated_data.get("merge_commit_message"))
        return PullRequestModel.objects.create(**validated_data)

    class Meta:
        model = PullRequestModel
        fields = ["id", "status", "base_branch_name",
                  "compare_branch_name", "created_at", "updated_at", "merge_commit_message"]
        read_only_fields = ['base_branch_name', "compare_branch_name"]
