
# Reminder


##Flasky
flasky is a tutorial from
https://blog.miguelgrinberg.com/post/setting-up-a-flask-application-in-visual-studio-code
Inside there, I created an virtual env named "env"



##FreeCodeCamp
The rest of the part is follow 
https://www.youtube.com/watch?v=Z1RJmh_OqeA
Howeer, there is some issues with the video

###Issue 1: install virtualenv
In order to use pip, use the comman show inside 
py -3 -mpip install virtualenv
https://stackoverflow.com/questions/55876467/pip3-is-not-recognized-as-an-internal-or-external-command-operable-program-or

###Issue 2: activate
The 'source' command is for linux 
https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate
Since I'm using powershell, what I should do is
- Set-ExecutionPolicy RemoteSigned (this doesn't work)
- Set-ExecutionPolicy -Scope CurrentUser
  ExecutionPolicy: RemoteSigned
  env\Stripts\activate
Check out detailed documentation at
https://virtualenv.pypa.io/en/legacy/userguide.html#activate-script


**Why we need virtual env?
**So whatever we install or config can be inside this env, 
**Won't affect your global
**Also easier for collaboration


###Reminder 1
To create database
1. Go to env
2. > py -3
3. >>> from app import db
4. >>> db.create_all()
- Then a test.db will be created
5. >>> exit()

###Reminder 2
**Check out more about the "Jinja syntax" 


###Issue 3
Changes made in CSS is not reflecting
Two possible reasons
1. CSS rule is not applied
2. CSS file is cached
- in my case, the reason is 2.
- Try ctrl + F5 in browser to force the refresh
https://stackoverflow.com/questions/28235731/css-changes-are-not-getting-reflected-why


###Reminder 3
After login to heroku, need to use gunicorn to create requirement.txt
py -3 -mpip install guinicorn
py -3 -mpip freeze > requirements.txt

###Reminder 4 After pushing, need to create procfile

###Issue 4
Heroku application error: H14 error in heroku - “no web processes running”
The problem is because of the "dynos"
https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app
