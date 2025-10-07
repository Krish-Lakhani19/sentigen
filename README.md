# 🌟 SentiGen - Sentiment-Driven AI Text Generator

An intelligent text generation system that creates sentiment-aligned content using state-of-the-art NLP models.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Transformers](https://img.shields.io/badge/Transformers-4.35.0-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Project Overview

SentiGen is a machine learning application that:
- Analyzes the sentiment of user input prompts (positive, negative, neutral)
- Generates coherent, contextually relevant text aligned with detected sentiment
- Provides an interactive web interface for real-time text generation

**Live Demo:** [Coming Soon - Deployment Link]

## ✨ Features

- **Automatic Sentiment Detection**: Uses DistilBERT to analyze input sentiment with confidence scores
- **Sentiment-Aware Generation**: GPT-2 Medium model generates text matching the detected sentiment
- **Manual Override**: Option to manually select desired sentiment
- **Customizable Output**: 
  - Adjustable text length (2-10 sentences)
  - Temperature control for creativity (0.5-1.5)
- **Beautiful UI**: Clean, modern interface with gradient styling
- **Export Function**: Download generated text as .txt files
- **Real-time Metrics**: Word count, character count, and sentiment display

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Sentiment Analysis** | DistilBERT (distilbert-base-uncased-finetuned-sst-2-english) |
| **Text Generation** | GPT-2 Medium |
| **ML Framework** | PyTorch + Hugging Face Transformers |
| **Frontend** | Streamlit |
| **Language** | Python 3.10 |

## 📋 Prerequisites

- Python 3.10 or 3.11
- 4GB+ RAM (8GB recommended)
- 2GB free disk space (for models)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/sentigen.git
cd sentigen

2. Create Virtual Environment
Using Conda (Recommended): 
```bash
conda create -n sentigen python=3.10 -y
conda activate sentigen

Using venv:
```bash
bashpython3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# venv\Scripts\activate  # On Windows

3. Install Dependencies
```bash
# Install PyTorch
conda install pytorch torchvision -c pytorch -y  # If using conda

# Install other packages
pip install -r requirements.txt

4. Run the Application
```bash
streamlit run app.py
The app will open automatically at http://localhost:8501
📖 How It Works
Architecture
User Input → Sentiment Analyzer → Text Generator → Output Display
     ↓              ↓                    ↓              ↓
  Prompt      DistilBERT           GPT-2 Medium    Streamlit UI
Workflow

Input Processing: User enters a text prompt
Sentiment Analysis: DistilBERT classifies sentiment (positive/negative/neutral)
Prompt Engineering: System adds sentiment-appropriate prefix to guide generation
Text Generation: GPT-2 generates coherent text matching the sentiment
Output Display: Results shown with metrics and download option

Sentiment Conditioning
The system uses predefined prompt templates to guide text generation:

Positive: "This is wonderful because...", "I'm so happy that..."
Negative: "This is disappointing because...", "Unfortunately..."
Neutral: "It is worth noting that...", "From an objective perspective..."

🎮 Usage Examples
Example 1: Positive Generation
Input: "summer vacation at the beach"
Detected Sentiment: POSITIVE (98% confidence)
Output: "This is wonderful because summer vacation at the beach brings 
         endless joy and relaxation. The warm sun, gentle waves, and 
         golden sand create perfect memories..."
Example 2: Negative Generation
Input: "dealing with Monday morning traffic"
Detected Sentiment: NEGATIVE (95% confidence)
Output: "This is disappointing because dealing with Monday morning traffic 
         drains energy and patience. The endless queues and honking horns 
         make for a frustrating start..."
⚙️ Configuration Options
ParameterRangeDefaultDescriptionSentences2-105Approximate number of sentencesTemperature0.5-1.50.8Creativity level (higher = more creative)Auto-detectOn/OffOnAutomatic sentiment detection
📁 Project Structure
sentigen/
├── app.py                      # Main Streamlit application
├── src/
│   ├── __init__.py
│   ├── sentiment_analyzer.py  # Sentiment analysis module
│   └── text_generator.py      # Text generation module
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
└── docs/                       # Additional documentation
🧪 Testing
Run the test scripts to verify components:
bash# Test sentiment analyzer
python test_sentiment_analyzer.py

# Test text generator
python test_generator.py
🚧 Challenges & Solutions
Challenge 1: Sentiment-Text Alignment
Problem: Generated text didn't always match detected sentiment
Solution: Implemented sentiment-specific prompt templates that guide the model's generation process
Challenge 2: Generation Coherence
Problem: Output sometimes rambled or lost context
Solution: Fine-tuned temperature and top-p sampling parameters; limited max length based on desired sentence count
Challenge 3: Model Loading Time
Problem: First-time model downloads took too long
Solution: Added Streamlit caching with @st.cache_resource to load models once and reuse
Challenge 4: Neutral Sentiment Detection
Problem: Model was too binary (only positive/negative)
Solution: Added confidence threshold (<0.6) to classify uncertain predictions as neutral
🔮 Future Enhancements

 Support for multiple languages
 Fine-tune GPT-2 on sentiment-specific datasets
 Add more generation styles (formal, casual, creative)
 Implement user authentication and history
 Add A/B testing for different generation strategies
 Support longer form content (articles, stories)
 Add emotion detection beyond basic sentiment

📊 Model Performance
ModelTaskAccuracySpeedDistilBERTSentiment Analysis~95%<1sGPT-2 MediumText GenerationN/A10-20s
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
📄 License
This project is licensed under the MIT License.
👨‍💻 Author
Krish Lakhani

GitHub: @Krish-Lakhani19
LinkedIn: https://www.linkedin.com/in/krishlakhani19
Email: krishlakhani46767@gmail.com

🙏 Acknowledgments

Hugging Face for the incredible Transformers library
Streamlit for the intuitive web framework
The open-source ML community