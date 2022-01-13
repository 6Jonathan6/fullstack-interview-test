from git import Repo

repo = Repo('.', search_parent_directories=True)


def get_branches():
    return [branch.name for branch in repo.branches]


def parse_file_stats(stats_dict):
    keys = stats_dict.keys()
    file_list = []
    for key in keys:
        file_list.append({**stats_dict[key], "file_name": key})
    return file_list


def parse_commit(raw_commit):
    return {
        "id": raw_commit.hexsha,
        "author": {
            "name": raw_commit.author.name,
            "email": raw_commit.author.email
        },
        "datetime": raw_commit.authored_datetime.isoformat(),
        "message": raw_commit.message.strip(),
        "short_sha": repo.git.rev_parse(raw_commit.hexsha, short=True),
        "total_stats": raw_commit.stats.total,
        "files_stats": parse_file_stats(raw_commit.stats.files)
    }


def get_commits_by_branch(branch_name, max_count=5000):
    commits = repo.iter_commits(branch_name, max_count=max_count)

    return list(map(parse_commit, commits))


def get_commit_by_sha(commit_sha):
    return parse_commit(repo.commit(commit_sha))


def get_branch_by_name(branch_name):
    return repo.branches[branch_name]


def merge_branches(base_branch_name, compare_branch_name, merge_message):
    prev_branch = repo.active_branch
    print('finallysdsd', merge_message)
    compare_branch = get_branch_by_name(compare_branch_name)
    repo.git.checkout(base_branch_name)
    repo.git.merge(compare_branch, no_ff=True, m=merge_message)
    repo.git.checkout(prev_branch)
