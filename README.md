# Sudoku Solver

## Usage

### Prerequesites:
1.

### Development:

1. Start the server-side flask app:

    ```sh
    $ cd server
    $ python3.9 -m venv env
    $ source env/bin/activate
    (env)$ pip3 install -r requirements.txt
    (env)$ python3 app.py
    ```

1. Start the client-side Node server:
    ```sh
    $ cd client
    $ npm i
    $ npm run serve
    ```

#### .env
A .env file is required in the root of the project:
```
NODE_PORT =
FLASK_PORT =
FLASK_ENV = 'development' (defaults to production, do not set in production)
```
#### CLI Entrypoint
`python3 cli.py`

## Links
[Trello](https://trello.com/c/1lH6BsPv/3-l)
