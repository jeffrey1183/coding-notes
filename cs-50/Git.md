Git and Github is an entrance to know the field of computer science. It's practical, basic and necessary knowledge.

Git is a version control software you can maintain multiple versions of your software. People will use it not only for versioning their code and for collaborating with others.

Watching this [video](https://www.youtube.com/watch?v=1u2qu-EmIRc) and doing it step-by-step is the best practice to learn Git. Here is the list to review them when you forget particular part.

# Basic Commands
* [Create a Github repository](https://youtu.be/1u2qu-EmIRc?t=700)
 * [git clone](https://youtu.be/1u2qu-EmIRc?t=748)and basic commands like cd, ls and touch. 
 * [git add](https://youtu.be/1u2qu-EmIRc?t=904)
   * `git add *` and `git add -A`is a convenient command to track all of files.
 * [git commit](https://youtu.be/1u2qu-EmIRc?t=971)
 * [git commit -am]
   * Add all of files that I've changed that I've already been tracking and commit them at the same time.  
 * [git status](https://youtu.be/1u2qu-EmIRc?t=1065)
 * [git push](https://youtu.be/1u2qu-EmIRc?t=1120)
 * [git pull](https://youtu.be/1u2qu-EmIRc?t=1202)
 * [merge conflict](https://youtu.be/1u2qu-EmIRc?t=1416)
 * [git log](https://youtu.be/1u2qu-EmIRc?t=1653)
 * [git reset](https://youtu.be/1u2qu-EmIRc?t=1673)
 * [git reflog](https://youtu.be/1u2qu-EmIRc?t=1857)

# Git Flow - Collaborate with other egineers
Start to know the workflow when you cowork withr other engineers
* Engineers can work in different branches separately. There are [master and feature branch.](https://youtu.be/XQs5KcUj-Do?t=162). The git commits and logs are seperate. HEAD refers to where we currently are in the repository.
* [git branch](https://youtu.be/XQs5KcUj-Do?t=449), if we don't have anything after it, just shows us all of the branches that we currently have. If we have git branch followed by the name of a branch, that creates a new branch.
* Change to other branch by [git checkout](https://youtu.be/XQs5KcUj-Do?t=516)
* Check the changes you in a particular branch by git log command.
* Combine with two different branches together by [git merge](https://youtu.be/XQs5KcUj-Do?t=577).
* [Deal with the situation when I want to git push but the Github only has the master branch but my computer has feature and master branch.](https://youtu.be/XQs5KcUj-Do?t=767)
* On the front end, the default branch that Github using is the master branch.
* [Remote](https://youtu.be/XQs5KcUj-Do?t=1043) is some version of the repository that exists on GitHub.
 * git fetch means going to the remote and online version of the repository and downloading all of the latest commits.
 * git pull is the process of downloading the latest commits and move myself to the latest commit based on the master branch.
 * Create a [fork](https://youtu.be/XQs5KcUj-Do?t=1227) of repository means that we have a version of the repository that belongs to you. You can do whatever you want to it and all of that won't affect the original version of the repository. Open source project is an good example. Contributors fork the repository and make their necessary changes to their own version.
 * [Pull Requests](https://youtu.be/XQs5KcUj-Do?t=1254) as a good way of getting feedback or comments from other people that you're collaborating with on projects. You would like someone to review those changes before we merge them into the master branch of a repository, for example. It's a good sanity way to take a step back and take a look at the code that you're about to merge before you actually perform that merge.



# Advanced Learning 
* How deal with the console opens a vim when you git commit. Please read the [post](https://stackoverflow.com/questions/6098742/using-git-commit-a-with-vim) form Stack Overflow.
* [Why need the git flow?](https://gitbook.tw/chapters/gitflow/why-need-git-flow.html)



