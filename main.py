import os
from agent import load_data, retrieve_context_keyword, generate_answer_with_llm


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, 'data')
    csv_file_path = os.path.join(data_dir, 'tax_policies.csv')
    print(f"Attempting to load file from: {csv_file_path}")  # Debug print


    #Load data

    tax_data = load_data(csv_file_path)

    #chack of data was loaded
    if tax_data is not None:
        print("Enter a question (or 'quit' to exit):")
        while True:
            question = input("> ").strip()
            if question.lower() == 'quit':
                break
            if not question:
                print("Please enter a valid question.")
                continue

            print(f"\nQuestion: {question}")
            retrieved_context = retrieve_context_keyword(question, tax_data, content_column='text')
            if retrieved_context:
                print(f"Retrieved context:\n{retrieved_context}")
                answer = generate_answer_with_llm(retrieved_context, question)
                print(f"Answer:\n{answer}")
            else:
                print("The context couldn't be retrieved for the question")
    else:
        print("Failed to load data")
