# Title

Sample luigi pipeline 

## Description

A sample luigi pipeline using  .cfg files as config, with auto logging generation. Furthermore, project has a single entery point which was designed using argparse. The entery point can be designed based on the requirements of the project.
As an example, using Hydra is another option.

## Notes:

In order to be able to use the project in different operating systems without the need to change the path structure (for windows, linux and mac), os library and pyprojroot were utilized. Moreover, using pyprojroot, the project automatically detects the location of parent folder. So, no need to modify the directories in your system. 

In your own project, I suggest to add data, report_docs, and logs folders to .gitignore. 
## Project initial structure

Current structure of the project:
```
.
├── data                    # (added to .gitignore)
│   ├── clean               # Clean data (auto-generate)
│   ├── transform
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

### Command Order:
'''
- python main.py taskt1
- python main.py taskc1
'''

## Example of how to get started with this project:

- Clone the project
- create a virtual env
- activate your env
- Run pip install -e .

And you are ready to go.


## Data:
Free data downloaded from internet.

### Dependencies

Dependencies are managed using pip. However, other pakcages such as poetry and pyenv can also be utilized. 

## Authors

[Farzad Roozitalab](https://www.linkedin.com/in/farzad-roozitalab-173066152/)