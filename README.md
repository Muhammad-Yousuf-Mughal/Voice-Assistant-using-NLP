# Aurora — AI Voice Assistant 🎙️✨

Aurora is a sleek, real-time AI-powered voice assistant web application designed to provide interactive, low-latency conversational AI experiences directly in the browser. Powered by a **FastAPI** backend integrated with the **Groq Cloud SDK** and deployed on **Vercel**, Aurora leverages continuous speech recognition and text-to-speech synthesis for seamless hands-free interaction.

🚀 **Live Application:** https://voice-assistant-using-nlp.vercel.app/

---

## 🌟 Key Features

* **Continuous Voice Interaction:** Hands-free listening with automated silence detection and auto-response dispatch.
* **Ultra-Low Latency Inference:** Powered by Groq Cloud Llama models for high-speed response generation.
* **Interactive Visual Feedback:** Real-time visual status indicators (*Listening*, *Thinking*, *Speaking*, *Idle*) and visual activity animations.
* **Hybrid Input Support:** Seamlessly switch between voice input and text prompt submission.
* **Contextual Conversation History:** Retains session dialogue memory for coherent multi-turn conversations.
* **Responsive Modern UI:** Modern glassmorphism UI styled with clean CSS and custom animations, optimized across desktop viewports.

---

## 🛠️ Tech Stack & Architecture

### **Frontend**
* **HTML5 / Modern CSS3:** Custom styling featuring responsive glassmorphism containers and dynamic activity animations.
* **Vanilla JavaScript (ES6+):** Async state management, DOM rendering, and API fetch handlers.
* **Web Speech API:** Utilizes native `SpeechRecognition` / `webkitSpeechRecognition` for speech-to-text and `SpeechSynthesis` for audio playback.

### **Backend & Cloud Infrastructure**
* **Python 3.10+ & FastAPI:** Asynchronous API service handling JSON chat completion endpoints and context history.
* **Groq Cloud SDK:** High-performance Llama-3 inference backend delivering fast completion response times.
* **Vercel Serverless Functions:** Hosted and deployed on Vercel with seamless serverless entry points (`api/index.py`).

---

## 📁 Project Structure

```text
├── api/
│   └── index.py            # FastAPI application entry point for Vercel Serverless
├── public/
│   ├── index.html          # Web application UI & Web Speech JS logic
│   └── style.css           # Glassmorphism design and animation styles
├── .env.example            # Environment variables template
├── requirements.txt        # Python package dependencies
├── vercel.json             # Vercel deployment and rewrite routing configuration
└── README.md               # Project documentation
```

---

## ⚙️ Environment Variables

To run the project locally or deploy it to Vercel, you need to configure your Groq API key:

| Variable Name | Description | Required |
| :--- | :--- | :--- |
| `GROQ_API_KEY` | Your Groq Cloud API key for model completions | **Yes** |

---

## 🚀 Getting Started Locally

### Prerequisites
* **Python 3.10+** installed on your system.
* A free **Groq Cloud Account** with an API key generated from Groq Console.

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Muhammad-Yousuf-Mughal/voice-assistant-using-nlp.git](https://github.com/Muhammad-Yousuf-Mughal/voice-assistant-using-nlp.git)
   cd voice-assistant-using-nlp
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the project root directory and add your Groq API Key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

5. **Run the Development Server:**
   ```bash
   uvicorn api.index:app --reload --port 8000
   ```

6. **Access the Application:**
   Open your browser and navigate to `http://localhost:8000`.

---

## 🌐 Deployment on Vercel

This application is pre-configured for Vercel Serverless deployment using `vercel.json`.

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```
2. Deploy directly from your terminal:
   ```bash
   vercel
   ```
3. Add your `GROQ_API_KEY` in the **Vercel Project Settings -> Environment Variables**.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.
