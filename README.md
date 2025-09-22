



# 🤖 Computer Vision-Powered Hand Cricket 🎯

This project is an **interactive hand cricket game** that leverages **advanced computer vision techniques** to detect real-time hand gestures via a webcam, enabling players to hit, bowl, and score runs without any physical controller. The system uses **OpenCV and deep learning models** to recognize gestures such as open hand, fist, and finger counts, converting them into cricket actions such as runs, wickets, and special moves. Combined with **NLP-powered strategy commands and adaptive AI**, it provides an immersive, responsive, and intelligent gaming experience for both single and multiplayer modes.

---

## 📂 Project Structure

The project is organized into separate directories to maintain a clear structure and ensure easy development, debugging, and deployment:

```
Hand_Cricket_Game/
│
├── backend/
│   └── app.py                  # Contains the Flask backend logic for gesture recognition, NLP command processing, AI opponent behavior, and game state management.
│
├── frontend/
│   ├── index.html              # The main HTML page providing the user interface for the game, including buttons, score display, and instructions.
│   ├── style.css               # CSS file for styling the game interface with responsive design and theme customization.
│   └── script.js               # JavaScript for handling UI interactions, score updates, animations, and communication with the Flask backend.
│
├── sounds/
│   ├── hit.wav                 # Sound effect triggered when the player hits the ball.
│   ├── wicket.wav              # Sound effect triggered when a wicket falls.
│   └── cheer.wav               # Crowd cheering sound to enhance the gameplay experience.
│
├── models/
│   └── hand_recognition_model.pkl # Pre-trained deep learning model for recognizing hand gestures accurately in real-time.
│
├── datasets/
│   └── hand_images/            # Dataset containing hand gesture images used for training the gesture recognition model.
│
├── README.md                   # Project documentation detailing features, setup, and usage instructions.
└── requirements.txt            # Python dependencies required to run the project.
```

---

## 🎯 Features

The game includes a wide variety of features designed to make gameplay **fun, interactive, and intelligent**, catering to both casual players and competitive users:

* **Real-Time Hand Gesture Detection:** Detects multiple hand gestures in real time to determine game actions like hitting, bowling, or scoring runs.
* **NLP Strategy Commands:** Players can use natural language text or voice commands to instruct AI teammates or opponents, enhancing interactivity.
* **Score Prediction & AI Adaptation:** The system predicts possible runs and adjusts AI difficulty dynamically based on the player’s performance and strategy.
* **Multiplayer Mode:** Supports multiple players on the same system, enabling competitive or cooperative gameplay.
* **Power-Ups & Random Events:** Introduces surprises, bonuses, and special moves to make gameplay more engaging and less predictable.
* **Customizable Themes & Sounds:** Users can switch between different game themes, background visuals, and sound effects for a personalized experience.
* **Save & Resume Functionality:** Allows users to save their game state and resume later, ensuring longer gameplay sessions without losing progress.

---

## 🖥️ Computer Vision Module

The core of the game is **computer vision-powered hand gesture recognition**, enabling seamless controller-free gameplay. This module ensures **fast and accurate detection of hand movements** and integrates them directly with the game logic:

* **Hand Detection:** Locates hands within the webcam frame using advanced contour detection and landmark estimation algorithms.
* **Gesture Recognition:** Classifies gestures such as open hand, fist, or specific finger counts using a trained machine learning/deep learning model, mapping them to in-game actions like runs or wickets.
* **Real-Time Processing:** Optimized to minimize latency, ensuring smooth and responsive gameplay without lag or missed gestures.
* **Integration with Game Logic:** Recognized gestures are converted into immediate game events, including score updates, power-ups, or wickets, creating a seamless interaction between the player and the AI system.

**Advantages:**

* Provides a **controller-free experience**, allowing natural interaction using hand movements.
* Enhances player engagement with **real-time visual feedback and sound effects**.
* Works **seamlessly with NLP commands and AI-driven gameplay** to provide a full-featured, intelligent gaming environment.

---

## ⚙️ Technology Stack

The project combines multiple technologies to create a **robust, real-time interactive gaming system**:

* **Frontend:** HTML, CSS, JavaScript for responsive UI, animations, and interactive components.
* **Backend:** Python and Flask to handle gesture recognition, AI logic, NLP commands, and game state management.
* **Machine Learning & Computer Vision:** OpenCV and TensorFlow for real-time hand gesture detection and classification.
* **Audio Integration:** WAV sound files for hit, wicket, and cheering effects to make the gameplay immersive.
* **Natural Language Processing (NLP):** Processes player strategy commands, allowing intelligent AI responses and improved game dynamics.

---

## 🚀 How to Run

Follow these steps to run the game locally:

1. **Clone the repository:**

```bash
git clone https://github.com/Srinithimahalakshmi/Hand_Cricket_Game.git
cd Hand_Cricket_Game
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Flask backend:**

```bash
python backend/app.py
```

4. **Open your browser** and navigate to:

```
http://127.0.0.1:5000
```

5. **Play the game** using hand gestures, NLP commands, and enjoy the interactive cricket experience. 🎮🏏

---

## 📈 Results

The game demonstrates **real-time hand gesture recognition** integrated with a full-featured cricket gameplay system:

* Accurate detection of hand gestures and finger counts for runs and wickets.
* Smooth gameplay with interactive audio cues for hits, wickets, and cheering.
* Adaptive AI provides increasing challenge and intelligent score prediction.
* Multiplayer mode successfully tested with real-time score updates and power-ups.
* Positive feedback on user engagement due to controller-free and interactive experience.

---

## 📚 References

* [OpenCV Hand Gesture Recognition](https://opencv.org/)
* [TensorFlow & Keras Documentation](https://www.tensorflow.org/)
* Research on NLP in Gaming Strategy Commands
* WAV sound integration tutorials for Python

---


