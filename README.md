# 🛠️ SkillCraft – AI-Powered Career Roadmap Generator

> *Craft your career like a skilled artisan.*

**SkillCraft** is an intelligent, AI-driven platform that generates personalized career roadmaps based on your current skills and target job role. Unlike static course lists or generic roadmaps, SkillCraft uses a reasoning-based AI agent to analyze skill gaps, infer learning dependencies, and guide you through a structured, role-specific path with curated courses and projects.

---

## 🌟 Motivation

As a second-year student, I spent nearly six months watching generic AI and tech career roadmap videos — most of which were broad and not tailored to my background. I realized there was no system that could take into account *where I am* and show *where I need to go*.  
**SkillCraft** was born to solve this — a system that thinks before it recommends, just like a career mentor would.

---

## 🧠 How the AI Agent Works

SkillCraft is powered by a **custom AI agent** built using **LLaMA 3**, following a **Think → Observe → Respond** loop:

- **Observe:** Takes user’s current skills and desired job role.
- **Think:** Performs structured reasoning to break down the role into logical skill clusters (e.g., Deep Learning, System Design), and determines dependencies between them.
- **Respond:** Recommends a personalized learning path with:
  - Ordered list of missing skills  
  - Curated courses (e.g., Coursera, edX)  
  - Suggested hands-on projects  

The agent ensures intelligent sequencing:
> “Master Transformer architecture before fine-tuning GPT.”  
> “Learn parallel computation before tackling distributed systems.”

---

## ✨ Key Features

- 🎯 Role-specific skill breakdowns (e.g., ML Engineer, Data Analyst)
- 📚 Curated learning paths with real course links
- 🧱 Project recommendations to apply each skill
- 🔁 Adaptive, never static — every roadmap is unique
- 🌍 Planned: Progress tracking & feedback-based refinement

---

## 🔧 Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| AI Agent     | LLaMA 3, LangChain                |
| Backend      | FastAPI, Python                   |
| Frontend     | React, Pure CSS                   |
| Retrieval    | Custom rule-based + semantic search |
| Optional     | Firebase (planned for user progress) |

---

## 🧪 Run Locally

```bash
# Clone the frontend
git clone https://github.com/your-username/skillcraft-frontend
cd skillcraft-frontend
npm install
npm start
