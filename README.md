# Solar

Solar is a general purpose discord bot thats includes common discord bot commands, fun stuff, and statistics for various online games (currently only FFXIV). This project is just for fun for the most part, and so I can experience python and creating a discord bot.

## Testing 

To test new commands, just run `python3 testbot.py` to run up the dummy bot and run the commands in the test server.

# Release Process

1. Run through all of the pr's and mark them as either enhancment, bug, or maintenance.
2. Change the future release to whatever the next release is
3. Make a new branch called "x.y.z release_prep"
4. On the new branch, run `github_changelog_generator` to update the change log, check it's okay
5. Tag the commit with the version, i.e `git tag -a x.y.z` and push
6. Make a new pull request of this branch into release.
7. Merge.
8. Back merge the release branch into master