# Gradio Integration to Lightning Template

## ViT Lightning Module on CIFAR10 dataset

## Model Training and Testing

1. Clone the repo:
```
git clone -b branch gradio https://github.com/AKJ21/emlo_assignment6.git
```
2. Install requirements and setup:
```
pip install -r requirements.txt && pip install -e .
```
3. Train the model:
```
copper_train experiment=gradio trainer.max_epochs=10"
```
Note: By default, trainer is set to train for maximum 1 epochs. You may change this setting by adding trainer.max_epcohs=10 for training 10 epochs.

To check default parameters set for trainer:
`copper_train --help`

To check parameters list for gradio experiment:
`copper_train experiment=gradio --help`

## Gradio Application

To run locally:
`python3 gradio.py`

To run the application inside docker:
- Build docker image with "`docker build --tag vit-gradio .`"
- Run the built image: "`docker run --rm -it vit-gradio`"

Open `localhost:8080` to start playing with the app.

## Group Members:
- Aman Jaipuria
- Anurag Mittal