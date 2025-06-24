from fastapi import FastAPI
from pydantic import BaseModel
from transformers import TFAutoModelForCausalLM, AutoTokenizer
import tensorflow as tf
import os

# Get absolute path to the model directory
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../model/distilgpt2-finetuned"))

# Load tokenizer and model from local files only
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
model = TFAutoModelForCausalLM.from_pretrained(MODEL_PATH, local_files_only=True)

SEP_TOKEN = "<|sep|>"

# Set pad token and pad_token_id
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id

app = FastAPI()

class Query(BaseModel):
    question: str

def generate_answer(question, max_new_tokens=50):
    input_ids = tokenizer.encode(question + f" {SEP_TOKEN}", return_tensors='tf')
    output = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    if SEP_TOKEN in answer:
        answer = answer.split(SEP_TOKEN)[-1].strip()
    return answer

@app.post("/chat")
async def chat(query: Query):
    answer = generate_answer(query.question)
    return {"answer": answer}