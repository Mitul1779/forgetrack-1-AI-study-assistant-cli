# Overview

CLI Study Assistant

A command-line study assistant built with the Gemini API. The application generates a structured study plan for any topic and allows users to ask follow-up questions in an interactive chat session.

The session ends when the user enters `exit` or `quit`, after which a summary of the study session is displayed.


# Features


- Generate a structured study plan for any topic
- Interactive question-answer session
- Topic-focused tutoring using a system prompt
- Session summary with question count
- Input validation and basic error handling


# Setup Instructions

### 1. Clone the repository

git clone <repository-url>
cd <repository-folder>

2. Install dependencies
pip install -r requirements.txt

3. Create a .env file
Copy the example file:
cp .env.example .env

Or create .env manually:
GEMINI_API_KEY=your_api_key_here

4. Run the application
python study_assistant.py

1. Enter a study topic.
2. Review the generated study plan.
3. Ask follow-up questions about the topic.
4. Enter `exit` or `quit` to end the session.
5. View the session summary.



# A couple of FAQs
1.  What role did you assign in your system prompt, and why did you choose that framing?

I assigned the role of an experienced tutor to the AI agent. This framing helps the model to actually teach the user instead of just giving short answers and helps in maintaining a consistent style of answers.

3. What format did you specify for the study plan output, and how did you enforce it in the prompt?

I instructed the model to generate numbered topics followed by lettered subtopics. I also specified that each topic and subtopic should include a short description which should remain under 25 words. These formatting requirements were explicitly written in the system prompt along with an example structure to enforce them.

3. What happens if you remove the system prompt entirely — how does the output change?

The output, after removing the system prompt, became much broader and inconsistent than what we need. There was still useful information but scattered. For example, i searched for meditaion basics with and without the instructions both; with instructions it gave me a structered plan to study; while without the instructions it gave me a 5 week course on meditation instead and when i asked the model to give a study plan on it instead, it focused on 'it' and gave me a 6 week course on IT.

