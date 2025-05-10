import openai
import os
import time

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your env

def split_text_into_chunks(text, max_tokens=1000):
    words = text.split()
    chunks = []
    chunk = []
    tokens = 0

    for word in words:
        chunk.append(word)
        tokens += 1
        if tokens >= max_tokens:
            chunks.append(" ".join(chunk))
            chunk = []
            tokens = 0

    if chunk:
        chunks.append(" ".join(chunk))

    return chunks

def safe_chat_completion(prompt):
    for attempt in range(3):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response['choices'][0]['message']['content']
        except openai.error.RateLimitError:
            print(f"⚠️ Rate limit hit, retrying in {5 * (attempt + 1)}s...")
            time.sleep(5 * (attempt + 1))
    raise Exception("❌ Failed after 3 retries due to rate limits.")

def summarize_chunk_for_slide(chunk):
    prompt = f"Summarize this text as a bullet-point slide:\n\n{chunk}"
    return safe_chat_completion(prompt)
