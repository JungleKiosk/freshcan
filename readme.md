# 1. creating a virtual environment

Put those command lines on terminal cmd:

## create folder
```
cd Desktop
mkdir name_project
```

## initial command
for Windows: 
```
name_project\python -m venv venv
```
for Mac|Unix: 
```
name_project/python3 -m venv venv
```

## Activate venv

for Windows:
```
name_project\venv\Scripts\activate
```

for Mac|Unix:
```
name_project/source venv/bin/activate
```

### ERROR: PowerShell execution policy restrictions.

To solve this problem, you need to change the execution policy to allow scripts to execute.

- 1st Steps_ Open PowerShell as Administrator:
    - Search for “PowerShell” in the Start menu.
    - Right-click on “Windows PowerShell” and select “Run as Administrator.” <br>

- 2nd step_ Change the Execution Policy:
    - In PowerShell, run the following command to allow scripts to run
    ```
    Set-ExecutionPolicy RemoteSigned
    ```
    - When prompted, confirm the change by responding with “Y” (Yes).<br>

- 3rd step_Activates the virtual environment:
    - for Windows: 
    ```
    name_project\python -m venv venv
    ```
    - for Mac|Unix: 
    ```
    name_project/python3 -m venv venv
    ```

## Result
```
C:\Users\name_admin\Desktop\folder_proj\name_project> python -m venv venv
C:\Users\name_admin\Desktop\folder_proj\name_project> python -m venv venv
C:\Users\name_admin\Desktop\folder_proj\name_project> venv\Scripts\activate             
(venv) C:\Users\name_admin\Desktop\folder_proj\name_project> 
```

# 2. Create Gitignore file
to hide all files in the venv folder:
- create a file named `.gitignore`
- write `venv/`
- save and push

# 3. Installing Flask

.../name_project>
```
python -m pip install --upgrade pip

```

```
pip install flask

```
# 4. Create Flask Environment

1. create file `.flaskenv`
2. set variables inside `.flaskenv`:
    ```
    FLASK_ENV=development
    FLASK_APP=module.py
    ```
3. run `pip install python-dotenv`

# 5. Automatically create file 'requirements.txt'

running `C:\Users\...\name_project> pip freeze > requirements.txt` and save all your python libraries with current version into requirements.txt file

# 6. DB integrate
## install libraries

C:\Users\ ... \name_project\venv>

1. run `pip install psycopg2`
2. run `pip install Flask-SQLAlchemy`

## DB config
in app.py:
```
from flak_sqlalchemy import SQLAlchemy

# config connection DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psqcopg2://postgres:password@localhost:5432/fc_db'

# SQLAlchemy will not keep track of changes on objects unless they are explicitly added to the session.
# This reduces memory overhead and improves performance.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init SQLAlchemy
db = SQLAlchemy(app)

# (Model)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# create table in DB
with app.app_context():
    db.create_all()
```




