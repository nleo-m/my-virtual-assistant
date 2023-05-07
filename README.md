## About
This is a Python-based virtual assistant with speech recognition and tts.  
Currently development is focused on linux dists. And there is a **lot to do** still.

## Setup
First of all, I recommend creating an [virtual environment](https://docs.python.org/pt-br/3/library/venv.html#creating-virtual-environments) – and don't forget to activate it ;P –, then you're going to need to install required libs:  
  `pip install -r requirements.txt`
  
Copy env.example to .env, and set up your ambient variables. After that, you're good to go, run:  
  `python main.py`
  
It will passive listen, and when you say your "BOTNAME", it will ask how it may aid you and start active listening.

If you're running into issues, you might also need to install some or all of these packages, using your package manager:
   * python3-dev: Python development headers;
   * portaudio19-dev: Development headers for PortAudio, a cross-platform api that allows developers to control audio hardware directly;
   * libpulse-dev: Development headers for the PulseAudio sound server, which is the default for many linux distributions;
   * espeak: Compact open source text-to-speech engine, used by default by the virtual-assistant;
   
