<div align="center">

# AIHawk: The first Jobs Applier AI Web Agent

AIHawk's core architecture remains **open source**, allowing developers to inspect and extend the codebase. However, due to copyright considerations, we have removed all third‑party provider plugins from this repository.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Media Coverage](#media-coverage)
- [Contributing](#contributing)
- [License](#license)

## Overview

AIHawk is an AI-powered job application automation tool that helps job seekers apply to positions automatically. It leverages large language models (LLMs) to generate personalized cover letters and resumes tailored to specific job descriptions, then automates the application process on various job platforms.

The system is designed to be flexible and configurable, allowing users to customize the AI models, job preferences, and application behavior according to their needs.

## Features

- **AI-Powered Resume Generation**: Automatically creates tailored resumes based on job descriptions
- **Intelligent Cover Letter Creation**: Generates personalized cover letters matching job requirements
- **Automated Application Submission**: Streamlines the application process across multiple platforms
- **Configurable LLM Support**: Works with various language models (OpenAI, Claude, Ollama, Perplexity, Gemini, HuggingFace)
- **Job Matching Algorithm**: Determines job suitability based on resume and job description alignment
- **Application Tracking**: Logs and tracks all applications submitted
- **Resume Parsing**: Extracts relevant information from existing resumes
- **Cost Tracking**: Monitors API usage costs for budget management

## Architecture

The system is built with a modular architecture consisting of:

- **LLM Manager**: Handles communication with various language model providers
- **Resume Builder**: Creates and formats resumes based on templates
- **Cover Letter Generator**: Creates job-specific cover letters
- **Job Parser**: Extracts relevant information from job postings
- **Application Engine**: Manages the application submission process
- **Configuration System**: Allows flexible configuration of AI models and behavior

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/geeked-anshuk666/Jobs_Applier_AI_Agent_AIHawk.git
   cd Jobs_Applier_AI_Agent_AIHawk
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Configure your job preferences and resume in the `data_folder` directory.

## Configuration

The system uses a configuration file (`config.py`) to manage various settings:

- `LLM_MODEL_TYPE`: The type of LLM to use (OpenAI, Claude, Ollama, etc.)
- `LLM_MODEL`: The specific model name
- `LLM_API_URL`: Custom API URL for self-hosted models
- `JOB_SUITABILITY_SCORE`: Minimum score for job applications
- Other settings for application behavior

## Usage

1. Prepare your resume data in the `data_folder/plain_text_resume.yaml` file
2. Set your job preferences in `data_folder/work_preferences.yaml`
3. Configure your secrets in `data_folder/secrets.yaml`
4. Run the main application:
   ```bash
   python main.py
   ```

## Media Coverage

AIHawk has been featured by major media outlets for revolutionizing how job seekers interact with the job market:

[**Business Insider**](https://www.businessinsider.com/aihawk-applies-jobs-for-you-linkedin-risks-inaccuracies-mistakes-2024-11)
[**TechCrunch**](https://techcrunch.com/2024/10/10/a-reporter-used-ai-to-apply-to-2843-jobs/)
[**Semafor**](https://www.semafor.com/article/09/12/2024/linkedins-have-nots-and-have-bots)
[**Dev.by**](https://devby.io/news/ya-razoslal-rezume-na-2843-vakansii-po-17-v-chas-kak-ii-boty-vytesnyaut-ludei-iz-protsessa-naima.amp)
[**Wired**](https://www.wired.it/article/aihawk-come-automatizzare-ricerca-lavoro/)
[**The Verge**](https://www.theverge.com/2024/10/10/24266898/ai-is-enabling-job-seekers-to-think-like-spammers)
[**Vanity Fair**](https://www.vanityfair.it/article/intelligenza-artificiale-candidature-di-lavoro)
[**404 Media**](https://www.404media.co/i-applied-to-2-843-roles-the-rise-of-ai-powered-job-application-bots/)

## Contributing

We welcome contributions to the AIHawk project! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

</div>