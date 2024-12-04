# Learning GitHub Actions

In this repo I will be teaching you how to use github actions to automate the running of python unit tests. 

## GitHub Actions Sales Pitch

1. [GitHub Actions Features](https://github.com/features/actions)

## Getting Started

1. Fork this repo and then clone it to your local machine

2. Create a virtual environment in the repo you cloned. On my machine the command to do this is ```python3.12 -m venv .venv```

3. Activate the virtual environment you just created and then install the required python modules. You can do with with the command ```pip install pytest``` or ```pip install -r requirements.txt ```

## Running Python Tests 

Once you have the repo cloned and the pytest module installed you can run the current set of tests using the command ```pytest -v example.py``` 

You will see that some of the tests are failing, this is by design for this example. We will fix the failing test cases later on in the example.

It is important to run (and write) your unit tests whenever you write new code. If you write a lot of code then that means you will be running your tests a lot. To save you time and effort we are going to be automating this.



## Automating Tests

1. In your local git repo make a new folder called ``` .github ```

2. Navigate to your ``` .github ``` directory and make another directory called ``` workflows ```

3. Navigate to ``` workflows ``` and make a new file called ``` python-action.yml ``` . The project structure should look like this ``` 385_GH_Actions/.github/workflows/python-action.yml ```

4. Inside your new YAML file copy and paste the code below and then save it. 

```
name: Python Action

on: [push]

jobs:
  Run-Tests:
    strategy:
      matrix:
        os: [macos-latest, ubuntu-latest] 

    runs-on: ${{ matrix.os }}
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

## Results 

Congratulations! We have now added an action to our repo that runs all of our test cases.

To view actions that have ran in our repo and their results we want to click on the button that says ```actions```. It is near the top of the page on the github repo.

We should see that our action failed. If we dig a little deeper we can see what step inside the action caused it to fail. In our case it was the step that actually ran the tests. It failed because we had tests that failed. 

Now is the time to go back and correct the failing tests. Once we commit and push the fixes to github our actions will run again and we should see that it passed this time.