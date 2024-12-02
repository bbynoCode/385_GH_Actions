# Learning GitHub Actions

In this repo I will be teaching you how to use github actions to automate the running of python unit tests. 

## GitHub Actions Sales Pitch

1. [GitHub Actions Features](https://github.com/features/actions)

## Hands On - Getting Started

1. Fork this repo and then clone it to your local machine

2. Create a virtual enviroment in the repo you cloned. On my machine the command to do this is ```python3.12 -m venv .venv```

3. Activate the virtual enviroment you just created and then install the required python modules. You can do with with the command ```pip install pytest``` or ```pip install -r requirements.txt ```

## Running Python Tests 

Once you have the repo cloned and the pytest module installed you can run the current set of tests using the command ```pytest example.py``` 

It is important to run (and write) your unit tests whenever you write new code. If you write a lot of code then that means you will be running your tests a lot. To save you time and effort we are going to be automating this.

## Automating Tests

1. In your local git repo make a new folder called ``` .github ```

2. Navigate to your ``` .github ``` directory and make another directory called ``` workflows ```

3. Navigate to ``` workflows ``` and make a new file called ``` python-action.yml ``` . The project structure should look like this ``` 385_GH_Actions/.github/workflows/python-action.yml ```

4. Inside your new YAML file copy all of this and then save it. 

```
name: Python Action

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Test with pytest
      run: |
        pytest -v example.py 
```
5. Add your changes to git, make a commit and then push it to your forked repo on github

