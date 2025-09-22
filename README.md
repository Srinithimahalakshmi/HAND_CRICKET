
COMPUTER VISION-Powered Advanced Hand Cricket Game 🎮🏏

This project is an interactive hand cricket game powered by NLP and computer vision, allowing players to play cricket using hand gestures detected via a webcam. The game features strategy commands, power-ups, adaptive AI, multiplayer mode, customizable themes, score prediction, and save & resume functionality, providing a rich and immersive experience.

📂 Project Structure
Hand_Cricket_Game/
│
├── backend/
│   └── app.py                  # Flask application for game logic and AI integration
│
├── frontend/
│   ├── index.html              # HTML interface for the game
│   ├── style.css               # CSS styling
│   └── script.js               # JavaScript for front-end interactivity
│
├── sounds/
│   ├── hit.wav                 # Sound effect for hitting
│   ├── wicket.wav              # Sound effect for losing a wicket
│   └── cheer.wav               # Crowd cheering sound
│
├── models/
│   └── hand_recognition_model.pkl # Pretrained hand gesture detection model
│
├── datasets/
│   └── hand_images/            # Dataset used for training hand gestures
│
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
🎯 Features

Hand Gesture Detection: Detects gestures like open hand, fist, and numbers to play cricket.

NLP Commands: Players can input strategy commands using text or voice.

Score Prediction: Predicts possible scores based on AI and player strategy.

Multiplayer Mode: Play with friends on the same system.

Power-ups & Surprises: Random events to make gameplay dynamic.

Customizable Themes: Change game appearance and sound effects.

Save & Resume: Continue your game from where you left off.

⚙️ Technology Stack

Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

Machine Learning: Hand gesture recognition using OpenCV & TensorFlow

Audio Effects: WAV sound integration

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 How to Run

Clone the repository:

git clone https://github.com/Srinithimahalakshmi/Hand_Cricket_Game.git
cd Hand_Cricket_Game


Install dependencies:

pip install -r requirements.txt


Run the Flask backend:

python backend/app.py


Open your browser and go to:

http://127.0.0.1:5000


Play the game using hand gestures and enjoy! 🎮🏏
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📈 Results

Real-time hand gesture recognition for scoring and wickets

Smooth gameplay with interactive sounds

Adaptive AI challenges for single-player mode

Multiplayer mode tested successfully with responsive score updates
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📚 References

OpenCV Hand Gesture Recognition

TensorFlow & Keras Documentation

Research on NLP in Gaming Strategy Commands

WAV sound integration tutorials for Python
