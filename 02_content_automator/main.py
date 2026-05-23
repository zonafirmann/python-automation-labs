import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_automated_content():
    print("🤖 Initiating Content Automation Protocol...")
    
    api_key = os.getenv("SECRET_API_KEY")
    if not api_key:
        print("❌ CRITICAL: Missing Secret API Key in environment. (Have you created the .env file?)")
        return

    source_url = "https://dummyjson.com/quotes/random"
    
    try:
        response = requests.get(source_url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        quote = data.get("quote", "No quote found")
        author = data.get("author", "Unknown")
        
        structured_payload = {
            "workflow_id": "auto_gen_001",
            "content_type": "short_form_video",
            "raw_text": f"{quote} - {author}",
            "voice_settings": "dramatic_male",
            "status": "ready_for_processing"
        }
        
        print("\n✅ Data Successfully Processed & Structured!")
        print("-" * 40)
        for key, value in structured_payload.items():
            print(f"{key.upper():<15} : {value}")
        print("-" * 40)
        print("🚀 Ready to forward to the next API pipeline...\n")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network or API Error: {e}")

if __name__ == "__main__":
    generate_automated_content()