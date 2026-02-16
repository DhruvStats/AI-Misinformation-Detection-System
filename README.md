# LLM-Based Misinformation Detection System

## Team Members
- Wagh Dhruv Arun

## Problem Statement
Detect fake news automatically using Large Language Models.

## System Architecture
User Input → Streamlit App → LLM Classifier → Prediction + Confidence → Logging → Evaluation

## Features
- Fake / Real classification
- Confidence score
- Explanation generation
- Evaluation metrics (Accuracy, Precision, Recall, F1)
- Misclassified sample logging
- Robustness testing

## Technologies Used
- Python
- HuggingFace Transformers
- Streamlit
- Pandas
- Scikit-learn

## Evaluation Results
- Accuracy: (Your value)
- Observed bias toward "Real News"
- Low recall for Fake News

## Limitations
- Small dataset
- Zero-shot model
- CPU-only inference
- Possible bias

## Future Work
- Fine-tuning on large dataset
- Fairness testing
- Adversarial robustness evaluation
- Cloud deployment
