from gtts import gTTS
import os

def text_to_speech(text, language='ar'):
    try:
        # initialize the gTTS object with the given text and Arabic language
        tts = gTTS(text=text, lang=language)

        # Save the speech as an MP3 file
        tts.save("output.mp3")

        # Play the MP3 file:
        os.system("start output.mp3")  # For Windows
        # os.system("afplay output.mp3")  # For macOS
        # os.system("mpg321 output.mp3")  # For Linux
    except Exception as e:
        print(f"Error: {e}")

# The Arabic text you want to convert to speech
arabic_text = """
من اول نظره قلبي هديتو ليك
خليتني نبغيك ونشتاق ليك
نفكر فيك ونهدر عليك
شغلتلي قلبي وشغلتلي تفكيري
مني فكرت كيفاش نبوح ليك
وقفت قدامك ونسيت الكلام
بقيتي تهدر وانا نشوف فيك
نتخيلك بجنبي يدي فيديك
بقيتي تسول فيا وانا نتأمل فيك
"""

# Call the function with Arabic text
text_to_speech(arabic_text, 'ar')

