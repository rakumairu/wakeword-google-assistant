### Prequisites

* Install [Python 3.X](https://www.python.org/downloads/)
* Clone this project to your local computer
* [Set Up Hardware and Network Access](https://developers.google.com/assistant/sdk/guides/service/python/embed/setup?hardware=rpi)
* [Configure and Test the Audio](https://developers.google.com/assistant/sdk/guides/service/python/embed/audio?hardware=rpi)
* [Configure a Developer Project and Account Settings](https://developers.google.com/assistant/sdk/guides/service/python/embed/config-dev-project-and-account)
* [Register the Device Model](https://developers.google.com/assistant/sdk/guides/service/python/embed/register-device)
* [Generate Credentials](https://developers.google.com/assistant/sdk/guides/service/python/embed/install-sample#generate_credentials)
* copy crendetials.json to this project root folder
* copy model file (.ppn) to this project root folder

### Installing

Installing all packages required in this app

Open command prompt/terminal and move to this project folder then install all requirements for this project

```
cd wakeword-google-assistant
pip install -r requirements.txt
```

### Running the server

To run this app, you can run the development server using this command

```
python wakeword.py
```
