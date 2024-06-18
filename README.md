the following commands will help run the code
git init #initializes the git
git add . #adds all the files in the folder to the git
git commit -m "initial commit for github action" #this command helps in committing the code and create a time snapshot of the code. The -m is for message and you can put any descriptive message in ""
now go to your github.com account and create a repo. Name it something like githubactionexample. copy its link and then execute the following command
git remote add origin <link> 
for me the command was
git remote add origin https://github.com/kanav-mirakalous/githubactionexample.git
Now it is linked to your code on github repo
next type the command 
git push --set-upstream origin master
now it should be pushed to the github website click on actions 
this code would be rejected due to a low pylint score