# GLINT-RU
This is the main implementation code of GLINT-RU for sequential recommender systems.
First you need to install `recbole` to conduct the experiments.
There are some bugs in some updated versions in `recbole`, so you should modify the `models/sequential recommenders` in these versions.
If you run the code with the error mentioning `ldiffrec`, you should replace the `ldiffrec.py` in `general recommender` to solve it.
- First step:
```bash
pip install recbole
```
- Second step:
Replace the configuration file like `ml-1m.yaml` in the `dataset` folder in the recbole package.
You can change the configuration for your own experiments.
Replace the `overall.yaml` in the recbole package.
Note: The maximun sequence length should be changed according to different datasets.
- Third step:
```bash
python run.py
```
Some basic configurations are set in `run.py`. 

