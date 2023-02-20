# TPC Client - Server Calculator
## Description:
Client-server calculator. 
Evaluates simple expressions including pow, truediv, floordiv and parentheses.

You can enter expression using keyboard or load it from file.

It is using _Reversed Polish Notation_ for calculation.

(You can expand it using `utils/notation.py`) 

Written w/ `asyncio streams` library. The data sends in JSON format.
## Usage:
It is preferable to use terminal.

Create `venv`,  and install 
```
python -m venv venv
```
activate it
```
. ./venv/bin/activate  # For Unix users
.\venv\Scripts\activate  # For Windows users
```
then install `requirements.txt`
```
pip install -r requirements.txt
```

You can edit the configuration in `config.cfg` for each application
### Server:
```
python start_server.py
```
### Client:
```
python start_client.py
``` 


