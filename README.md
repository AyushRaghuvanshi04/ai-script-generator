# 🎬 AI Script Generator

A Streamlit web application that generates creative and engaging Reel/Ad scripts using a fine-tuned ChatGPT model. Perfect for content creators, marketers, and businesses looking to create compelling video scripts quickly.

![Demo](https://img.shields.io/badge/Demo-Live-brightgreen)
![GitHub last commit](https://img.shields.io/github/last-commit/AyushRaghuvanshi04/ai-script-generator)
![GitHub repo size](https://img.shields.io/github/repo-size/AyushRaghuvanshi04/ai-script-generator)

## ✨ Features

- **AI-Powered Script Generation**: Utilizes a fine-tuned GPT-4.1 Nano model for high-quality script generation
- **User-Friendly Interface**: Simple and intuitive form-based input 
- **Dual View Display**: View scripts in both text area (for easy copying) and formatted markdown
- **Responsive Design**: Works on both desktop and mobile devices
- **Customizable Inputs**: Tailor scripts with specific app details, target audience, and goals

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for the fine-tuned model)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AyushRaghuvanshi04/ai-script-generator.git
   cd ai-script-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Create a `.streamlit/secrets.toml` file
   - Add your OpenAI API key:
     ```toml
     OPENAI_API_KEY = "your-openai-api-key-here"
     ```

### Running the Application

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`

## 🛠️ How It Works

1. Enter your app/product details in the form
2. Specify your target audience
3. Set your goal/purpose for the script
4. Click "Generate Script"
5. Copy the generated script or view it in formatted markdown

## 🧠 Fine-Tuned Model

This application uses a custom fine-tuned GPT-4.1 Nano model specifically trained for generating engaging and creative video scripts. The model ID is:

```
ft:gpt-4.1-nano-2025-04-14:personal:3-content-script-generator:Bvj2a1H5
```

## 📝 Example Usage

### Input:
- **App Description**: A language learning app with gamified lessons
- **Target Audience**: Young professionals aged 20-35
- **Goal**: Create an engaging Instagram Reel script

### Output:
```
[Visual: Creator looking at a foreign menu, looking confused]
[Text: "Struggling to order food in a new country? I was too! 😅"]

[Visual: Pulling out phone with the app open]
[Text: "Then I discovered [App Name] - my pocket language tutor!"]

[Visual: Quick cuts of fun lessons and challenges]
[Text: "5 minutes a day and I was ordering like a local! 🎉"]

[CTA: "Swipe up to start your language journey today! 🌍"]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI](https://openai.com/)
- Fine-tuned model by [Ayush Raghuvanshi]
