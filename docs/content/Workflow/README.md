# Workflow tips

## Text editor suggestions

In our recommended Python development workflow, you will write Python scripts and modules (`*.py` files) in a text editor. Then you will run those scripts from your terminal. You will want a capable text editor for developing your code. Many capable text editors exist, but I recommend [Visual Studio Code](https://code.visualstudio.com).

[VS Code](https://code.visualstudio.com) is free and will be included with your installation of Anaconda.  This is a very capable text editor and will include syntax highlighting for Python and and built in Git controls.  In addition to the basics, you may want to use a more advanced linter for Python.  This will help you correct syntax errors on the fly and provide helpful information as you declare objects and call functions.  [This link](https://code.visualstudio.com/docs/python/linting) provides step-by-step instructions on using more advanced linting in VS Code.

Some extensions that I recommend installing into your VS Code:
* cornflakes-linter
* Git Extension Pack
* GitLens
* Jupyter
* LaTeX language support
* LaTeX preview
* LaTeX Workshop
* Markdown All in One
* Pylance
* Stata Enhanced


## Working in the Command Line

It's helpful to know your way around the Unix/DOS command line.  This is the way I recommend interacting with Git (discussed below) and is also how I typically run Python scripts.  It's also the only way you can typically interact with remote servers on which you might store data or run software (such as the [Research Cyber Infrastructure](http://www.sc.edu/about/offices_and_divisions/division_of_information_technology/rci/) clusters on campus).

Some of the most common commands you'll use are summarized in the table below.

| Command                                              | Unix                                                                                                         | DOS                                                                                                                              |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Change directory                                     | `cd <directory path>` (could be relative path)                                                                 | `cd `                                                                                                                              |
| List files in directory                              | `ls  `                                                                                                         | `dir`                                                                                                                              |
| Move up one level in directory structure             | `cd .. `                                                                                                       | `cd ..`                                                                                                                            |
| List current processes                               | `ps`                                                                                                           | `tasklist`                                                                                                                         |
| Kill a running process                               | `kill <process id>`                                                                                            | `Taskkill /PID <process id> /F  `                                                                                                  |
| Connect to remote machine via secure shell           | `ssh -p <port number> <user@hostname>`                                                                         | `<path to PuTTY.exe> -ssh <username@host> <port number>  `                                                                         |
| Transfer files to a remote machine (via Secure Copy) | `scp [options] <username1@source_host:directory1/filename1> <username2@destination_host:directory2/filename2>` | `pscp -scp [options] <username1@source_host:directory1/filename1> <username2@destination_host:directory2/filename2>`              |
| Submit a batch script                                | `qsub <filename.sh>`                                                                                           | unlikely to do this. If need to, see [here](https://stackoverflow.com/questions/26522789/how-to-run-sh-on-windows-command-prompt) |

## Git and GitHub tutorial

 Git is a powerful version control software that comes natively installed on many machines and is widely used. GitHub.com is the most widely used online platform for hosting open source projects and integrating with Git software. Git has a significant learning curve, but it is essential for large collaborations that involve software development.

 A good online tutorial for my preferred git workflow can be found at [https://pslmodels.github.io/Git-Tutorial](https://pslmodels.github.io/Git-Tutorial).  Below, I summarize some of the most common commands you'll use in Git.

| Functionality                                               | Git Command                                                      |
|-------------------------------------------------------------|------------------------------------------------------------------|
| See active branch and uncommitted changes for tracked files | `git status -uno`                                                  |
| See branches (with note about active branch)                | `git branch`                                                  |
| Change branch                                               | `git checkout <branch name>`                                       |
| Create new branch and change to it                          | `git checkout -b <new branch name>`                                |
| Track file or latest changes to file                        | `git add <filename>`                                               |
| Commit changes to branch                                    | `git commit -m "message describing changes" `                      |
| Stash changes (ignore them from history)                    | `git stash <filename> `                      |
| Push committed changes to remote branch                     | `git push origin <branch name>`                                |
| Merge changes from master into development branch           | `(change working branch to master, then…) git merge <branch name>` |
| Merge changes from development branch into master           | (change to development branch, then…) `git merge master`           |
| List current tags                                           | `git tag`                                                          |
| Create a new tag                                            | `git tag -a v<version number> -m "message with new tag"`           |
| Pull changes from remote repo onto local machine            | `git fetch upstream`                                               |
| Merge changes from remote into active local branch          | `git merge upstream/<branch name>`                                 |
| Clone a remote repository                                   | `git clone <url to remote repo>`                                  |
