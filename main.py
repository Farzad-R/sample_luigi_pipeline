# code example: open terminal in the project directory, invoke the environment, run:
# For this specific file open the terminal in the parent folder and run:
# python main.py taskt1
# python main.py taskc1


import argparse
import luigi
import src.config as cfg  # config module needs to be run for setting up the logging
import logging
from src.transform.TransformAnnualEnterprise import TransformAnnualEnterprise
from src.clean.CleanCA500 import CleanCA500

logger = logging.getLogger(__name__)

# assigning the terminal arguments
parser = argparse.ArgumentParser()
parser.add_argument("task", type=str, help="choose the desired task")
parser.add_argument(
    "-w", "--workers", type=int, help="number of luigi workers", default=5
)
parser.add_argument(
    "-s",
    "--scheduler",
    help="state of scheduler True or False",
    default=True,
)
# if False: open terminal, invoke the env (source /home/imspecies/python_envs/ieso_env/bin/activate),
# run: luigid, open: http://localhost:8082/, run the task

args = parser.parse_args()


def init_tasks():

    transform_tasks = {
        "taskt1": TransformAnnualEnterprise,
    }
    clean_tasks = {
        "taskc1":CleanCA500
    }


    # Union of dicts
    tasks = {
        **transform_tasks,
        **clean_tasks,
    }
    return tasks


Tasks = init_tasks()


def main(task=args.task, workers=args.workers, scheduler=args.scheduler):
    try:
        luigi.build([Tasks[task]()], workers=workers, local_scheduler=scheduler)
    except:
        logger.error(f"Task {task} does not exist")
        raise


if __name__ == "__main__":
    main()
