import pvporcupine
import struct
import pyaudio

import assistant.pushtotalk as pushtotalk

PROJECT_ID = 'hey-lumi'
DEVICE_MODEL_ID = 'hey-lumi-hey-lumi-e75s95'
CREDENTIALS_PATH = './credentials.json'
MODEL_PATH = './hey_lumi.ppn'

handle = pvporcupine.create(keyword_paths=[MODEL_PATH])
pa = pyaudio.PyAudio()
audio_stream = pa.open(
                rate = handle.sample_rate,
                channels = 1,
                format = pyaudio.paInt16,
                input = True,
                frames_per_buffer = handle.frame_length)

try:
    print('started')
    while True:
        pcm = audio_stream.read(handle.frame_length)
        pcm = struct.unpack_from("h" * handle.frame_length, pcm)
        keyword_index = handle.process(pcm)
        if keyword_index >= 0:
            # detected
            pushtotalk.main(
                project_id = PROJECT_ID,
                device_model_id = DEVICE_MODEL_ID,
                credentials  = CREDENTIALS_PATH,
                once = True
            )
            pass
finally:
    if handle is not None:
        handle.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()