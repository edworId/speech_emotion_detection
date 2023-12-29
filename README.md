<h1 align="center"> Speech Emotion Recognition using a shell GUI menu </h1>

<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=COMPLETO&color=GREEN&style=for-the-badge"/>
</p>

Detect emotions in audio with this speech emotion detection project. The system analyzes voice recordings and categorizes them into emotions. Utilizing the RAVDESS dataset, the model is trained to recognize a wide range of emotional expressions using mel spectograms and MFCC features.

The dialog command is a command-line tool used to create text-based user interfaces on Unix-like systems. It provides an interactive way to display dialog boxes, menus, and forms in the terminal.

## Basic Requirements

You will need to install **Dialog** package, run in your terminal:

```
sudo apt-get install dialog
```

You must give permissions to use this project, run in your terminal:

```
chmod a+x -v *.sh
```

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/edworId/speech_emotion_detection.git
    cd speech_emotion_detection
    ```

2. Run the main script:

    ```bash
    ./audio.sh
    ```

3. Follow the instructions in the menu to choose the desired action.

  - **RECORD**
  - **PLAY**
  - **MEL SPECTOGRAM**
  - **MFCC**
  - **EXIT FROM PROGRAM**

## DATASET

Dataset: https://zenodo.org/records/1188976

<h1 align="center">  </h1>
<p align="center">
<img width="900", img src="https://raw.githubusercontent.com/edworId/speech_emotion_detection/main/menu_audio.png"/>
</p>

<h6 align="center">This interface was built using Dialog, text based menu. </h6>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


<h2> Author </h2>

[<img src="https://avatars.githubusercontent.com/u/110691832?s=400&u=e671447386d38975c165bff78b715ea80549c069&v=4" width=115><br><sub>Edmundo Lopes Silva</sub>](https://github.com/edworId)  

<p align="center">
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Shell-009000?style=for-the-badge&logo=&logoColor=green"/>
</p>
