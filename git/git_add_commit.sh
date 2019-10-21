# -----------------------------------------------------------------------------
# @title         git Adding/Committing Snippets
# @brief         Commands and Examples for Adding, Un-Adding, Committing, and
#                  Dealing with version control of Text-file Changes.
# @author.name   Tommy Vegetables
# @author.email  leafyrabbet@gmail.com
# -----------------------------------------------------------------------------


# Get the Repo (Branch) Status (includes new files, modified files, and added
#  files). Note that anything excluded by a `.gitignore` will not show-up at
# all, ever.
git status


# Show all the differences between the unstaged ("not `add`-ed") modifications
#  for all tracked files and their state in the local checked-out branch.
git diff


# Show all the differences between the staged modifications and the state of
#  the modified files as committed into the local checked-out branch.
git diff --cached


# Stage (add) a file in its current state to the pre-commit staging "area"
git add ./<path_to_subdirectoy_file>/<filename>


# Stage all current modifications to the pre-commit staging "area"
git add .


# Unstage all currently staged modifications
git reset


# Replace current state of a Working Tree (local) file with the checked-in
#   state from the local (current) branch's index.
git restore ./<path_to_subdirectory_file/<filename>


# (Alternative) Replace the current state of a Working Tree (local) file
#   with the newest checked-in (committed) state from the local (current)
#   branch's index.
git checkout ./<path_to_subdirectory_file/<filename>


# Commit all modifications in the pre-commit staging "area" as a single, new
#   history point in the repository's index for the current branch (the
#   configured commit-message editor will open and the saved message will be
#   sent with the changes as the commit message logged at the new history
#   point in the index).
git commit


# Commit all modifications in the pre-commit staging "area" as a single, new
#   history point in the repository's index for the current branch with the
#   given message.
git commit -m "<Commit message goes here.>"


# Create and switch-to a new branch before staging any modifications, so that
#   your dev-work can be easily tracked in a short-lived, parallel branch.
git checkout -b <new_branch_topic>/<new_branch_name>

