from github import Github

# First, create an authenticated Github instance
g = Github('<YOUR_GITHUB_ACCESS_TOKEN>')

# Replace <YOUR_GITHUB_ACCESS_TOKEN> with your actual access token
# You can create a personal access token at https://github.com/settings/tokens

# Next, specify the repository and user
user = g.get_user('<YOUR_GITHUB_USER>')
repo = user.get_repo('<YOUR_GITHUB_REPO>')

print("Total branches: ", repo.get_branches().totalCount)

deactivated_users = ['user 1', 'user 2']

# Loop through all branches in the repository and delete them
for branch in repo.get_branches():
    branch_name = branch.name
    if branch.commit.committer is not None:
        branch_owner = branch.commit.committer.login
        if branch_owner in deactivated_users:
            print(f"Found a deactivated user branch: {branch_name} (owned by {branch_owner})")
            # Delete the branch
            repo.get_git_ref(f"heads/{branch_name}").delete()
            print(f"branch: {branch_name} deleted...")
    else:
        print(f"{branch_name} has no owner")

