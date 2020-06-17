# Flog

# Install Dependencies & Run Tests

You should create a virtualenv for this project.  Run pip and all commands from that virtualenv.

```
$ docker-compose up -d
$ pip install -r requirements.txt
$ pytest
..........                                         [100%]
10 passed in 2.03s
```

If all tests pass, you are ready to participate in the tutorial.

## Docker

The above assumes you have Docker & docker-compose available to setup services.  You don't have to
use docker.  You could also setup these services natively on your system and change the connection
string in app.py.
