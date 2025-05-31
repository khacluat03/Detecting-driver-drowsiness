# Group 15: PHÁT HIỆN TÀI XẾ BUỒN NGỦ VÀ MẤT TẬP TRUNG KHI LÁI XE

## Giới thiệu
Dự án là đồ án cuối kỳ môn `Thị giác máy tính` của nhóm 15. Dự án tập trung vào việc phát triển một hệ thống phát hiện buồn ngủ và mất tập trung khi lái xe bằng cách sử dụng ba mô hình deep learning khác nhau: YOLO, CNN (Convolutional Neural Network) và ViT (Vision Transformer). Khi phát hiện tài xế buồn ngủ hệ thống sẽ cảnh báo bằng cách phát ra âm thanh.

## Thành viên:
- Nguyễn Khắc Luật – 21099741 
- Hoàng Ngọc Tân - 21074741
- Nguyễn Thị Ty Ty - 21096511 

## Cấu trúc file
- `training_code/cnn-cv-01.ipynb`: Notebook huấn luyện mô hình CNN
- `training_code/vit-01.ipynb`: Notebook huấn luyện mô hình Vision Transformer
- `training_code/CodeTrainYolo.ipynb`: Huấn luyện mô hình YOLO với [dữ liệu](https://www.kaggle.com/datasets/nguyenluatdev/data-computer-vision)
- `link.txt`: chứa các notebook huấn luyện và dataset cần thiết liên quan đến dự án
- `Report_Group15_ComputerVision.pdf`: Báo cáo chi tiết về dự án
- `Slide_Group15_ComputerVision.pdf`: Slide thuyết trình

## Bạn có thể sử dụng bộ dữ liệu để huấn luyện YOLO thông qua API đã gắn nhãn từ Roboflow
```python
from roboflow import Roboflow
rf = Roboflow(api_key="tOfbkzltAMQMayGo8I3p")
project = rf.workspace("luatluat").project("final2-kwf46-fkead")
version = project.version(2)
dataset = version.download("yolov11")
```

## Link Kaggle
Các notebook huấn luyện mô hình có thể được tìm thấy tại:
- Vision Transformer (ViT): [notebook](https://www.kaggle.com/code/ngctnhong/vit-01)
- CNN: [notebook](https://www.kaggle.com/code/ngctnhong/cnn-cv-01)
- YOLO: [notebook](https://colab.research.google.com/drive/1FHDNQxvbh8P5Oj6rV6-kSXyojLdgtNHP?usp=sharing)

## Mục tiêu
- Phát hiện buồn ngủ của người lái xe
- Phát hiện hành vi mất tập trung khi lái xe
- Cảnh báo kịp thời để đảm bảo an toàn giao thông

## Công nghệ sử dụng
- Python
- Deep Learning
- Computer Vision
- CNN (Convolutional Neural Network)
- ViT (Vision Transformer)
- YOLO (ultralytics)

## Hướng dẫn cài đặt và chạy

### Yêu cầu hệ thống
- Python 3.8 trở lên
- GPU tương thích với CUDA (khuyến nghị cho việc huấn luyện mô hình)

### Thiết lập môi trường
1. Clone repository:
```bash
git clone https://github.com/khacluat03/final-project-computer-vision.git
cd final-project-computer-vision
```

2. Tạo môi trường ảo (khuyến nghị):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### Chạy notebook
1. Mở Jupyter Notebook:
```bash
jupyter notebook
```

2. Chọn và chạy một trong các notebook:
- `cnn-cv-01.ipynb` cho mô hình CNN
- `vit-01.ipynb` cho mô hình Vision Transformer
- `YOLO` cho mô hình YOLO đã được huấn luyện trước

### Lưu ý
- Đảm bảo tất cả dữ liệu được tải vào thư mục `data224x224/`
- Kiểm tra GPU đã được cài đặt và hoạt động đúng
- Các tham số trong notebook có thể cần được điều chỉnh tùy thuộc vào cấu hình máy tính.

## Tài liệu tham khảo:
[1]. Khandave,  A.  (2020,  September  20).  *Driver  drowsiness  detection  alert  system  with Open-CV & Keras using IP-WebCam for camera connection.* Retrieved from [https://www.linkedin.com/pulse/driver-drowsiness-detection-alert-system-open-cv-keras-khandave/]
[2]. Sahayadhas, A., Sundaraj, K., & Murugappan, M. (2012). *Detecting driver drowsiness based on sensors: A review.* Sensors, 12(12), 16937–16953. [https://doi.org/10.3390/s121216937](https://doi.org/10.3390/s121216937)
[3]. Díaz-Santos, S., Cigala-Álvarez, Ó., Gonzalez-Sosa, E., Caballero-Gil, P., & Caballero-Gil,  C.  (2024). *Driver  identification  and  detection  of  drowsiness  while  driving.*  Applied Sciences, 14(6), 2603. [https://www.mdpi.com/2076-3417/14/6/2603](https://www.mdpi.com/2076-3417/14/6/2603)
[4]. Alshaqaqi, B., Baquhaizel, A. S., Ouis, M. E. A., Boumehed, M., Ouamri, A., & Keche, M. (2013). *Driver drowsiness detection system.* Trong 2013 8th International Workshop on Systems, Signal Processing and their Applications (WoSSPA). IEEE.
[5]. Liu, C. C., Hosking, S. G., & Lenné, M. G. (2009). *Predicting driver drowsiness using vehicle measures: Recent insights and future challenges.* Journal of Sleep Research, 18(3), 239-253. [https://doi.org/10.1016/j.jsr.2009.04.005](https://doi.org/10.1016/j.jsr.2009.04.005)
[6]. Vural, E., Cetin, M., Ercil, A., Littlewort, G., Bartlett, M., & Movellan, J. (n.d.). *Drowsy Driver  Detection  Through  Facial  Movement  Analysis.*  Sabanci  University;  University  of California San Diego. 
[7]. Grace, R., Byrne, V. E., Bierman, D. M., Legrand, J.-M., Gricourt, D., & Davis, B. K. (1998). *A drowsy driver detection system for heavy vehicles.* In 17th DASC. AIAA/IEEE/SAE. Digital Avionics Systems Conference. Proceedings (Cat. No.98CH36267). IEEE.
[8]. Zhang, H., Liu, T., Lyu, J., & Chen, D. (2023). *Integrate memory mechanism in multi-granularity deep framework for driver drowsiness detection.* Intelligence & Robotics, 3(4), 614-631. https://doi.org/10.20517/ir.2023.34 