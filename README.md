# 📄 AI Document Summarizer

An intelligent text summarization tool powered by Facebook's BART transformer model.

## 🚀 Live Demo
[Try it here](https://huggingface.co/spaces/naveentk/ai-text-summarizer)

## ✨ Features
- **Smart Summarization**: Uses state-of-the-art BART model from Facebook AI
- **Long Document Support**: Handles documents up to 2000+ words with automatic chunking
- **Real-time Processing**: Get summaries in seconds
- **Compression Metrics**: See original vs summary word count and compression percentage
- **Clean UI**: Simple, intuitive interface built with Streamlit

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Model**: Facebook BART (bart-large-cnn)
- **Framework**: Hugging Face Transformers
- **Backend**: PyTorch

## 📊 Performance
- Achieves 85-90% text compression
- Maintains key information with high ROUGE scores
- Processes 500-word documents in ~3-5 seconds

## 🏃 Run Locally
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/textsum.git
cd textsum

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
