# Education Domain Chatbot: Grade School Math Q&A

## Overview
This project is an education-domain chatbot designed to answer grade school math questions using a fine-tuned DistilGPT-2 model. The chatbot is trained on the GSM8K dataset and deployed with a FastAPI backend and a Gradio web interface. The project includes both Jupyter Notebooks and Python scripts for data preprocessing, model training, evaluation, and deployment.

## Dataset
- **Source:** GSM8K - Grade School Math 8K Q&A (Kaggle)
- **Files:** `main_train.csv`, `main_test.csv`
- **Columns:**
  - `question`: Math word problem (string)
  - `answer`: Step-by-step solution (string)

## Project Structure
```
education-domain-chatbot/
│
├── data/                # main_train.csv, main_test.csv
├── model/               # Training scripts, model checkpoints
├── app/                 # FastAPI backend, Gradio UI
├── notebooks/           # Jupyter Notebooks for EDA, training, etc.
├── requirements.txt     # All dependencies
├── README.md            # Project documentation
└── main.py              # Entry point for training or running the chatbot
```

## Setup Instructions
1. Clone the repository and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place `main_train.csv` and `main_test.csv` in the `data/` folder.
4. Use the Jupyter Notebooks in `notebooks/` for data exploration, preprocessing, and model training.
5. Run the FastAPI backend and Gradio UI from the `app/` directory.

## Next Steps
- Data preprocessing and EDA in Jupyter Notebook
- Model fine-tuning and evaluation
- Backend and UI development
- Documentation and demo video