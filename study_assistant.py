def get_topic():
    while True:
        topic = input("Enter a study topic (or 'exit/quit' to quit): ").strip()
        if topic.lower() == "exit" or topic.lower() == "quit":
            print("Program ending...")
            return None
        elif topic:
            return topic
        else:
            print("Please enter a valid topic.")

def prompt():
    Prompt= '''
    you are an experienced tutor.
    write the topics(each one followed by its subtopics) regarding the topic.
    Format (for study plan):
        1. Topic 1: Description of topic 1
            a. Subtopic 1.1: Description of subtopic 1.1
            b. Subtopic 1.2: Description of subtopic 1.2        
    keep the descriptions in study plan under 25 words.
    keep the topics and subtopics from basics to deeper concepts.
    For follow-up questions, adapt explanations to the apparent knowledge level of the user.
    Format (for follow-up questions):
        small paragraphs with clear explanations and examples.
    keep the length of explanations for follow-up questions under 100 words.
    do not ask questions, just provide the topics and subtopics with their descriptions.
    do not go off-topic unless specified by the user. '''
    return Prompt

def create_chat():
    pass

def study_plan(chat, topic):
    pass

def chat_loop(chat):
    pass

def session_summary(topic, question_count):
    pass


get_topic()