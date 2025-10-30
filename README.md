# GLINT-RU
This is the main implementation code of GLINT-RU for sequential recommender systems.

## 🛠️Installation
First you need to install `recbole` to conduct the experiments.There are some bugs in some updated versions in `recbole`, so you should modify the `models/sequential recommenders` in these versions.

If you run the code with the error mentioning `ldiffrec`, you can replace the `ldiffrec.py` by our code as a placeholder in `general recommender` to solve it.
- First step:
```bash
pip install recbole, ray, ray-tune, protobuf==2.21.0
```
## 🚀Configuration & Training
Replace the configuration file like `ml-1m.yaml` in the `dataset` folder in the recbole package.
You can change the configuration for your own experiments.
Replace the `overall.yaml` in the recbole package.
Note: The maximun sequence length should be changed according to different datasets.
- Third step:
```bash
python run.py
```
Some basic configurations are set in `run.py`. 

## Experiment Results
More details can be found in our paper: https://dl.acm.org/doi/pdf/10.1145/3690624.3709304

## 🎓Citations
```latex
@inproceedings{zhang2025glint,
  title={Glint-ru: Gated lightweight intelligent recurrent units for sequential recommender systems},
  author={Zhang, Sheng and Wang, Maolin and Wang, Wanyu and Gao, Jingtong and Zhao, Xiangyu and Yang, Yu and Wei, Xuetao and Liu, Zitao and Xu, Tong},
  booktitle={Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 1},
  pages={1948--1959},
  year={2025}
}
```

