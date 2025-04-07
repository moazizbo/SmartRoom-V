import os
from dotenv import load_dotenv

# load_dotenv()
# from openai import OpenAI
# api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=api_key)

def interpret_command(command: str):
    print("⚠️ MOCKED AI — OpenAI API disabled (no billing)")

    if "sleep" in command.lower():
        return '''
        {
            "lights": "off",
            "fan": "on",
            "music": "none",
            "brightness": 10
        }
        '''
    elif "study" in command.lower():
        return '''
        {
            "lights": "dimmed",
            "fan": "on",
            "music": "lofi",
            "brightness": 60
        }
        '''
    else:
        return '''
        {
            "lights": "on",
            "fan": "off",
            "music": "none",
            "brightness": 80
        }
        '''

# Test it
if __name__ == "__main__":
    cmd = input("Type your room command: ")
    result = interpret_command(cmd)
    print("\nAI Agent Response:\n", result)
