# Tabular Machine Learning: Car Insurance Claim Prediction

Binary classification using tree-based methods on tabular data.

## Dataset

Dataset comes from [Kaggle](https://www.kaggle.com/datasets/ifteshanajnin/carinsuranceclaimprediction-classification)
- Tabular data records policy holder information such as vehicle age, make and model, fuel type etc.

Problem: Car insurance is mandatory for car owners in many countries, so there is a lot of data for car insurance companies. These companies need to make informed decisions about new customers, mainly whether or not they think the user will make a claim soon, costing the company money. The focus of this project is to see if a new customer will make a claim in the next 6 months with this dataset.

Run `make dataset` to download/setup dataset. Requires [Kaggle CLI](https://www.kaggle.com/docs/api).
- Otherwise, download from above Kaggle link, and unzip to `data/` in this directory

## Technologies
- Python
- Anaconda
- Pipenv
- Pandas, NumPy



## Development Overview:
- Setup environment with Pipenv/Anaconda
- [EDA and modelling](./source/notebooks/eda.ipynb)

## Setup

See [Setup instructions](./SETUP.md). Install Git LFS before pulling repo to pull model and weights.

## Use

# TODO
Refer to [Makefile](./Makefile).
1. Run `make setup` to install environment
2. Train with `make train`
