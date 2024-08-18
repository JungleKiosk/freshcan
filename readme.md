# 1. creating a virtual environment

Put those command lines on terminal cmd:

## create folder
```
cd Desktop
mkdir name_project
```

## initial command
- for Windows: 
```
name_project\python -m venv venv
```
- for Mac|Unix: 
```
name_project/python3 -m venv venv
```

## Activate venv

- for Windows:
```
name_project\venv\Scripts\activate
```

- for Mac|Unix:
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
PS C:\Users\name_admin\Desktop\folder_proj\name_project> python -m venv venv
PS C:\Users\name_admin\Desktop\folder_proj\name_project> python -m venv venv
PS C:\Users\name_admin\Desktop\folder_proj\name_project> venv\Scripts\activate             
(venv) PS C:\Users\name_admin\Desktop\folder_proj\name_project> 
```

# Create Gitignore file
to hide all files in the venv folder:
- create a file named `.gitignore`
- write `venv/`
- save and push


