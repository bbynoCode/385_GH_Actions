# Learning GitHub Actions
[![Python Action](https://github.com/bbynoCode/385_GH_Actions/actions/workflows/python-action.yml/badge.svg)](https://github.com/bbynoCode/385_GH_Actions/actions/workflows/python-action.yml)

In this repo I will be teaching you how to use github actions to automate the running of python unit tests. 

## Getting Started

1. Fork this repo and then clone it to your local machine

2. Create a virtual enviroment in the repo you cloned. On my machine the command to do this is ```python3.12 -m venv .venv```

3. Activate the virtual enviroment you just created and then install the required python modules. You can do with with the command ```pip install pytest``` or ```pip install -r requirements.txt ```

## Running Python Tests 

Once you have the repo cloned and the pytest module installed you can run the current set of tests using the command ```pytest example.py``` 

It is important to run (and write) your unit tests whenever you write new code. If you write a lot of code then that means you will be running your tests a lot.