"""
SentiGen - Sentiment-Driven Text Generator
A portfolio project demonstrating ML text generation with sentiment analysis
"""

import streamlit as st
from src.sentiment_analyzer import SentimentAnalyzer
from src.text_generator import TextGenerator
import time

# Page configuration
st.set_page_config(
    page_title="SentiGen - AI Text Generator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .sentiment-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .positive-box {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
    }
    .negative-box {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
    }
    .neutral-box {
        background-color: #d1ecf1;
        border-left: 5px solid #17a2b8;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize models (with caching for performance)
@st.cache_resource
def load_models():
    """Load models once and cache them"""
    with st.spinner("🚀 Loading AI models... (first time takes ~30 seconds)"):
        analyzer = SentimentAnalyzer()
        generator = TextGenerator()
    return analyzer, generator

# Load models
analyzer, generator = load_models()

# Header
st.markdown('<h1 class="main-header">✨ SentiGen</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Sentiment-Driven Text Generator</p>', unsafe_allow_html=True)

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Manual sentiment override
    auto_detect = st.checkbox("Auto-detect sentiment", value=True)
    
    if not auto_detect:
        manual_sentiment = st.selectbox(
            "Select sentiment:",
            ["positive", "negative", "neutral"]
        )
    
    # Text length control
    st.subheader("📏 Text Length")
    num_sentences = st.slider(
        "Number of sentences:",
        min_value=2,
        max_value=10,
        value=5,
        help="Approximate number of sentences to generate"
    )
    
    # Creativity control
    st.subheader("🎨 Creativity")
    temperature = st.slider(
        "Temperature:",
        min_value=0.5,
        max_value=1.5,
        value=0.8,
        step=0.1,
        help="Higher values = more creative but less predictable"
    )
    
    # Info section
    st.markdown("---")
    st.subheader("ℹ️ How it works")
    st.markdown("""
    1. **Enter** your prompt
    2. **Detect** sentiment (or choose manually)
    3. **Generate** sentiment-aligned text
    4. **Enjoy** your AI-generated content!
    """)
    
    st.markdown("---")
    st.caption("Built with 💜 using Transformers & Streamlit")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Your Prompt")
    
    # Example prompts
    example_prompts = [
        "a day at the beach",
        "the future of technology",
        "my favorite childhood memory",
        "working from home",
        "learning something new"
    ]
    
    with st.expander("💡 Need inspiration? Try these examples"):
        for example in example_prompts:
            if st.button(f"📌 {example}", key=example):
                st.session_state.prompt_input = example
    
    # Text input
    user_prompt = st.text_area(
        "Enter your prompt:",
        value=st.session_state.get('prompt_input', ''),
        height=150,
        placeholder="e.g., 'a sunny day in the park' or 'facing challenges at work'",
        help="Describe what you want the AI to write about"
    )
    
    # Generate button
    generate_button = st.button("🚀 Generate Text", type="primary", use_container_width=True)

with col2:
    st.subheader("🎯 Results")
    
    if generate_button:
        if not user_prompt.strip():
            st.warning("⚠️ Please enter a prompt first!")
        else:
            # Step 1: Sentiment Analysis
            with st.spinner("🔍 Analyzing sentiment..."):
                sentiment_result = analyzer.analyze(user_prompt)
                detected_sentiment = analyzer.get_sentiment_label(user_prompt)
                time.sleep(0.5)  # Small delay for UX
            
            # Display sentiment
            sentiment_colors = {
                'positive': 'positive-box',
                'negative': 'negative-box',
                'neutral': 'neutral-box'
            }
            
            sentiment_emojis = {
                'positive': '😊',
                'negative': '😔',
                'neutral': '😐'
            }
            
            final_sentiment = manual_sentiment if not auto_detect else detected_sentiment
            
            st.markdown(
                f'<div class="sentiment-box {sentiment_colors[final_sentiment]}">'
                f'<strong>Detected Sentiment:</strong> {sentiment_emojis[final_sentiment]} '
                f'{final_sentiment.upper()} '
                f'<span style="color: #666;">(Confidence: {sentiment_result["confidence"]:.2%})</span>'
                f'</div>',
                unsafe_allow_html=True
            )
            
            # Step 2: Text Generation
            with st.spinner("✍️ Generating your text... (this may take 10-20 seconds)"):
                generated_text = generator.generate(
                    prompt=user_prompt,
                    sentiment=final_sentiment,
                    max_length=num_sentences * 20 + 50,
                    temperature=temperature
                )
            
            # Display generated text
            st.success("✅ Generation complete!")
            st.markdown("### 📄 Generated Text:")
            st.markdown(f"<div style='background-color: #f8f9fa; padding: 1.5rem; border-radius: 10px; line-height: 1.8;'>{generated_text}</div>", unsafe_allow_html=True)
            
            # Download button
            st.download_button(
                label="💾 Download as TXT",
                data=generated_text,
                file_name="sentigen_output.txt",
                mime="text/plain"
            )
            
            # Metrics
            word_count = len(generated_text.split())
            char_count = len(generated_text)
            
            metric_col1, metric_col2, metric_col3 = st.columns(3)
            with metric_col1:
                st.metric("Words", word_count)
            with metric_col2:
                st.metric("Characters", char_count)
            with metric_col3:
                st.metric("Sentiment", final_sentiment.upper())

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>SentiGen</strong> - Demonstrating sentiment analysis + text generation</p>
    <p>Models: DistilBERT (sentiment) + GPT-2 Medium (generation)</p>
</div>
""", unsafe_allow_html=True)