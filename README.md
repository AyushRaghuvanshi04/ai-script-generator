# 🎬 AI Script Generator

A powerful Streamlit web application that generates creative Reel/Ad scripts using a fine-tuned ChatGPT model. Perfect for content creators, marketers, and businesses looking to create engaging video content.

## ✨ Features

- **🤖 Fine-tuned AI Model**: Uses a custom-trained ChatGPT model specifically optimized for script generation
- **📝 User-friendly Interface**: Simple form-based input for app description, target audience, and goals
- **🎨 Dual Display Format**: 
  - Text area for easy copying and editing
  - Expandable formatted view for better readability
- **⚡ Real-time Generation**: Fast script generation with loading indicators
- **🔧 Error Handling**: Robust error handling with user-friendly messages

## 🚀 Demo

![AI Script Generator Demo](https://via.placeholder.com/800x400/4CAF50/FFFFFF?text=AI+Script+Generator+Demo)

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- OpenAI API key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AyushRaghuvanshi04/ai-script-generator.git
   cd ai-script-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   
   Create or update `.streamlit/secrets.toml` with your OpenAI API key:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   Navigate to `http://localhost:8501` to use the application.

## 📋 Usage

1. **Describe your app**: Enter a detailed description of your application or product
2. **Define target audience**: Specify who your content is aimed at
3. **Set your goal**: Describe what you want to achieve with the script
4. **Generate**: Click the "Generate Script" button
5. **Copy & Use**: Copy the generated script from the text area or view it in the formatted section

### Example Input

- **App Description**: "A fitness tracking app that helps users monitor their daily workouts and nutrition"
- **Target Audience**: "Health-conscious millennials aged 25-35"
- **Goal**: "Create an engaging Instagram Reel script to promote app downloads"

## 🔧 Configuration

### Fine-tuned Model

The application uses a custom fine-tuned ChatGPT model:
- **Model ID**: `ft:gpt-4.1-nano-2025-04-14:personal:3-content-script-generator:Bvj2a1H5`
- **Specialization**: Creative script writing for ads and social media content
- **Parameters**: 
  - Temperature: 0.7 (balanced creativity)
  - Max tokens: 1000

### Customization

You can modify the following parameters in `app.py`:

```python
response = client.chat.completions.create(
    model="your-fine-tuned-model-id",
    messages=[...],
    temperature=0.7,        # Adjust creativity (0.0-1.0)
    max_tokens=1000         # Adjust response length
)
```

## 📁 Project Structure

```
ai-script-generator/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── secrets.toml      # API key configuration
├── README.md             # Project documentation
└── .git/                 # Git repository
```

## 🔐 Security

- **API Key Protection**: Store your OpenAI API key in `.streamlit/secrets.toml`
- **Environment Variables**: For production, use environment variables instead of secrets.toml
- **Rate Limiting**: Consider implementing rate limiting for production use

## 🚀 Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your `OPENAI_API_KEY` in the Streamlit Cloud secrets management
4. Deploy!

### Local Production

```bash
# Install production dependencies
pip install -r requirements.txt

# Run with production settings
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## 📊 Dependencies

- **streamlit>=1.25.0**: Web application framework
- **openai>=1.0.0**: OpenAI API client

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the ChatGPT API
- Streamlit for the amazing web framework
- The open-source community for inspiration and support

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/AyushRaghuvanshi04/ai-script-generator/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your setup and the issue

## 🔄 Changelog

### v2.0.0 (Latest)
- ✅ Migrated from Gemini API to fine-tuned ChatGPT
- ✅ Improved script formatting and display
- ✅ Enhanced UI with dual view format
- ✅ Better error handling and user feedback

### v1.0.0
- ✅ Initial release with Gemini API integration
- ✅ Basic script generation functionality

---

**Made with ❤️ by [Ayush Raghuvanshi](https://github.com/AyushRaghuvanshi04)**
