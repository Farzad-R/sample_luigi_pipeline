# Title

Sample luigi pipeline 

## Description

A sample luigi pipeline using  .cfg files as config, with auto logging generation. Furthermore, project has a single entery point which was designed using argparse. The entery point can be designed based on the requirements of the project.
For instance you can use Hydra as an alternative.

## Notes:

In order to be able to use the project in different operating systems without the need to change the path structure (for windows, linux and mac), os library and pyprojroot were utilized. Moreover, using pyprojroot, the project automatically detects the location of your project's root directory. So, no need to modify the directories in your system. 

In your own project, I suggest to add data, report_docs, and logs folders to .gitignore. 

Luigi tasks can contain three different parts, requires, output, and run. Howoever, the way you use these three methods vary based on your needs. In this pipeline, I didn't use the requires method. Also, output is just used to create the new output directory for that specific task.
Check the [documentation](https://luigi.readthedocs.io/en/stable/tasks.html) for further information of how you can use luigi pipelines.

## Project initial structure

Current structure of the project:
```
.
├── data                    # (added to .gitignore)
│   ├── clean               # Clean data (auto-generate)
│   ├── transform           # transformed data (auto-generate)
│   └── raw                 # The raw data
│       ├── annual-enterprise-survey-2020-financial-year-provisional-csv.csv
│       └── ca-500.csv
│ 
├── docs                    # contains the documentation of the project (data information - project information - etc.)
│   └── ...TODO
│ 
├── report                  # Reports to be recorded for later use or to be shown (added to .gitignore)
├── notebooks               # Exploration jupyter notebooks
├── config                  # config files for the main pipeline
├── src                     # Contains the codes of the main pipeline
│   ├── utils               # Includes utils.py module
│   ├── clean
│   ├── transform
│   └── ...TODO
│
├── logs                    # Includes two levels of log files (for different log levels)
│   ├── debug.log               
│   └── info.log
│
├── requirements.txt        # Required packages for the project
├── README.md
├── .gitignore
├── setup.py
└── test					# contains unit-test for different parts of the project
```
## Example of how to get started with this project:

- Clone the project
- create a virtual env
- Activate your env
- Run pip install -e .

And you are ready to go.

### How to run and commands:

- Open the project in the root directory. 
- Open terminal
- Make sure the right virtual environment is activated
- In the terminal run the following commands

```
python main.py taskt1

python main.py taskc1
```

- You should see the luigi commands end with :) status.

#### Luigi web interface:

- Change default value of scheduler argument in main.py to False.
- In terminal run: luigid
- Open http://localhost:8082/
- Run the tasks in a separate terminal
- Refresh luigi web page 

## Data:

Free data downloaded from internet.

### Dependencies

Dependencies are managed using pip. However, other pakcages such as poetry and pyenv can also be utilized. 

## Authors

[Farzad Roozitalab](https://www.linkedin.com/in/farzad-roozitalab-173066152/)