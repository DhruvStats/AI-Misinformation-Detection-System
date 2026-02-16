# 📰 LLM-Based Misinformation Detection System

## 👥 Team Members
- **Wagh Dhruv Arun**
- **Tooba Naeem**

---

## 🚀 Project Overview

This project presents a **Full-Stack AI-powered Misinformation Detection System** that leverages a **Large Language Model (LLM)** to classify news articles as *Real* or *Fake*.

The system integrates:

- A frontend interface for user interaction  
- A backend API for inference  
- A local LLM for classification  
- Logging, evaluation, and robustness analysis  

The objective is to demonstrate practical deployment of modern NLP systems in a real-world misinformation detection pipeline.

---

## 🧠 Why This Project Matters

Misinformation spreads rapidly across digital platforms, influencing public opinion, elections, and public safety.

Traditional machine learning models struggle with:
- Context understanding
- Sarcasm detection
- Long-form reasoning

Large Language Models (LLMs) provide:
- Deep contextual understanding
- Zero-shot reasoning capability
- Better semantic comprehension

This project demonstrates how LLMs can be integrated into a production-style system for automated misinformation detection.

---

## 🏗️ System Architecture

User Input (Streamlit UI)  
        ↓  
Backend API (FastAPI / Uvicorn)  
        ↓  
LLM Classifier (Local Inference)  
        ↓  
Prediction + Confidence Score  
        ↓  
Logging + Evaluation + Robustness Testing  

The architecture follows a **Client–Server Model**, ensuring modularity and scalability.

---

## 🔥 Key Features

- ✅ Real/Fake news classification  
- ✅ Confidence score estimation  
- ✅ Explanation generation (LLM reasoning)  
- ✅ Evaluation metrics:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  
- ✅ Misclassified sample tracking  
- ✅ Robustness testing framework  
- ✅ Clean modular backend architecture  

---

## 🛠️ Technologies Used

- **Python**
- **HuggingFace Transformers**
- **Streamlit (Frontend)**
- **FastAPI + Uvicorn (Backend API)**
- **Pandas**
- **Scikit-learn**
- **Docker (Containerization)**
- **SQLite (Lightweight Database)**

---

## 📊 Evaluation Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | (Insert Your Value) |
| Precision | (Insert Your Value) |
| Recall    | (Insert Your Value) |
| F1 Score  | (Insert Your Value) |

### Observations:
- Slight bias toward predicting "Real News"
- Lower recall for Fake News due to dataset imbalance
- Zero-shot inference limits domain-specific adaptation

---

## ⚠️ Limitations

- Small dataset size  
- Zero-shot LLM usage (no fine-tuning)  
- CPU-only inference (slower response time)  
- Possible dataset bias  
- No adversarial training  

---

## 🔮 Future Improvements

- Fine-tuning on larger misinformation datasets  
- Bias and fairness evaluation  
- Adversarial robustness testing  
- Deployment on cloud infrastructure  
- Vector database integration for RAG-based verification  
- Multi-modal misinformation detection (text + image)  

---

## 🧪 How to Run the Project

### 1️ Run Backend

```bash
uvicorn backend.main:app --reload

**### 2 Run Frontend**

```bash
streamlit run app.py

**### 3 Docker**

```bash
docker build -t misinformation-app .
docker run -p 8000:8000 misinformation-app


## 📌 Learning Outcomes

Through this project, we gained hands-on experience in:

- **LLM inference pipelines** – Understanding how input text flows through tokenization, transformer layers, and prediction generation during real-time inference.

- **Prompt engineering** – Designing structured prompts to guide the Large Language Model toward accurate and consistent classification results.

- **Client–server architecture** – Building a modular system where the frontend (Streamlit) communicates with the backend (FastAPI) through REST APIs.

- **Evaluation of NLP systems** – Applying metrics such as Accuracy, Precision, Recall, and F1-score to measure model performance and identify weaknesses.

- **Model robustness testing** – Testing system behavior under varied and edge-case inputs to evaluate stability and reliability.

- **Deployment using Docker** – Containerizing the application to ensure portability, reproducibility, and consistent execution across environments.

- **Full-stack AI system design** – Integrating frontend UI, backend APIs, machine learning models, logging, and evaluation into a complete production-style AI application.
