{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "eb46b04f-d2e5-4ef6-9d1f-78f43d3ecdd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "## Artificial Intelligence (AI) – A Quick Primer  \n",
      "\n",
      "| Term | Description |\n",
      "|------|-------------|\n",
      "| **Artificial** | Something made by humans, not occurring naturally. |\n",
      "| **Intelligence** | The ability to acquire knowledge, reason, solve problems, learn from experience, and adapt to new situations. |\n",
      "| **AI** | Machines or software that simulate, emulate, or replicate one or more aspects of human intelligence. |\n",
      "\n",
      "---\n",
      "\n",
      "### 1. Core Ideas Behind AI\n",
      "\n",
      "| Principle | What it means for a system |\n",
      "|-----------|----------------------------|\n",
      "| **Machine Learning (ML)** | Systems learn patterns from data instead of being explicitly programmed. |\n",
      "| **Deep Learning** | A subset of ML that uses neural networks with many “layers” to model complex relationships. |\n",
      "| **Unsupervised vs. Supervised** | *Supervised* learning uses labeled data (e.g., a photo labeled “cat”). *Unsupervised* learns structure from unlabeled data (e.g., clustering similar images). |\n",
      "| **Reinforcement Learning** | An agent learns by taking actions in an environment to maximize cumulative rewards (like a game‑playing AI). |\n",
      "\n",
      "---\n",
      "\n",
      "### 2. Main Categories of AI\n",
      "\n",
      "| Category | Typical Tasks |\n",
      "|----------|---------------|\n",
      "| **Narrow AI** | Designed for a specific task (e.g., facial recognition, spam filtering). |\n",
      "| **General AI** | (Hypothetical) would match human flexibility across all domains. |\n",
      "| **Superintelligence** | (Speculative) exceeds human cognitive capabilities. |\n",
      "\n",
      "---\n",
      "\n",
      "### 3. Common Applications\n",
      "\n",
      "| Domain | Example |\n",
      "|--------|---------|\n",
      "| **Natural Language Processing (NLP)** | Chatbots, language translation, sentiment analysis. |\n",
      "| **Computer Vision** | Image classification, object detection, autonomous driving perception. |\n",
      "| **Robotics** | Automated warehouses, surgical robots, drones. |\n",
      "| **Recommendation Systems** | Movie or product suggestions on streaming platforms or e‑commerce. |\n",
      "| **Finance** | Fraud detection, high‑frequency trading algorithms, credit scoring. |\n",
      "| **Healthcare** | Diagnostic imaging, personalized treatment recommendations, drug discovery. |\n",
      "\n",
      "---\n",
      "\n",
      "### 4. How Does an AI System Work in Practice?\n",
      "\n",
      "1. **Data Collection** – Gather relevant data (images, text, sensor readings).  \n",
      "2. **Pre‑processing** – Clean, normalise, and transform data.  \n",
      "3. **Model Design** – Choose architecture (e.g., convolutional neural network).  \n",
      "4. **Training** – Use computational resources to optimise model parameters.  \n",
      "5. **Evaluation** – Test on unseen data, compute metrics (accuracy, F1‑score).  \n",
      "6. **Deployment** – Integrate into an application or service.  \n",
      "7. **Monitoring & Update** – Continually track performance; retrain with new data as needed.\n",
      "\n",
      "---\n",
      "\n",
      "### 5. Ethical & Societal Considerations\n",
      "\n",
      "| Topic | Key Questions |\n",
      "|-------|---------------|\n",
      "| **Bias & Fairness** | Does the model treat all groups equally? |\n",
      "| **Transparency** | Can we understand why a model makes a specific decision? |\n",
      "| **Privacy** | How are personal data handled and protected? |\n",
      "| **Safety & Robustness** | How does the system behave in edge cases or against malicious inputs? |\n",
      "| **Accountability** | Who is responsible if an AI causes harm? |\n",
      "\n",
      "---\n",
      "\n",
      "### 6. AI Today vs. Tomorrow\n",
      "\n",
      "| 2024‑Style AI | Future Vision (next decade) |\n",
      "|---------------|---------------------------|\n",
      "| Predominantly statistical pattern‑recognition systems | Hybrid models combining symbolic reasoning, understanding, and creativity |\n",
      "| Limited reasoning outside trained domains | More general-purpose, versatile agents able to transfer learning across tasks |\n",
      "| Human‑in‑the‑loop oversight common | Potential for autonomous systems that still require careful supervision |\n",
      "\n",
      "---\n",
      "\n",
      "#### Bottom line\n",
      "Artificial Intelligence is the scientific and engineering effort to build machines that can *think*—or at least act—like humans under specified conditions. It relies heavily on data, learning algorithms, and mathematical models to transform raw inputs into useful outputs, while raising important questions of fairness, safety, and accountability.\n"
     ]
    }
   ],
   "source": [
    "from openai import OpenAI\n",
    "\n",
    "client = OpenAI(\n",
    "    base_url=\"https://openrouter.ai/api/v1\",\n",
    "    api_key=\"import os

api_key = os.getenv("OPENROUTER_API_KEY")"\n",
    ")\n",
    "\n",
    "response = client.chat.completions.create(\n",
    "    model=\"openai/gpt-oss-20b:free\",\n",
    "    messages=[\n",
    "        {\n",
    "            \"role\": \"user\",\n",
    "            \"content\": \"What is AI?\"\n",
    "        }\n",
    "    ]\n",
    ")\n",
    "\n",
    "print(response.choices[0].message.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "79d51037-d740-47f5-896d-30fccef8a43e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AI Chatbot Started\n",
      "Type 'exit' to stop\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  hello\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: Hello! How can I help you today?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  exit\n"
     ]
    }
   ],
   "source": [
    "from openai import OpenAI\n",
    "\n",
    "client = OpenAI(\n",
    "    base_url=\"https://openrouter.ai/api/v1\",\n",
    "    api_key=\"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\"\n",
    ")\n",
    "\n",
    "print(\"AI Chatbot Started\")\n",
    "print(\"Type 'exit' to stop\")\n",
    "\n",
    "while True:\n",
    "\n",
    "    question = input(\"You: \")\n",
    "\n",
    "    if question.lower() == \"exit\":\n",
    "        break\n",
    "\n",
    "    response = client.chat.completions.create(\n",
    "        model=\"openai/gpt-oss-20b:free\",\n",
    "        messages=[\n",
    "            {\n",
    "                \"role\": \"user\",\n",
    "                \"content\": question\n",
    "            }\n",
    "        ]\n",
    "    )\n",
    "\n",
    "    answer = response.choices[0].message.content\n",
    "\n",
    "    print(\"Bot:\", answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "35a705bb-3aca-4c4e-a13b-2c188d903416",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\admin\\anaconda3\\lib\\site-packages (1.51.0)\n",
      "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.5.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<7,>=4.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (5.5.1)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (8.2.1)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (2.3.5)\n",
      "Requirement already satisfied: packaging<26,>=20 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (25.0)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (2.3.3)\n",
      "Requirement already satisfied: pillow<13,>=7.1.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (12.0.0)\n",
      "Requirement already satisfied: protobuf<7,>=3.20 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (5.29.3)\n",
      "Requirement already satisfied: pyarrow<22,>=7.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (21.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (2.32.5)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (9.1.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (4.15.0)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (3.1.45)\n",
      "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from streamlit) (6.5.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.0)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.7.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\admin\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.11)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2025.11.12)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.37.0)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.28.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.2)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "!pip install streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b0bec25-b7f9-472c-a742-c62a0e369e7f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb2eb4a8-3d49-4e39-89c7-17e887b5a506",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
