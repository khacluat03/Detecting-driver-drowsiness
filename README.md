# Dự án Phát Hiện Buồn Ngủ và Mất Tập Trung Khi Lái Xe

## Giới thiệu
Dự án này tập trung vào việc phát triển một hệ thống phát hiện buồn ngủ và mất tập trung khi lái xe bằng cách sử dụng ba mô hình deep learning khác nhau: YOLO, CNN (Convolutional Neural Network) và ViT (Vision Transformer).

## Cấu trúc file
- `cnn-cv-01.ipynb`: Notebook huấn luyện mô hình CNN
- `vit-01.ipynb`: Notebook huấn luyện mô hình Vision Transformer
- `data224x224/`: Thư mục chứa dữ liệu ảnh đã xử lý (kích thước 224x224) [LINK](https://www.kaggle.com/datasets/nguyenluatdev/computer-vision-data224x224)
- `cv_report.docx`: Báo cáo chi tiết về dự án
- `group_15_slide_computer-vision.pptx`: Slide thuyết trình dự án
- `CodeTrainYolo`: Huấn luyện mô hình YOLO với [dữ liệu](https://www.kaggle.com/datasets/nguyenluatdev/data-computer-vision)

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
git clone [URL_REPOSITORY]
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