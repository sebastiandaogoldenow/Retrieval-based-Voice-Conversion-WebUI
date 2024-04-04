# How to train a good RVC model without GPU requirements (using Colab and Kaggle)?
## Step 1: Prepare dataset
- Collect 10 - 15 mins audio data with high quality voice.
- Reduce noisy (ex: Deep Filter Net).
- Truncate silent, split audio to 10s segments (ex: Audacity)
- Zip all audio and upload it to Google Drive.

## Step 2: Training model
-   Upload notebook rvc-rmvpe-ru-main.ipynb to Kaggle and enable GPU T4 x2
-   Replace link download in notebook by your link dataset on Google Drive.
-   Replace path to your dataset.
-   Set number of epoch and start training.

## Step 3: Inference model (can run on CPU)
- When completed training, download weight (in /assets/weights/) and index feature (in /logs/) to your local.
- Clone this repo and install requirement.
```bash
pip install torch torchvision torchaudio
pip install requirements.txt
```
- Download pre-models to inference
```bash
#Download all needed models from https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main/
python tools/download_models.py
```
- Put trained-weights to "/assets/weights/" and index feature to "/logs/"
- Install FFmepg for Ubuntu
```bash
sudo apt install ffmpeg
```

- Run on web
```bash
python infer-web.py
```

- Choose the weights and index feature, choose the audio path to convert speech to speech.