import azure.cognitiveservices.speech as speechsdk
import random
ImportLocation = open("Locations.txt", "r", encoding="utf8")
Location = ImportLocation.readlines()

ImportAnimal = open("Animals.txt", "r", encoding="utf8")
Animal = ImportAnimal.readlines()

Salt = "Salz"

LocationCount = len(Location)
AnimalCount = len(Animal)

def SaltRandomizer():
    LocationRandomizer = random.randrange(0,LocationCount)
    AnimalRandomizer = random.randrange(0,AnimalCount)
    return LocationRandomizer,AnimalRandomizer

SaltRandomizer()

MagicSalt = Location[(SaltRandomizer()[0])].capitalize().strip() + " " + Animal[(SaltRandomizer()[1])].strip() + " " + Salt

text_out = str("Dein magisches Salz ist: " + MagicSalt)

ImportLocation.close()
ImportAnimal.close()






















#AZURE SPEECH ----------------------------------------------------------------------------------------------------------

# Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
speech_key, service_region = "d52dab0700e84faabbaf29f73432a631", "westeurope"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates an audio configuration that points to an audio file.
# Replace with your own audio filename.
audio_filename = "salt_choice.wav"
audio_output = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename=None, stream=None)

# Creates a synthesizer with the given settings
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output)

# Synthesizes the text to speech.
# Replace with your own text.
text = text_out
result = speech_synthesizer.speak_text_async(text).get()

# Checks result.
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to [{}] for text [{}]".format(audio_filename, text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")