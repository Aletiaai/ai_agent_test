import pandas as pd
import string
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variables not set")
genai.configure(api_key = GEMINI_API_KEY)

def load_data(file_path:str)->pd.DataFrame | None:
    #Loads data from a csv file into a pandas dataframe
    try:
        df = pd.read_csv(file_path)
        print(f"successfully loaded data from {file_path}")
        return df
    except FileNotFoundError:
        print(f"This file: '{file_path}' was not founod")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: file '{file_path}' is empty")
        return None
    except Exception as e:
        print(f"An unexpected error occured while loading {file_path}: {e}")
        return None

#Lowe case and remove punctuation
def retrieve_context_keyword(question: str, data: pd.DataFrame, content_column: str = 'text')-> str | None:
    #¡Retrieves the most relevant text fragment based on keywords
    if data is None or data.empty:
        print("Error: Data is not loaded or is empty")
        return None
    translator = str.maketrans('', '', string.punctuation)
    question_clean = question.lower().translate(translator)
    question_keywords = set(question_clean.split())

    if not question_keywords:
        print("Warming: Could not extract keywords from the question.")
        return None
    
    best_match_score = -1
    best_match_text = None

    #iterate through text fragments in the dataframe
    for index, row in data.iterrows():
        text_content =  row[content_column]
        if not isinstance(text_content, str):
            continue
        
        #lower case and remove punctuation from the text 
        text_clean = text_content.lower().translate(translator)
        text_words = set(text_clean.split())

        #count commond words between question and text
        common_keywords = question_keywords.intersection(text_words)
        score = len(common_keywords)

        #update best match
        if score > best_match_score:
            best_match_score = score
            best_match_text = text_content #return original uncleaned text

        if best_match_score > 0:
            print(f"Foound context with score: {best_match_score}")
            return best_match_text
        else:
            print("No relevant contect found based on keywors")
            return None
        
def generate_answer_with_llm(context: str, question: str)-> str | None:
    #Generates an answer using gemini-2.0-flach-lite
    if not context:
        return "I couldn't find relevant information to answer your question"
    #Select model
    model = genai.GenerativeModel('gemini-2.0-flash-lite')

    #Build the prompt
    prompt = f"Answer the question based on the the context:\n Question: '{question}' \n Context:\n'{context}:\nAnswer:"""

    try:
        response = model.generate_content(prompt)
        if response and response.text:
            return response.text.strip()
        else:
            return "Sorry, I couldn't generate an answer at this time"
    except Exception as e:
        print(f"An error ocurred while calling the Geminii API: {e}")
        return "An error occurred while trying to generate the answer."




