import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/chat"

def ask_bot(question):
    response = requests.post(API_URL, json={"question": question})
    if response.status_code == 200:
        return response.json()["answer"]
    else:
        return "Error: Could not get response from backend."

iface = gr.Interface(
    fn=ask_bot,
    inputs=gr.Textbox(lines=2, placeholder="Ask a grade school math question..."),
    outputs="text",
    title="Education Domain Chatbot (GSM8K + DistilGPT-2)",
    description="Ask a grade school math question and get a step-by-step answer!"
)

if __name__ == "__main__":
    iface.launch()