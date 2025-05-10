from summarizer import split_text_into_chunks, summarize_chunk_for_slide
import os

# Load your file content (replace this with dynamic upload if needed)
with open("input.txt", "r", encoding="utf-8") as f:
    content = f.read()

chunks = split_text_into_chunks(content)

for i, chunk in enumerate(chunks):
    print(f"\n🧠 Slide {i+1}:")
    slide = summarize_chunk_for_slide(chunk)
    print(slide)
