import os
import openai
from tkinter import *
from tkinter import scrolledtext, messagebox
from dotenv import load_dotenv

# Load API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text():
    input_text = input_box.get("1.0", END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter some text to summarize.")
        return

    try:
        output_box.delete("1.0", END)
        output_box.insert(END, "⏳ Summarizing...")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Summarize this:\n{input_text}"}
            ],
            max_tokens=150,
            temperature=0.5
        )

        summary = response["choices"][0]["message"]["content"].strip()
        output_box.delete("1.0", END)
        output_box.insert(END, summary)
    except Exception as e:
        output_box.delete("1.0", END)
        output_box.insert(END, f"❌ Error: {e}")

# GUI Setup
root = Tk()
root.title("🧠 AI Text Summarizer")
root.geometry("700x600")

Label(root, text="Enter Text:", font=("Arial", 14)).pack(pady=5)
input_box = scrolledtext.ScrolledText(root, wrap=WORD, width=80, height=15, font=("Arial", 11))
input_box.pack(pady=10)

Button(root, text="Summarize", font=("Arial", 12), command=summarize_text).pack(pady=10)

Label(root, text="Summary:", font=("Arial", 14)).pack(pady=5)
output_box = scrolled_
