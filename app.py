from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


## config app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' ##using //// 4 is 
db = SQLAlchemy(app)                                        ##using /// 3 is relative


## Todo class 
## Object to be stored as todo task
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) #create content, and cannot be null
    date_created = db.Column(db.DateTime, default=datetime.utcnow) #access to date

    def __repr__(self):
        return '<Task %r>' % self.id 
        #to return string everytime created an element


## route
@app.route('/', methods=['POST', 'GET'])
def index(): ## config "add task" functions
    if request.method == 'POST':
        task_content = request.form['content'] ##get name="content" at <form> of index.html
        new_task = Todo(content=task_content) ##initi new Todo task

        ##after created the content, try to commit to database
        try: 
            db.session.add(new_task)
            db.session.commit()
            return redirect('/') ##if sucess, redirect to index page
        except:
            return 'There was a problem adding your task'    

    else:
        tasks = Todo.query.order_by(Todo.date_created).all() ##look at all the db, and order by date
        return render_template('index.html', tasks=tasks) ##the file must be inside folder with the name, "templates"
                                            ##don't forget to pass the tasks inside templates



## Delete Task
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id) ##get the task using id || if nothing, return 404

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


## Update task
## will redirect to update.html for editing
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem updating your task'

    else:
        return render_template('update.html', task=task)



if __name__ == "__main__":
    app.run(debug=True)