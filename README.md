# Otus Web 4 WSGI Framework

This is a wsgi-compatible framework made by Sergey Zenchenko aka xelnod for Otus Web lessons.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Virtualenv
- Pip


### Installing

Make a new virtualenv (you may as well not if you know what you're doing)

```
$ virtualenv -p python3 otus_web_04
```

Clone this repo

```
$ git clone https://github.com/xelnod/otus_web_04.git
```


Install requirements

```
$ pip install -r requirements.txt
```
## How to use

1. Write some view in views.py - a function which accepts `request` arg and returns response content
2. Wire it to some url in urls.py
3. Run server: `uwsgi uwsgi.ini`

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
