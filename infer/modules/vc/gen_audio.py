import os
from google.cloud import texttospeech as tts

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./key.json"

def gen_audio(text, speed_rate, language, name):
    client = tts.TextToSpeechClient()

    synthesis_input = tts.SynthesisInput(text=text)

    voice = tts.VoiceSelectionParams(
        language_code=language,
        name=language+"-"+name,
    )

    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.MP3,
        speaking_rate=speed_rate,
        effects_profile_id=["large-home-entertainment-class-device"],
        volume_gain_db=-60,
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("./tts_script.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "tts_script.mp3"')
        

def list_voices(language_code=None):
    client = tts.TextToSpeechClient()
    response = client.list_voices(language_code=language_code)
    voices = sorted(response.voices, key=lambda voice: voice.name)

    print(f" Voices: {len(voices)} ".center(60, "-"))
    for voice in voices:
        languages = ", ".join(voice.language_codes)
        name = voice.name
        gender = tts.SsmlVoiceGender(voice.ssml_gender).name
        rate = voice.natural_sample_rate_hertz
        print(f"{languages:<8} | {name:<24} | {gender:<8} | {rate:,} Hz")


