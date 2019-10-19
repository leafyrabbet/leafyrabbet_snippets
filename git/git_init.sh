# -----------------------------------------------------------------------------
# @title         git Initialisation Snippets
# @brief         Unix Shell (bash) Snippets for Initialising New or Cloned
#                  git (or GitHub) repositories locally on a PC or Server.
# @author.name   Tommy Vegetables
# @author.email  leafyrabbet@gmail.com
# -----------------------------------------------------------------------------


# Checkout a Repo from GitHub using SSH
cd <parent_directory_for_checkout>
git clone git@github.com:<user_account>/<repo_name>.git


# Create a New Repo from Scratch
cd <parent_directory_for_checkout>
mkdir ./<repo_directory_name>
cd ./<repo_directory_name>
git init
git config user.name "Tommy Vegetables"
git config user.email "leafyrabbet@gmail.com"
git checkout -b trunk  # Change main branch name
touch .gitignore
git add ./.gitignore
git commit
# Commit Message (Title and Body):
#   Initialised Repo with gitignore
#   
#   - Created new repository
#   - Switched `HEAD` to New Branch: `trunk`
#   - Deleted default `HEAD` branch
#   - Added empty `.gitignore`
#   - Initial Commit
#


# Initialize git User for Commit "Signing"
git config user.name "Tommy Vegetables"
git config user.email "leafyrabbet@gmail.com"


# Config OniVim2 as your Commit Message Editor (Globally)
git config --global core.editor "onivim -f $1 > /dev/null; reset;"


# Make sure you're sync-ed Locally and with Remotes
git fetch --prune


# Configure (and Create if does not yet exist) the .gitignore
touch ./.gitignore
<editor> .gitignore


# Clone and Push a Local Repo to a new GitHub Repo
cd <local_git_repository>
curl -u <github_username> \
     -H "Content-Type: application/json" \ 
     -d '{"name":"<new_remote_repo_name>"}' \
	 https://api.github.com/user/repos
# Respond to Password Prompt for <github_username>
# Note: If you're using 2FA on GitHub, you need to get one
#   of your valid 6-digit tokens and add:
#   X-GitHub-OTP: <six_digit_token>
#   as a line in the header (-H) for the curl request
git remote add github git@github.com:<github_username>/<new_remote_repo_name>.git
# Note: `github` is the Remote Name, you can customise it to
#  whatever valid text you want; normally it is `origin`
git stash
git checkout trunk
git push -u github trunk

