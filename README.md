# DETECT DRIVER Drowsiness and Distraction While Driving

## Introduction
The project is the final project of the `Computer Vision` subject of group 15. The project focuses on developing a system to detect drowsiness and distraction while driving by using three different deep learning models: YOLO, CNN (Convolutional Neural Network) and ViT (Vision Transformer). When detecting a drowsy driver, the system will warn by emitting a sound.

## Members:
- Nguyen Khac Luat – 21099741
- Hoang Ngoc Tan - 21074741
- Nguyen Thi Ty Ty - 21096511

## File structure
- `training_code/cnn-cv-01.ipynb`: CNN model training notebook
- `training_code/vit-01.ipynb`: Vision Transformer model training notebook
- `training_code/CodeTrainYolo.ipynb`: YOLO model training with [data](https://www.kaggle.com/datasets/nguyenluatdev/data-computer-vision)
- `link.txt`: contains training notebooks and necessary datasets related to the project
- `Report_Group15_ComputerVision.pdf`: Detailed report about the project
- `Slide_Group15_ComputerVision.pdf`: Presentation slide program

## You can use the dataset to train YOLO via the labeled API from Roboflow
```python
from roboflow import Roboflow
rf = Roboflow(api_key="tOfbkzltAMQMayGo8I3p")
project = rf.workspace("luatluat").project("final2-kwf46-fkead")
version = project.version(2)
dataset = version.download("yolov11")
```

## Kaggle Link
Model training notebooks can be found at:
- Vision Transformer (ViT): [notebook](https://www.kaggle.com/code/ngctnhong/vit-01)
- CNN: [notebook](https://www.kaggle.com/code/ngctnhong/cnn-cv-01)
- YOLO: [notebook](https://colab.research.google.com/drive/1FHDNQxvbh8P5Oj6rV6-kSXyojLdgtNHP?usp=sharing)

## Objectives
- Detect driver drowsiness
- Detect distracted driving behavior
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
- Python 3.8 or higher
- GPU compatible with CUDA (recommended for model training)

### Environment setup
1. Clone repository:
```bash
git clone https://github.com/khacluat03/final-project-computer-vision.git
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

### Running the notebook
1. Open Jupyter Notebook:
```bash
jupyter notebook
```

2. Select and run one of the notebooks:
- `cnn-cv-01.ipynb` for CNN model
- `vit-01.ipynb` for Vision Transformer model
- `YOLO` for pre-trained YOLO model

### Note
- Make sure all data is loaded into the `data224x224/` directory
- Check that the GPU is installed and running correct
- The parameters in the notebook may need to be adjusted depending on the computer configuration.

## Tài liệu tham khảo:
[1]. Khandave,  A.  (2020,  September  20).  *Driver  drowsiness  detection  alert  system  with Open-CV & Keras using IP-WebCam for camera connection.* Retrieved from [https://www.linkedin.com/pulse/driver-drowsiness-detection-alert-system-open-cv-keras-khandave/]

[2]. Sahayadhas, A., Sundaraj, K., & Murugappan, M. (2012). *Detecting driver drowsiness based on sensors: A review.* Sensors, 12(12), 16937–16953. [https://doi.org/10.3390/s121216937](https://doi.org/10.3390/s121216937)

[3]. Díaz-Santos, S., Cigala-Álvarez, Ó., Gonzalez-Sosa, E., Caballero-Gil, P., & Caballero-Gil,  C.  (2024). *Driver  identification  and  detection  of  drowsiness  while  driving.*  Applied Sciences, 14(6), 2603. [https://www.mdpi.com/2076-3417/14/6/2603](https://www.mdpi.com/2076-3417/14/6/2603)

[4]. Alshaqaqi, B., Baquhaizel, A. S., Ouis, M. E. A., Boumehed, M., Ouamri, A., & Keche, M. (2013). *Driver drowsiness detection system.* Trong 2013 8th International Workshop on Systems, Signal Processing and their Applications (WoSSPA). IEEE.

[5]. Liu, C. C., Hosking, S. G., & Lenné, M. G. (2009). *Predicting driver drowsiness using vehicle measures: Recent insights and future challenges.* Journal of Sleep Research, 18(3), 239-253. [https://doi.org/10.1016/j.jsr.2009.04.005](https://doi.org/10.1016/j.jsr.2009.04.005)

[6]. Vural, E., Cetin, M., Ercil, A., Littlewort, G., Bartlett, M., & Movellan, J. (n.d.). *Drowsy Driver  Detection  Through  Facial  Movement  Analysis.*  Sabanci  University;  University  of California San Diego. 
[7]. Grace, R., Byrne, V. E., Bierman, D. M., Legrand, J.-M., Gricourt, D., & Davis, B. K. (1998). *A drowsy driver detection system for heavy vehicles.* In 17th DASC. AIAA/IEEE/SAE. Digital Avionics Systems Conference. Proceedings (Cat. No.98CH36267). IEEE.

[8]. Zhang, H., Liu, T., Lyu, J., & Chen, D. (2023). *Integrate memory mechanism in multi-granularity deep framework for driver drowsiness detection.* Intelligence & Robotics, 3(4), 614-631. [https://doi.org/10.20517/ir.2023.34](https://doi.org/10.20517/ir.2023.34)
