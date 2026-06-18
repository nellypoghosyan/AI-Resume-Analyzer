# AI Resume Analyzer

AI Resume Analyzer is a simple web application built with Python, Streamlit, and OpenAI API that analyzes resumes and provides personalized feedback. The application evaluates resumes by identifying strengths, weaknesses, missing skills, and suggestions for improvement.

## Features

* Resume analysis using AI
* Detects strengths and weaknesses
* Suggests missing skills and improvements
* Provides an overall resume evaluation score
* Interactive and user-friendly interface built with Streamlit

## Technologies Used

* Python
* Streamlit
* OpenAI API
* python-dotenv

## How It Works

Users can paste their resume into the application, and the AI generates feedback based on the resume content. The analysis includes:

* Strengths
* Weaknesses
* Missing skills
* Improvement suggestions
* Overall score

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
```

2. Navigate to the project folder

```bash
cd ai-resume-analyzer
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your OpenAI API key

```env
OPENAI_API_KEY=your_api_key_here
```

5. Run the application

```bash
streamlit run aii.py
```

## Note

This project requires an OpenAI API key to function properly.

## Future Improvements

* Upload resume as PDF
* Better resume scoring system
* Job-specific resume analysis
* Resume keyword optimization

## Author

Nelli Poghosyan
