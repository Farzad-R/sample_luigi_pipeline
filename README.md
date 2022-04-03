# Title

PhD Project 

## Description

Wind Power Prediction

## Project initial structure

Current structure of the project:
```
.
├── data                    # (added to .gitignore)
│   ├── augment
│   ├── clean               # Clean data (auto-generate)
│   ├── external            # External data that is used in the project
│   ├── interom             # The mid-level data (e.g mapping files) (auto-generate)
│   ├── processed           # The processed data for training
│   ├── transform
│   └── raw                 # The raw data
│       ├── ieso_power      # The wind farms output power
│       └── met_tower       # The weather forecast data
│ 
├── docs                    # contains the documentation of the project (data information - project information - etc.)
│   ├── datasets.opg        # description of raw datasets (their column, types, etc.)      
│   └── ...TODO
│ 
├── report                  # Reports to be recorded for later use or to be shown during th weekly meeting (added to .gitignore)
├── notebooks               # Exploration jupyter notebooks
│   └── planning.md         # this file is for my brainstorms and project planning
├── config                  # config files for the main pipeline
├── src                     # Contains the codes of the main pipeline
│   ├── utils               # Includes utils.py module
│   ├── augment
│   ├── clean
│   ├── download
│   ├── map
│   ├── report
│   ├── transform
│   └── ...TODO
│
├── logs                    # Includes two levels of log files
│   ├── debug.log               
│   └── info.log
│
├── requirements.txt        # Required packages for the project
├── README.md
├── pyproject.toml          # poetry dependancy management file
├── poetry.lock
├── .gitignore
├── setup.py
└── test					# contains unit-test for different parts of the project
```
### Pipeline Order:
	- download
	- transform: drop useles columns, make all column names lowercase, check column data types, set index if needed
	- clean: Any further cleaning needed beside the ones performed in transform (e.g: dropping extra rows, filtering met info based on data percentage,
	 filtering ieso and met based on min and maximum valid data etc.)
	- augment: adding nny necessary data to the transformed or cleaned datasets (e.g: wind_compass_direction, wind direction 360 degree altitude, etc.) 
	---> preprocess: preprocessing tasks(e.g: feature extraction, interpolation, merge, etc.)			 <---
	│																										 │
	---> evaluate: evaluating the output of preprocessing step (e.g: feature importance selection, etc.) <---
	- train: training using the outputs of preprocessing ()
	- ... TODO

### Command Order:
TransformIesoCrossReference
TransformIesoPower
TransformMetStationInventory

DownloadMetData
TransformMetStation
CleanMetStation
MetStationsGeographicalInfo
MapWindAngle
ConvertWindAngle

CorrelationCheck
## Getting Started

Project uses [poetry](https://python-poetry.org/) for managing the dependencies. Furthermore, [luigi](https://luigi.readthedocs.io/en/stable/) is used for pipeline creation.
Install the libraries from requirements.txt with pip, or use pyproject.toml. Tasks' execution were tested in both linux and ubuntu.

### Windows 11:
1. Install python
2. Install vscode
3. Install sourcetree
	- connect it to the github
	- modify the setup file if necessary (in case you get select helper constalntly, search for it and modify the helper. set it as manager-core)
	- clone the repository

4. install git for windows
5. install poetry using windows poewrshell (search for hte code. It is not pip install poetry)
6. open windows powershell
	- run: pip --version (if it throws you an error, then you need to install it)
	- run: pip install Virtualenv
	- python -m venv .venv (.venv is the name of the environment)
		ex: python -m venv .ieso_env

6. open vscode (you can also create virtual env from vscode terminal. search for it if you want to see how)
	- Go in the project root directory
	- find the virtual env and add it to the vscode
	- open a command prompt as the terminal (instead of powershell). (it should automatically activate the virtual environment)
    - inside the project root directory run: "pip install -e ." (It will automaticall install all the dependencies and prepare the project)


7. Usefull tools:
	- pip install -e .
    - python setup.py --help
    - python setup.py install
	- pip install -r requirements.txt
    - poetry install (for now it has a problem with installing scipy) To be investigated later

	- poetry lock
	- poetry update
	- poetry add "packagename" / pip install packagename
	- poetry remove "packagename" / pip uninstall "packagename
	In windows:
		- TODO
	In Ubuntu:
		- source <dir to the virtual env>/bin/activate (e.g: source /home/imspecies/python_envs/ieso_env/bin/activate)
	- luigid: http://localhost:8082/

	- In case you yield a luigi tas: ... = self.input()[0].path 

8. Creating/Cloning a project:
	** Creating a new project: (cd to your desired directory)
	- git init
	- git remote add origin http://.../...git (origin is the name of the repo)
	** Cloning an existing project (cd to your desired directory)
	- git clone https://github.com/gittower/git-crash-course.git <name of the folder that you want to clone the project>
9. Source control:
	** Create a branch for each task. Then, ask for pull request. DO NOT PUSH INTO THE MASTER DIRECTLY.
	- git fetch origin
	- git pull origin
	- git push origin master
	- for windows sourcetree can be installed for the cource control

### Ubuntu:
- TODO

### Data:
https://drive.google.com/file/d/1YRr9xB8X7QffXSYoaPw15yjNd-1Y-_we/view?usp=sharing

### Dependencies

Dependencies are managed using Poetry. However, the requirement.txt file is also included for pip use.

## Authors

[Farzad Roozitalab](https://www.linkedin.com/in/farzad-roozitalab-173066152/)