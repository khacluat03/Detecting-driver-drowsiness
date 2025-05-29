# Dự án Phát hiện Cảnh báo Buồn ngủ và Mất tập trung khi Lái xe

## Giới thiệu
Dự án này tập trung vào việc phát triển hệ thống phát hiện cảnh báo buồn ngủ và mất tập trung khi lái xe sử dụng hai mô hình học sâu khác nhau: CNN (Convolutional Neural Network) và ViT (Vision Transformer).

## Cấu trúc dự án
- `CNN_CV_01.ipynb`: Notebook triển khai mô hình CNN
- `ViT_CV_01.ipynb`: Notebook triển khai mô hình Vision Transformer
- `data224x224/`: Thư mục chứa dữ liệu hình ảnh đã được xử lý (kích thước 224x224)
- `cv_report.docx`: Báo cáo chi tiết về dự án
- `group_15_slide_computer-vision.pptx`: Slide thuyết trình về dự án

## Link Kaggle
Các notebook huấn luyện mô hình có thể được tìm thấy tại:
- Vision Transformer (ViT): https://www.kaggle.com/code/ngctnhong/vit-01
- CNN: https://www.kaggle.com/code/ngctnhong/cnn-cv-01

## Mục tiêu
- Phát hiện tình trạng buồn ngủ của người lái xe
- Phát hiện các hành vi mất tập trung khi lái xe
- Cảnh báo kịp thời để đảm bảo an toàn giao thông

## Công nghệ sử dụng
- Python
- Deep Learning
- Computer Vision
- CNN (Convolutional Neural Network)
- ViT (Vision Transformer)

## Hướng dẫn cài đặt và chạy

### Yêu cầu hệ thống
- Python 3.8 trở lên
- CUDA-compatible GPU (khuyến nghị cho việc huấn luyện mô hình)

### Cài đặt môi trường
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

### Cấu trúc thư mục dữ liệu
```
data224x224/
├── train/
│   ├── closed_eye/
│   ├── open_eye/
│   ├── looking_away/
│   └── yawning/
└── test/
    ├── closed_eye/
    ├── open_eye/
    ├── looking_away/
    └── yawning/
```

### Chạy notebook
1. Mở Jupyter Notebook:
```bash
jupyter notebook
```

2. Chọn và chạy một trong các notebook:
   - `cnn-cv-01.ipynb` cho mô hình CNN
   - `vit-01.ipynb` cho mô hình Vision Transformer

### Lưu ý
- Đảm bảo đã tải đầy đủ dữ liệu vào thư mục `data224x224/`
- Kiểm tra GPU đã được cài đặt và hoạt động đúng cách
- Có thể cần điều chỉnh các tham số trong notebook tùy theo cấu hình máy tính 