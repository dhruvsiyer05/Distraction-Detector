# Distraction Detector

A real-time distraction detection system that helps improve focus while working by detecting common distractions (like phones, gaming controllers, etc.) through your webcam! Essentially, this AI-powered tool signals when a distraction is detected through a beeping sound, helping you stay on track while working or studying.

Includes:
- **Custom Object Detection Model:** Trained using TensorFlow 2 to detect various distractions with high accuracy.
- **Real-Time Inference:** Leverages OpenCV for real-time video processing through your webcam, and uses PyGame to provide audio alerts when distractions are detected!
- **Scalable Dataset:** Collected and annotated a diverse dataset of over 1,000 images using data augmentation techniques and web scraping to ensure accuracy across various scenarios; you never hold a phone or something else in the exact same angle or position when casually using it!

Will be implemented soon:
- **Flexible Configuration:** Be able to customize the sensitivity of the distraction detection to suit the working environment you're in! This includes a time-sensitive tracker for how many times you've been distracted within a given timeframe.

### Installation

Installation of this application should be fairly quick, just follow the steps below.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/dhruvsiyer05/distraction-detector.git
   cd distraction-detector

2. **Make sure you download the necessary dependencies, do this easily by:**
   ```bash
   pip install -r requirements.txt

3. **Now, just run the application by running the python script utilized for detection! The custom model and everything else is already pre-installed.**
   python distraction_detector.py

   
   
