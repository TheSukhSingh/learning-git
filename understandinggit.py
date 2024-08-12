## git config - tells your details on the system connected to git


## git init 
# staging area - tells which files are to be monitored and saved by git
# commit history
# i have to create local repository, for that i will write git init
# this will create empty git repository (it is hidden folder, it has staging area and commit history)

# it will create a 'master' branch, but we need some other name, we can rename it later, but if we use it in this command we can directly name it main, command is below

# git init -b main
# now it will create branch 'main' (we can change name forcefully too if we want to at a later stage)

# git add filename -> this will add the file in the staging area

# git commit -> it goes into the local commit
# git commit -m "message" -> we have to pass a message then only we can commit

# git commit -a -m 'msg' -> this will auto save updates in staging area and then commit the files already in staging area

# git log -> it will give us the log of all the commits

# if we have some changes...and then we write git status, it will check and tell there is some modifications

# now if i type git commit -m "something"
# it will not commit, but say that changes not staged for commit
# reason -> file is not in staging area, 
# when we have to commit something, the file is currently in working directory, and then we have to add it to staging area, and from there it will go to commit history(local commit), but we did not add it in staging area, that is the reason commit did not work

# first do git add filename
# then write git commit
# now it will work



## diff command -> checking the difference
# git diff
# it checks the difference between last staged file, and the current working directory file (if we do git add filename), then it will not see changes, bcoz the file is saved in staging area, it checks for changes in staged and current working
# git diff --cached
# it will show the difference between the staged file and the last commit
# git diff HEAD
# it will show the difference between latest commit, and working directory


# removing a file from git repository
# maybe bcoz that file has something confidential...and you don't want it to be uploaded
# firstly you added in commit, and now you want to remove it.
# git rm --cached filename
# remember - this will only remove for upcoming commits, not for previous commits..so just don't add this file in staging area in the first place.


## setting up repo

# echo "# git-course demo" >> README.md
# this will create a readme file (md -> markdown)

# git init
# same meaning

# git status
# tells the files untracked and tracked

# git add filename
# it will be added in staging area

# git commit -m 'msg'

# git branch -M main
# it will rename the branch from master to main forcefully

# difference between using ssh and https is 
# for https - it asks for login everytime
# for ssh - setup the machine once, setup the key, and it will automatically login you


# ssh-keygen -o
# this created a key for one time, no need to create this again, it is created only once
# enter the filename: don't enter anything (goes for default name)
# passphrase - don't enter anything
# just press enter, and then the file is created
# now go to hidden folder .ssh and open the file, and copy the key
# go to github settings, and ssh keys, enter the ssh key and save a name , eg learning github
# it will successfully connect client and server.

# git remote add origin (add ssh link)
# remote is connected

# git push -u origin main
# pushes the commit to github
# -u means upstream
# git push -u origin main -> for initial push
# git push -> for subsequent pushes

# why origin? 
# git remote -v - fetch and push links
# here we can see it is named as origin



## git tag (this means version of software - like v1.1 v1.5)
# command is
# git tag - this will show you all the tags which are given till now for this project
# (annotated tagging, lightweight tagging)
# annotated tagging below -
# git tag -a v1.0 -m '1st release'
# git show v1.0 - this will show all the details for this tag