import openai
import streamlit as st

api_key = st.secrets["OPENAI_KEY"]
openai.api_key = api_key



system_prompt = """
You are an expert assistant in MBTI typology. Here are the meanings of the letters:

- **E** for Extraversion: energy directed outward, social interactions, action.
- **I** for Introversion: energy directed inward, reflection, solitude.
- **S** for Sensing: focus on concrete facts, details, present.
- **N** for Intuition: focus on ideas, concepts, future possibilities.
- **T** for Thinking: decisions based on logic and objectivity.
- **F** for Feeling: decisions based on personal values and harmony.
- **J** for Judging: preference for organization, planning, firm decisions.
- **P** for Perceiving: preference for flexibility, adaptability, openness to options.

Given a provided text, your task is to determine for each pair of letters (E/I, S/N, T/F, J/P):
1. The most representative letter.
2. The confidence percentage in this choice.
3. A very short explanation (max 20 words) of the choice.

Respond by correctly calling the `classify_mbti` function.
"""


functions = [
    {
        "name": "classify_mbti",
        "description": "Classify MBTI letters based on user text and return confidences and brief explanations",
        "parameters": {
            "type": "object",
            "properties": {
                "EI": {
                    "type": "object",
                    "properties": {
                        "letter": {"type": "string", "enum": ["E", "I"]},
                        "confidence": {"type": "integer", "minimum": 0, "maximum": 100},
                        "explanation": {
                            "type": "string",
                            "description": "A very short explanation (max 20 words) for why this letter was chosen"
                        }
                    },
                    "required": ["letter", "confidence", "explanation"]
                },
                "SN": {
                    "type": "object",
                    "properties": {
                        "letter": {"type": "string", "enum": ["S", "N"]},
                        "confidence": {"type": "integer", "minimum": 0, "maximum": 100},
                        "explanation": {
                            "type": "string",
                            "description": "A very short explanation (max 20 words) for why this letter was chosen"
                        }
                    },
                    "required": ["letter", "confidence", "explanation"]
                },
                "TF": {
                    "type": "object",
                    "properties": {
                        "letter": {"type": "string", "enum": ["T", "F"]},
                        "confidence": {"type": "integer", "minimum": 0, "maximum": 100},
                        "explanation": {
                            "type": "string",
                            "description": "A very short explanation (max 20 words) for why this letter was chosen"
                        }
                    },
                    "required": ["letter", "confidence", "explanation"]
                },
                "JP": {
                    "type": "object",
                    "properties": {
                        "letter": {"type": "string", "enum": ["J", "P"]},
                        "confidence": {"type": "integer", "minimum": 0, "maximum": 100},
                        "explanation": {
                            "type": "string",
                            "description": "A very short explanation (max 20 words) for why this letter was chosen"
                        }
                    },
                    "required": ["letter", "confidence", "explanation"]
                },
            },
            "required": ["EI", "SN", "TF", "JP"],
        }
    }
]



def classify_personality(text):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            functions=functions,
            function_call={"name": "classify_mbti"}
        )

        # Parse function response
        function_response = response.choices[0].message.function_call.arguments
        result = json.loads(function_response)

        return result

    except Exception as e:
        print(f"Error: {e}")
        return None
