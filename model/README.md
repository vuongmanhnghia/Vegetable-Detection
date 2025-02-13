### **Set up Model and Backend**

Note that the current path address is in the form '.../model>'

```bash
python.exe -m pip install --upgrade pip
```

#### 1. Set up virtual environment

```bash
python -m venv venv
```

#### 2. Create `.env` file and copy the content in `.env.example` file to `.env` file and configure the environment variables

#### 3. Select Interpreter

##### PowerShell

```bash
venv\Scripts\activate.ps1
```

##### Command Prompt

```bash
venv\Scripts\activate.bat
```

When the terminal path shows '(venv)' it is successful

```
(venv) C:/...
```

#### 4. Install the necessary libraries

```bash
pip install -r requirements.txt
```

#### 5. Run the project

```bash
uvicorn app.main:app --reload
```
