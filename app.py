import streamlit as st
from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def main():
    st.title("Document Summarizer AI")
    st.write("Upload a text document to get a summary")

    uploaded_file = st.file_uploader("Choose a text file", type="txt")

    if uploaded_file is not None:
        # Read file
        text = uploaded_file.read().decode("utf-8")
        
        # Show original text
        with st.expander("View Original Text"):
            st.write(text)
        
        # Summarize
        if st.button("Summarize"):
            with st.spinner("Generating summary..."):
                try:
                    # Split text into chunks (model has 1024 max length)
                    max_chunk = 500
                    text_chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
                    
                    # Summarize each chunk
                    summaries = []
                    for chunk in text_chunks:
                        summary = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
                        summaries.append(summary[0]['summary_text'])
                    
                    full_summary = " ".join(summaries)
                    
                    # Show summary
                    st.subheader("Summary")
                    st.write(full_summary)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
