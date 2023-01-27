# Variables

## Download Dataset
dataset: 
	kaggle datasets download ifteshanajnin/carinsuranceclaimprediction-classification
	mkdir data
	unzip carinsuranceclaimprediction-classification.zip -d data > /dev/null
	rm carinsuranceclaimprediction-classification.zip

## Training model and running locally with BentoML
train:
	pipenv run python ./source/trainer.py

setup:
	pipenv install --dev
