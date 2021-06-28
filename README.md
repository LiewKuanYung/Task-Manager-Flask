
# README

This Flask application is a tutorial from
[Learn Flask from Python - Full Tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) <br>
The final deployment is at https://flasktaskmanagment.herokuapp.com/


# Issues and Reminder

However the tutorial consists some minor issues 


1. Some content are _OS sensitive_, (I run on Windows, the tutorial run on MacOS)
2. Some parts require extra steps


Hence this _README.md_  also aims to address those issues and write down some reminders

## Issue 1 (4:19): install virtualenv

We can't use pip3 like that directly <br>
In order to use pip to download venv, we need to use
```
terminal> py -3 -mpip install virtualenv
```

Check out [pip3-is-not-recognized-as-an-internal-or-external-command](https://stackoverflow.com/questions/55876467/pip3-is-not-recognized-as-an-internal-or-external-command-operable-program-or)

## Issue 2 (5:42): activate env

The _source_ command is for linux or Poisix, not really for windows <br>
Since I'm using powershell, what I should do to activate env is to do RemoteSigned first than call activate inside Scripts
```
terminal> Set-ExecutionPolicy RemoteSigned (but this doesn't work)
```
However, this might run into access denied issues. Instead, use
```
terminal> Set-ExecutionPolicy -Scope CurrentUser
terminal> ExecutionPolicy: RemoteSigned
terminal> env\Stripts\activate
```

Other relevant problems
Check out [issue-with-virtualenv-cannot-activate](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate) <br>
Check out [activate script documentation](https://virtualenv.pypa.io/en/legacy/userguide.html#activate-script)<br>
Check out [virtualenv is not recognized](https://stackoverflow.com/questions/35950740/virtualenv-is-not-recognized-as-an-internal-or-external-command-operable-prog)
<br>

Side note, why we need virtual env?
<br>
So whatever we install or config can be inside this env
<br>
It won't affect your global, also easier for collaboration

### Reminder 1
To create database
```
Go to env
terminal> py -3
py terminal>>> from app import db
py terminal>>> db.create_all()
```
Then a test.db will be created. Now we can exit py terminal
```
py terminal>>> exit()
```

### Reminder 2

Check out more about the "Jinja syntax" 

## Issue 3 (30:59): CSS not updating after edited

Changes made in CSS is not reflecting
<br>
Two possible reasons
<br>
1. CSS rule is not applied
2. CSS file is cached
<br>
In my case, the reason is 2.<br>
Try ``ctrl + F5`` in browser to force the refresh 

Check out [css-changes-are-not-getting-reflected](https://stackoverflow.com/questions/28235731/css-changes-are-not-getting-reflected-why)


### Reminder 3

After login to heroku, need to use gunicorn to create requirement.txt
```
py -3 -mpip install guinicorn
py -3 -mpip freeze > requirements.txt
```

### Reminder 4 

After pushing to git, need to create procfile

## Issue 4 (Final deployment)

Heroku application error: 
_H14 error in heroku - “no web processes running”_
```
terminal> git push heroku master
terminal> heroku ps:scale web=1
```
The problem is because of the "dynos" <br>
check the [heroku documentation](https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app)
