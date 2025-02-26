import os
import openai

# Set your OpenAI API key here or rely on the environment variable.
openai.api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

def evaluate_text_quality(text):
    """
    Evaluates the quality of the given text by scoring clarity, grammar, coherence, and creativity.
    
    Parameters:
      - text (str): The text to evaluate.
      
    Returns:
      - str: The evaluation result with scores and explanations.
    """
    prompt = f"""
You are an expert writing evaluator. Evaluate the quality of the following text by providing scores (from 1 to 10) and a brief explanation for each of the following categories:
- Clarity
- Grammar
- Coherence
- Creativity

Also provide an overall quality score (from 1 to 10) with a summary explanation.

Text:
{text}

Please format your answer as follows:

Clarity: <score> - <brief explanation>
Grammar: <score> - <brief explanation>
Coherence: <score> - <brief explanation>
Creativity: <score> - <brief explanation>
Overall: <score> - <brief summary explanation>
"""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        evaluation = response.choices[0].text.strip()
    except Exception as e:
        evaluation = f"An error occurred: {e}"
    
    return evaluation

def main():
    # Example text to evaluate
    sample_text = (
        "Artificial intelligence is the simulation of human intelligence processes by machines, "
        "especially computer systems. These processes include learning (the acquisition of information and rules for using the information), "
        "reasoning (using rules to reach approximate or definite conclusions), and self-correction."
    )
    
    result = evaluate_text_quality(sample_text)
    
    print("Text Quality Evaluation:")
    print(result)

if __name__ == "__main__":
    main()
