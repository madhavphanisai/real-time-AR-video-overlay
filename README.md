# 🎥 Real-Time-AR-Video-Overlay  
Augmented Reality project that overlays a video on a detected target image in real time using **Python + OpenCV**.  

---

## 🚀 Overview  
This project demonstrates how to blend **computer vision** and **augmented reality** by detecting a reference image (marker) and projecting a video onto it in real time.  

It uses:  
- **OpenCV** for feature detection & matching  
- **NumPy** for matrix operations  
- **VideoCapture** for handling real-time frames  

---

## 📂 Project Structure  
```

real-time-AR-video-overlay/
├── main.py            # Main project code
├── targetIMG.jpg      # Target image for detection
├── targetVid.mp4      # Video to overlay on target
├── requirements.txt   # Python dependencies

````

---

## ⚙️ Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/madhavphanisai/real-time-AR-video-overlay.git
   cd real-time-AR-video-overlay
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 requirements.txt

```txt
opencv-python
numpy
```

---

## ▶️ Usage

Run the project with:

```bash
python main.py
```

* Hold the **target image (targetIMG.jpg)** in front of your camera.
* The **video (targetVid.mp4)** will overlay on top of the detected image in real-time.

## 💡 Future Improvements

* Support multiple target images.
* Add 3D object overlay.
* Optimize for mobile devices.

---
## 🤝 Connect with Me

👨‍💻 Developed by **Madhav Phani Sai**
🔗 [LinkedIn](https://www.linkedin.com/in/madhavphanisai)
