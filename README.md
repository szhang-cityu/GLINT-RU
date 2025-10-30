# GLINT-RU
This is the main implementation code of GLINT-RU for sequential recommender systems.

## 🛠️Installation
First you need to install `recbole` to conduct the experiments. There are some bugs in some updated versions in `recbole`, so you should modify the `models/sequential recommenders` in these versions. Move `GLINT-RU.py` to the `sequential_recommender` and modify the `__init__.py` to make sure the GLINT-RU model can be intregrated into recbole framework.

If you run the code with the error mentioning `ldiffrec`, you can replace the `ldiffrec.py` by our code as a placeholder in `general recommender` to solve it. Then you should also change the corresponding `__init__.py` by editing the import code using the placeholder.

Install recbole and other required packages:
```bash
pip install recbole, ray, ray[tune], protobuf==3.20.0
```
## 🚀Configuration & Training
Replace the configuration file like `ml-1m.yaml` in the `dataset` folder in the recbole package.

You can change the configuration for your own experiments.

Replace the `overall.yaml` in the recbole package.

Note: The maximun sequence length should be changed according to different datasets.

Train GLINT-RU:
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

