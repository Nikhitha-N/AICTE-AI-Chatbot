# AI-Based Chatbot for AICTE FAQs - Smart India Hackathon 2022

## 🚀 Project Overview

This project was developed for the **Smart India Hackathon 2022** under the problem statement **DR702** by the **All India Council for Technical Education (AICTE)**. The goal was to create an **AI-powered chatbot** to respond to frequently asked questions on AICTE's website, improving accessibility and user experience.

---
## 💡 Problem Statement

AICTE receives a high volume of queries from various stakeholders such as students, teachers, organizations, and administrators. Many users face difficulties due to lack of information, critical data blocks, or accessibility challenges (visual, auditory, or speech impairments). This project aims to streamline the query process using an intelligent chatbot.
--
## 🧠 Proposed Solution

We built an AI-based chatbot using the **Rasa Framework**. The bot supports both **voice** and **text** input (in English) and responds with interactive elements like:

- Text replies
- Hyperlinks
- Voice messages
- Images
- Videos
- Clickable buttons

The chatbot features include:

- **Accessibility support**: Designed for users with visual, speech, or hearing impairments
- **Interactive UI**: Rich user interface with multimedia content
- **Audio toggle**: Users can switch between voice on/off modes
- **Chat transcripts**: All conversations are stored in a simple Excel database for future reference
---
## 🧰 Tech Stack

### Backend:
- **Language**: Python 3
- **Framework**: Rasa NLU & Rasa Core
- **Server**: Sanic
- **Database**: Excel (for chat logs)
- **Connection Protocols**: REST API, Socket.IO, Engine.IO

### Frontend:
- **Languages**: HTML, CSS, JavaScript, Python
- **Interface**: Web-based, integrated with speech API
---
## 📦 Dependencies & Tools

- Rasa framework
- Web Speech API
- Excel for data storage
- REST & Socket-based communication
---
## 🔍 Use Cases

- Answering general queries on AICTE website
- Supporting differently-abled users
- Assisting students, faculty, and organizations in navigating AICTE services
---
## ⚠️ Known Issues / Show Stoppers

- Potential failure in voice recognition or speech API
- UI compatibility issues on low-end devices
- Blocking due to incomplete/critical data
- Need for a scalable database in production environments
---
## 📝 Future Scope

- Expand support for regional languages
- Enhance AI/ML model for better NLP accuracy
- Transition to a more robust DBMS
- Deploy to production-ready cloud infrastructure
---
## 👥 Team Information

- Niveditha DP
- Madhumita G
- Jayashree
- Janani Sri
- Varshitha Reddy M
- Nikhitha N
