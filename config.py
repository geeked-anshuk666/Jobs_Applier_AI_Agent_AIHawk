# In this file, you can set the configurations of the app.

from src.utils.constants import DEBUG, ERROR, LLM_MODEL, OPENAI

#config related to logging must have prefix LOG_
LOG_LEVEL = 'ERROR'
LOG_SELENIUM_LEVEL = ERROR
LOG_TO_FILE = False
LOG_TO_CONSOLE = False

MINIMUM_WAIT_TIME_IN_SECONDS = 60

JOB_APPLICATIONS_DIR = "job_applications"
JOB_SUITABILITY_SCORE = 7

JOB_MAX_APPLICATIONS = 5
JOB_MIN_APPLICATIONS = 1

# --- LLM CONFIGURATION ---
# Keep 'openai' as type for any compatible API (DeepSeek, OpenRouter, etc.)
LLM_MODEL_TYPE = 'openai' 

# Examples:
# OpenAI: 'gpt-4o-mini' | URL: 'https://api.openai.com/v1'
# DeepSeek: 'deepseek-chat' | URL: 'https://api.deepseek.com'
# OpenRouter: 'google/gemini-2.0-flash-001' | URL: 'https://openrouter.ai/api/v1'
# Local (LM Studio): 'llama-3.2' | URL: 'http://localhost:1234/v1'

LLM_MODEL = 'gpt-oss-120b' 
LLM_API_URL = 'https://api.openai.com/v1' # Set this to your provider's base URL