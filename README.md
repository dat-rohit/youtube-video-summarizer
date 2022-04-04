# Youtube-video-summarizer

This app was built with the purpose of getting a short text summary of any given youtube video (in English language only at the moment). It relies on OpenAI's API that provides access to GPT-3, mainly used for natural language tasks.


## Installation

Install the needed packages listed in requirements.txt easily with:

```bash
$ pip install -r requirements.txt
```


## Usage

Once in the project folder, run the app with:

```bash
$ streamlit run main.py
```

The app should then be accessible at ```http://localhost:8501```

The web interface built using Streamlit allows you to input a youtube link (.be format accepted only, e.g: ```https://youtu.be/ukzFI9rgwfU```) and get a text summary of its content. The sidebar has a slider that lets you adjust the length you want the summary to be.

![preview](https://github.com/dat-rohit/youtube-video-summarizer/blob/main/interface_preview.jpg)


## License
[MIT](https://choosealicense.com/licenses/mit/)