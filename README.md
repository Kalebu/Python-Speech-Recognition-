<h1 align = "center"> Speech Recognition in Python </h1>


Python-Speech-Recognition
---------------------------

This repository of basic examples on performing Speech Recognitionin Python using Google Speech Recognition Engine.


The original article
-------------------------

To see full article with explanation on source code from this repository **[Click here](https://kalebujordan.com/python-speech-recognition)**


Getting started 🔧
--------------------
Firstly before we begin exploring the source code, you might wanna *clone* or *download* the repository
just as shown below;

```bash
# Clone this repository
$ git clone https://github.com/Kalebu/Python-Speech-Recognition-

# Go into the repository
$ cd Python-Speech-Recognition-
```

## Dependancies

Now you would need to Install all the Dependecies to begin running
playing the Examples 

Linux users  
----------

```bash
 
$ pip3 install pydub
$ pip3 install PyAudio
$ pip3 install SpeechRecognition
```

Window users
-----------

```bash 
$ pip install pydub
$ pip install PyAudio
$ pip install SpeechRecognition
```

Once everything is cleary installed , you're now ready to run the above examples 

Recognition From Microphone 
----------------------------


The first Example *app.py* consist of python code to perform speech recognition 
on sound that is directly fed from Microphone 

To run the Example do the following

```bash 
$ python app.py 
    Adjusting noise 
    Recording for 4 seconds
    Done recording
    Recognizing the text
    Decoded Text : Python is awesome
```

Recognition From Audio File 
-----------------------------

The second Example *app_audio.py* consist of a python code to perform speech recognition from 
sound loaded from local audio file 

To run the Example do the following 

```bash
$ python3 app_audio.py 
    Done recording
    Recognizing the text
    Decoded Text : python programming is the best of all by Jordan
```

Recognizing From Long Audio File 
-----------------------------------

Incase you have a long audio File, loading plus processing it, It takes a quite a while therefore 
the best way is to break the long audio source from file into small chunks and then performing 
speech Recognition on those chunks 

The script *long_audio.py* consist of Python demo code just to that 

To run the example do the Following 

```bash 
$ python3 app_audio.py 
    Done recording
    Recognizing the text
    Decoded Text : python programming is the best of all by Jordan
```

Explore and build your own thing
---------------------------------

Well Hope you had amazing time practicing Some Speech Recognition Now It's your turn to create something useful out of what you just learned.


Give it a star 
--------------
Did you find this information useful, then give it a star 


Credits
-----------
All the credits to [kalebu](github.com/kalebu) 


*The Only limits are the one you have set upon yourself @unkown*