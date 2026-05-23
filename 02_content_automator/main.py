import os
import requests
from dotenv import load_dotenv

# Muat kunci rahasia dari .env
load_dotenv()

def generate_ai_video_script():
    print("🧠 Memulai Sistem AI Content Generator (Open-Source Edition)...")
    
    # 1. Verifikasi Kunci Hugging Face
    hf_api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not hf_api_key:
        print("❌ KRITIS: HUGGINGFACE_API_KEY tidak ditemukan di file .env!")
        return

    # 2. Ambil data mentah (Kutipan)
    print("📡 Mengambil bahan baku dari internet...")
    source_url = "https://dummyjson.com/quotes/random"
    try:
        response = requests.get(source_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        raw_quote = f"{data.get('quote')} - {data.get('author')}"
        print(f"✅ Bahan didapat: '{raw_quote}'")
    except Exception as e:
        print(f"❌ Gagal mengambil bahan baku: {e}")
        return

    # 3. Merakit Prompt untuk AI
    print("\n✨ Mengirim instruksi ke otak AI (Hugging Face) untuk merakit naskah...")
    prompt = f"""
    You are an expert short-form video scriptwriter. Create a 60-second dramatic and motivational video script based on this quote: "{raw_quote}".
    
    Format the output strictly like this:
    [VISUAL]: (scene description)
    [VOICEOVER]: (words to be spoken)
    """

    # 4. Menembak API Hugging Face (Kita gunakan model Mistral yang sangat pintar & cepat)
    # Model ini gratis dan siap pakai.
    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    headers = {"Authorization": f"Bearer {hf_api_key}"}
    
    # Konfigurasi agar AI menjawab dengan panjang yang pas
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250, # Batas panjang kata balasan AI
            "return_full_text": False # Agar AI tidak mengulang prompt awal kita
        }
    }

    try:
        # Kirim permintaan ke server AI
        ai_response = requests.post(api_url, headers=headers, json=payload)
        ai_response.raise_for_status()
        
        # Ekstrak teks balasan dari AI
        result_data = ai_response.json()
        ai_script = result_data[0]['generated_text']
        
        print("\n" + "="*60)
        print("🎬 NASKAH VIDEO HASIL GENERASI AI:")
        print("="*60)
        print(ai_script.strip())
        print("="*60)
        print("🚀 Payload Naskah SIAP dikirim ke API Video Generator otomatis!")
        
    except Exception as e:
        print(f"❌ AI Engine Error: Server Hugging Face mungkin sedang sibuk atau token salah. Detail: {e}")

if __name__ == "__main__":
    generate_ai_video_script()