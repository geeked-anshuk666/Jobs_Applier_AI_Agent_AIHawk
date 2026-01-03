<div align="center">

# 🦅 AIHawk: The Ultimate AI Job Application Agent

**Land your dream job with AI-powered automation, tailored resumes, and professional 1-page layouts.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Optimized for OpenRouter](https://img.shields.io/badge/LLM-OpenRouter-orange.svg)](https://openrouter.ai/)

---

AIHawk's core architecture remains **open source**, allowing developers to inspect and extend the codebase. This version features heavy optimizations for **one-page resume layouts** and lightning-fast generation using **OpenRouter**.

</div>

## 🚀 Overview

AIHawk is an advanced AI-powered job application automation ecosystem. It doesn't just apply for you; it **re-engineers your professional presence**. By leveraging state-of-the-art LLMs, AIHawk parses job descriptions and dynamically reconstructs your resume and cover letter to ensure a perfect match for every application.

---

## ✨ Key Features & Recent Optimizations

*   **⚡ OpenRouter Integration**: Powered by `Gemini 2.0 Flash` for near-instant resume tailoring with zero latency.
*   **📏 Professional 1-Page Layouts**: 
    *   **Default Style**: Optimized for high-density information with a classic professional feel.
    *   **Clean Blue Style**: Modern, sleek layout with a compact header—guaranteed to fit on 1 page while maintaining readability.
*   **📊 Quantified Achievement Focus**: The AI is tuned to prioritize metric-driven accomplishments (e.g., "Increased efficiency by 40%").
*   **🔗 Smart Hyperlinking**: Automatically expands and hyperlinks LinkedIn, GitHub, and Portfolio URLs in the resume header.
*   **🛠️ Robust Output Sanitization**: Advanced logic to strip LLM-specific markdown artifacts, ensuring your PDF is clean and professional.
*   **🔍 FAISS-Powered Context**: Uses vector similarity search to find the most relevant parts of your experience for any job description.

---

## 🛠️ Architecture

The system is built with a modular, scalable architecture:

*   **`ResumeFacade`**: The orchestrator that manages the end-to-end generation flow.
*   **`LLMParser` (FAISS)**: Analyzes job descriptions using vector embeddings to extract key requirements.
*   **`StyleManager`**: Handles dynamic CSS loading and allows for easy style hot-swapping.
*   **`LoggerChatModel`**: Provides robust error handling, rate-limit retries, and detailed API logging.

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/geeked-anshuk666/Jobs_Applier_AI_Agent_AIHawk.git
cd Jobs_Applier_AI_Agent_AIHawk
```

### 2. Set Up Virtual Environment (Recommended)
**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```
**Unix/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### `data_folder/secrets.yaml`
Add your API key here. We recommend using **OpenRouter** for the best performance.
```yaml
llm_api_key: "your_openrouter_api_key_here"
```

### `config.py`
Configure your preferred model and API endpoint.
```python
LLM_MODEL_TYPE = 'openai' 
LLM_MODEL = 'google/gemini-2.0-flash-001' 
LLM_API_URL = 'https://openrouter.ai/api/v1'
```

### `data_folder/plain_text_resume.yaml`
Input your professional history. Use **quantifiable metrics** for the best AI-generated results!

---

## 🚀 Usage

1.  **Prepare your data**: Ensure `plain_text_resume.yaml` and `work_preferences.yaml` are filled out.
2.  **Launch the Agent**:
    ```bash
    python main.py
    ```
3.  **Choose your path**:
    *   `Generate Resume`: Creates a professional, cleaned-up base resume.
    *   `Generate Tailored Resume`: Scrapes a job URL and optimizes your resume specifically for that role.

---

## 🎨 Styles Showcase

| Style Name | Author | Features |
| :--- | :--- | :--- |
| **Clean Blue** | [samodum](https://github.com/samodum) | **Compact header**, row-based contact info, optimized for 1-page fit. |
| **Default** | [krishnavalliappan](https://github.com/krishnavalliappan) | Classic layout, bold headers, dark bullet points for better scannability. |
| **Modern Blue** | [josylad](https://github.com/josylad) | Sleek, modern design with subtle blue accents. |

---

## 📺 Media Coverage

AIHawk has been featured by major media outlets for revolutionizing the job hunt:

[**Business Insider**](https://www.businessinsider.com/aihawk-applies-jobs-for-you-linkedin-risks-inaccuracies-mistakes-2024-11) | [**TechCrunch**](https://techcrunch.com/2024/10/10/a-reporter-used-ai-to-apply-to-2843-jobs/) | [**Wired**](https://www.wired.it/article/aihawk-come-automatizzare-ricerca-lavoro/) | [**The Verge**](https://www.theverge.com/2024/10/10/24266898/ai-is-enabling-job-seekers-to-think-like-spammers)

---

## 🤝 Contributing & License

We welcome contributions! Fork the repo, create a branch, and submit a PR.
This project is licensed under the **MIT License**.

</div>