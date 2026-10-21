import getpass
import os
from google import genai
from google.genai import types

def initialize_client() -> genai.Client:
    """
    Safely retrieves the Gemini API key without hardcoding.
    Checks environment variables first, then securely asks the user.
    """
    # 1. First, check if it's already in the system environment
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # 2. If not found, ask the user to input it securely
    if not api_key:
        print("🔑 Gemini API Key not found in environment variables.")
        # getpass hides the input text while typing so no one peeks over your shoulder
        api_key = getpass.getpass("Please paste your Gemini API Key: ").strip()
        
        if not api_key:
            raise ValueError("API Key cannot be empty. Execution stopped.")
            
    # 3. Return the authenticated client
    return genai.Client(api_key=api_key)

def enhance_user_message(client: genai.Client, raw_message: str) -> str:
    """
    Pass 1: Analyzes the raw message and outputs an enhanced version.
    """
    enhancer_prompt = f"""
    Analyze the following user input for a chatbot. 
    Rewrite it into an optimized, highly descriptive prompt for an advanced AI.
    
    Extract and add:
    1. The primary implicit goal of the user.
    2. The ideal tone/persona for the response.
    3. Any structural constraints (e.g., should use bullet points, code blocks).
    
    Raw User Input: "{raw_message}"
    
    Output ONLY the final, enhanced prompt wrapped in comprehensive instructions.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=enhancer_prompt
    )
    return response.text

def generate_final_response(client: genai.Client, raw_message: str) -> str:
    """
    Pass 2: Takes the enhanced message payload and sends it to the 
    core intelligence model for the user to see.
    """
    # 1. Enhance the input dynamically
    enhanced_payload = enhance_user_message(client, raw_message)
    
    print(f"\n--- [Internal Enhancement Log] ---\n{enhanced_payload}\n----------------------------------\n")
    
    # 2. Get the final output using the high-reasoning model
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=enhanced_payload,
        config=types.GenerateContentConfig(
            system_instruction="You are a brilliant, elite assistant executing highly structured instructions.",
            temperature=0.7,
        )
    )
    return response.text

# --- Interactive Loop ---
if __name__ == "__main__":
    print("🤖 Welcome to the Gemini Dual-Pass Chatbot!")
    
    # Securely initialize the client once at startup
    try:
        client = initialize_client()
    except Exception as e:
        print(f"Initialization Error: {e}")
        exit(1)
        
    print("\nInitialization successful! Type your message below (or type 'quit' to exit).")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
                
            if not user_input:
                continue
                
            print("Enhancing and generating response...")
            final_output = generate_final_response(client, user_input)
            print(f"\nBot:\n{final_output}")
            
        except Exception as e:
            print(f"\nAn error occurred: {e}")
