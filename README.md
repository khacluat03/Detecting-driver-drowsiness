# Project to Detect Drowsiness and Distraction while Driving

## Introduction
This project focuses on developing a system to detect drowsiness and distraction while driving using three different deep learning models: YOLO, CNN (Convolutional Neural Network) and ViT (Vision Transformer).

## File structure
- `CNN_CV_01.ipynb`: CNN model training notebook
- `ViT_CV_01.ipynb`: Vision Transformer model training notebook
- `data224x224/`: Folder containing processed image data (size 224x224) [LINK](https://www.kaggle.com/datasets/nguyenluatdev/computer-vision-data224x224)
- `cv_report.docx`: Detailed project report
- `group_15_slide_computer-vision.pptx`: Project presentation slide
- `CodeTrainYolo`: Training YOLO model with [data](https://www.kaggle.com/datasets/nguyenluatdev/data-computer-vision)

## You can use the dataset to train YOLO via the labeled API from Roboflow
```
from roboflow import Roboflow
rf = Roboflow(api_key="tOfbkzltAMQMayGo8I3p")
project = rf.workspace("luatluat").project("final2-kwf46-fkead")
version = project.version(2)
dataset = version.download("yolov11")
```

## Kaggle Link
The model training notebooks can be found at:
- Vision Transformer (ViT): [notebook](https://www.kaggle.com/code/ngctnhong/vit-01)
- CNN: [notebook](https://www.kaggle.com/code/ngctnhong/cnn-cv-01)
- YOLO: [notebook](https://colab.research.google.com/drive/1FHDNQxvbh8P5Oj6rV6-kSXyojLdgtNHP?usp=sharing)

## Objectives
- Detect driver drowsiness
- Detect distracted driving behaviors
- Timely warning to ensure traffic safety

## Technology used
- Python
- Deep Learning
- Computer Vision
- CNN (Convolutional Neural Network)
- ViT (Vision Transformer)
- YOLO (ultralytics)

## Installation and running instructions

### System requirements
- Python 3.8 or later
- CUDA-compatible GPU (recommended for model training)

### Environment setup
1. Clone repository:
```bash
git clone [URL_REPOSITORY]
cd final-project-computer-vision
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install the required libraries:
```bash
pip install -r requirements.txt
```

### Run the notebook
1. Open Jupyter Notebook:
```bash
jupyter notebook
```

2. Select and run one of the notebooks:

- `cnn-cv-01.ipynb` for CNN model

- `vit-01.ipynb` for Vision Transformer model

- `YOLO` for YOLO pretrained model

### Note
- Make sure all data is loaded into the `data224x224/` folder
- Check that the GPU is installed and working properly
- Parameters in the notebook may need to be adjusted depending on the configuration computer.