🏏 Hand Cricket Game (AI + Flask + OpenCV + Mediapipe)
📌 Overview

A Hand Cricket Game 🎮 powered by AI-based hand recognition, built using Flask, OpenCV, and Mediapipe.
Play cricket using just your hand gestures ✋ via webcam — no keyboard required!
The system tracks your moves in real-time, updates the score 🏏, plays sound effects 🔊, and announces whether you Win 🎉 or Lose ❌.

✨ Features

🤖 AI Hand Gesture Recognition (Mediapipe)

⚡ Automatic Score Detection — no button clicks needed

🔊 Sound Effects

score.mp3 → When you score runs

out.mp3 → When you get out

win.mp3 → When you win the game

🎥 Live Webcam Feed (Flask + OpenCV Streaming)

🎨 Colorful & Interactive UI (HTML + CSS + JS)

🏆 Game End Alerts → Declares winner or loser

📂 Project Structure
HAND_CRICKET/
│
├── app.py               # Flask backend
├── hand_utils.py        # Hand recognition + cricket logic
├── requirements.txt     # Dependencies
│
├── templates/
│   └── index.html       # Main frontend page
│
├── static/
│   ├── scripts.js       # JavaScript logic
│   └── style.css        # CSS styling
│
└── sounds/              # Sound effects
    ├── out.mp3
    ├── score.mp3
    └── win.mp3

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/hand-cricket.git
cd hand-cricket

2️⃣ Create Virtual Environment
python -m venv venv
# Activate:
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser

👉 http://127.0.0.1:5000

🕹️ How to Play

✋ Show your hand in front of the webcam.

☝️ 1 finger → Run = 1

✌️ 2 fingers → Run = 2

… up to 6 fingers

🤖 Computer randomly chooses a number.

If both match → OUT ❌

Otherwise, your score increases ✅

🏆 Game ends when:

You get OUT, or

You reach the target (Win 🎉)

📸 Screenshots

📷 Add gameplay screenshots here once you capture them.

🚀 Tech Stack

Backend → Flask

Frontend → HTML, CSS, JavaScript

AI/ML → Mediapipe (Hand Tracking)

Computer Vision → OpenCV

Audio → HTML5 <audio> + JS

🎯 Future Improvements

👥 Multiplayer Mode

📱 Mobile-Friendly UI

🎚️ Difficulty Levels

📊 Scoreboard History

🙌 Acknowledgements

🤝 Mediapipe
 → Hand Recognition

🤝 OpenCV
 → Computer Vision

🤝 Flask
 → Web Framework

✨ Developed with ❤️ for learning, fun, and innovation.
