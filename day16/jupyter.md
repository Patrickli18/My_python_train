### 新建环境

```bash
conda create -n new35 python=3.5
```

### 添加到 Jupyter Notebook

```bash
conda activate new35
python -m ipykernel install --user --name new35 --display-name "Python 3.5"
```

### 退出虚拟环境

```bash
conda deactivate
```

### 安装 Python 包

```bash
pip install graphviz
pip install numpy
pip install scipy
pip install scikit-learn
pip install pandas
pip install keras
pip install tensorflow
```