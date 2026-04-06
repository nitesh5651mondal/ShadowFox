# 🧠 ShadowFox – AI Image Tagger

An AI-powered web application that classifies images into categories like **cat, dog, car, etc.** using deep learning. Built with a full-stack approach, combining a PyTorch-based model with a Flask web interface.

---

## 🚀 Features

* 📷 Upload any image via web UI
* 🧠 Real-time image classification using deep learning
* ⚡ Fast predictions using a trained CNN model
* 🌐 Simple and user-friendly interface
* 📦 Lightweight and easy to run locally

---

## 🏗️ Project Structure

```
ShadowFox/
└── image-tagger/
    └── backend/
        ├── app.py                # Flask backend server
        ├── model/
        │   ├── train.py          # Model training script
        │   └── model.pth         # Trained PyTorch model
        ├── utils/
        │   └── predict.py        # Prediction logic
        ├── templates/
        │   └── index.html        # Web UI
        ├── static/
        │   └── uploads/          # Uploaded images
        └── requirements.txt      # Dependencies
```

---

## 🧠 Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** PyTorch
* **Frontend:** HTML, CSS
* **Libraries:** torchvision, PIL, NumPy

---

## 📊 Model Details

* Dataset: CIFAR-10
* Architecture: Convolutional Neural Network (CNN)
* Classes:

  * airplane, car, bird, cat, deer
  * dog, frog, horse, ship, truck

---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```
git clone https://github.com/your-username/ShadowFox.git
cd ShadowFox/image-tagger/backend
```

---

### 🔹 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 🔹 3. Train Model (First Time Only)

```
cd model
python train.py
```

Move model:

```
move model.pth ..
```

---

### 🔹 4. Run Application

```
cd ..
python app.py
```

---

### 🌐 Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧪 How It Works

1. User uploads an image
2. Image is saved in `static/uploads`
3. Preprocessing is applied (resize, normalize)
4. PyTorch model predicts class
5. Result is displayed on UI

---

## 📸 Demo Flow

* Upload Image → Preview Displayed → Prediction Output

---

## ⚠️ Notes

* Ensure `model.pth` exists before running app
* Use `.jpg` or `.png` for best compatibility
* `static/uploads` folder must exist

---

## 🚀 Future Improvements

* 🎯 Use pretrained models (ResNet / MobileNet)
* 🎨 Improve UI with modern frameworks
* 🌍 Deploy on cloud (Render / AWS)
* 🧠 Add multi-object detection (YOLO)

---

## 💼 Resume Description

**ShadowFox – AI Image Tagging System**
Developed a deep learning-based web application using PyTorch and Flask to classify images into multiple categories with real-time predictions, integrating backend ML models with a user-friendly frontend.

---

## 👨‍💻 Author

Nitesh Mondal

---

## ⭐ Contribute

Feel free to fork this repo and enhance it!

---

## 📌 License

This project is open-source and free to use.
