# ✦ Imagine AI

An AI-powered image generation web application that converts text prompts into images using Generative AI.

Imagine AI provides a simple and interactive interface where users can describe an image, choose a visual style, and generate an AI-created image directly from the browser.

---

## 🚀 Features

- Generate images from natural language prompts
- Multiple visual styles
  - Realistic
  - Cinematic
  - Digital Art
  - Anime
  - Fantasy
  - 3D Render
- Simple and user-friendly Streamlit interface
- AI-powered image generation using Hugging Face
- Preview generated images directly in the application
- Download generated images as PNG files
- Secure API key management using `.env`
- Responsive dark-themed interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- FLUX.1-schnell
- Pillow
- python-dotenv

---

## 🧠 How It Works

The application follows a simple workflow:

```text
User enters a prompt
        ↓
Selects image style
        ↓
Streamlit processes the input
        ↓
Prompt is sent to Hugging Face
        ↓
FLUX.1-schnell generates the image
        ↓
Generated image is displayed
        ↓
User can download the image


## 📁 Project Structure

```text
image-generator/
│
├── app.py
├── .env
├── .gitignore
├── README.md
└── venv/
```

### File Description

| File         | Purpose                                                      |
| ------------ | ------------------------------------------------------------ |
| `app.py`     | Main Streamlit application                                   |
| `.env`       | Stores the Hugging Face API token                            |
| `.gitignore` | Prevents sensitive and unnecessary files from being uploaded |
| `README.md`  | Project documentation                                        |
| `venv/`      | Python virtual environment                                   |

---