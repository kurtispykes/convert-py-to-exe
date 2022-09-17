# Creating Executable Files in Python
There are several scenarios of which you may wish to convert a Python file (`.py`) to and executable file (`.exe`), for example, you may want to hide your source code
when sharing Python scripts with others. Executable files are used to install or run software applications on computers with a Windows operating system. In this project,
I cover two methods to convert a `.py` file to an `.exe`. To achieve this, I created an automated validation schema that will run periodically (hypothetically) to 
prevent my (imaginary) Data science team from engaging in repetitive task. The data used in this project is the 
[New York City Airbnb open data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data?resource=download&select=AB_NYC_2019.csvhttps://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data?resource=download&select=AB_NYC_2019.csv) dataset. 

## Installation 
- Clone this repository to your local computer 
- You will have to [create two virtual environments](https://docs.python.org/3/library/venv.html) if you wish to sample both methods
  - One in the `auto_py_to_exe` repository and the other in the `pyinstaller` repository.
  - Only activate the virtual environment for the tool you are using
- Install the respective requirements by navigating to the tool you wish to use to create the executable file and running the following command 
from your terminal (be sure to activate the correct virtual environment): `pip install -r requirements.txt`

## Usage
### Creating an .EXE file with Pyinstaller
- In your terminal, navigate to the `pyinstaller` directory.
- Activate the virtual environment 
- Install the requirements using `pip install -r requirements.txt`
- Run the following command: `pyinstaller --onefile validation.py`
  - This will create two new directories: `build` and `dist` - the `validation.exe` file is in the `dist` directory. 
  
### Creating an .EXE file with Auto Py To Exe
- In your terminal, navigate to the `auto_py_to_exe` directory.
- Activate the virtual environment 
- Install the requirements using `pip install -r requirements.txt`
- Run the following command: `auto-py-to-exe `
  - This will return a GUI where you must set the configuration (see [Auto py to exe Tutorial](https://www.datacamp.com/tutorial/two-simple-methods-to-convert-a-python-file-to-an-exe-file#:~:text=see%20Figure%202.-,Auto%20py%20to%20exe%20Tutorial%C2%A0,-The%20first%20step) for assistance)

## Extending this project
- Deploy the `.exe` file and set up periodic runs

## Articles Related to This Project
- [Two Simple Methods To Convert A Python File To an EXE File](https://www.datacamp.com/tutorial/two-simple-methods-to-convert-a-python-file-to-an-exe-file)
