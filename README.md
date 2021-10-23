# Sudoku Solver

## Usage

1. Start the server-side flask app:

    ```sh
    $ cd server
    $ python3.8 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python3 -m flask run
    ```

1. Start the client-side Node server:
    ```sh
    $ cd client
    $ npm i
    $ npm run serve
    ```

### .env
A .env file is required in the root of the project:
```
NODE_PORT =
FLASK_PORT =
FLASK_ENV = 'development' (defaults to production, do not set in production)
```
### CLI Entrypoint
`python3 cli.py`

## Future Goals
* [ ] Validate a starting board
* [ ] Some sort of "solvable sudoku" API
* [ ] Website
  * [ ] Hint system (Solve the requested square)
  * [ ] Decide whether placing a wrong number is alerted or not