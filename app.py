import streamlit as st
from transformers import pipeline
import torch

st.set_page_config(page_title="AI Document Summarizer", page_icon="📄")

# Cache the model to avoid reloading
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_words=400):
    """Split text into chunks of max_words"""
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = ' '.join(words[i:i + max_words])
        chunks.append(chunk)
    return chunks

def summarize_long_text(text, summarizer):
    """Handle long texts by chunking"""
    word_count = len(text.split())
    
    # If text is short enough, summarize directly
    if word_count <= 400:
        result = summarizer(text, max_length=150, min_length=50, do_sample=False)
        return result[0]['summary_text']
    
    # For long text, chunk and summarize each chunk
    chunks = chunk_text(text, max_words=400)
    summaries = []
    
    progress_bar = st.progress(0)
    for i, chunk in enumerate(chunks):
        chunk_summary = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
        summaries.append(chunk_summary[0]['summary_text'])
        progress_bar.progress((i + 1) / len(chunks))
    
    # Combine chunk summaries
    combined = ' '.join(summaries)
    
    # If combined summary is still long, summarize it again
    if len(combined.split()) > 200:
        final_summary = summarizer(combined, max_length=150, min_length=50, do_sample=False)
        return final_summary[0]['summary_text']
    
    return combined

st.title("📄 AI Document Summarizer")
st.markdown("Paste your document below and get an intelligent summary")

summarizer = load_model()

# Text input
text = st.text_area("Enter your document here:", height=300, 
                    placeholder="Paste your text here...")

col1, col2 = st.columns([1, 5])
with col1:
    summarize_btn = st.button("Summarize", type="primary")

if summarize_btn and text:
    with st.spinner("Generating summary..."):
        try:
            word_count = len(text.split())
            
            if word_count > 400:
                st.info(f"📝 Long document detected ({word_count} words). Processing in chunks...")
            
            summary = summarize_long_text(text, summarizer)
            
            st.success("✅ Summary generated!")
            st.markdown("### Summary:")
            st.info(summary)
            
            # Show stats
            col1, col2, col3 = st.columns(3)
            col1.metric("Original Words", word_count)
            col2.metric("Summary Words", len(summary.split()))
            col3.metric("Compression", f"{round((1 - len(summary.split())/word_count)*100)}%")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Try with a shorter text or check your internet connection.")
            
elif summarize_btn:
    st.warning("⚠️ Please enter some text to summarize!")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit & Transformers | [GitHub](your-github-link)")