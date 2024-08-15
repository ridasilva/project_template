# Boas práticas de programação

Aqui vamos fazer os comentários básicos para criação de um projeto para ciência dos dados.

## Instalação

Instalando o `conda`

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

```

Criando um ambiente em conda e ative o ambiente para uso 

```
conda env create -f environment.yml
conda activate project_template 
```

Para criar ou atualizar um arquivo [environment.yml](./environment.yml), faça:

```
conda env export | grep -v "^prefix: " > environment.yml
```

## Usando a ferramenta

Após a instalação e ativação do ambiente, é possível usar a ferramenta de comando fazendo

```
python hello.py <nome do visitante>
```

Também é possível utilizar o módulo dentro de um `terminal` ou `notebook`, veja o exemplo:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ridasilva/project_template/blob/master/notebooks/hello.ipynb)
