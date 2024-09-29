from src import app

from datetime import date

@app.route('/', methods=['GET'])
def source_get():
    return "Try to visit /healthcheck"

@app.route('/healthcheck', methods=['GET'])
def healthcheck_get(status=None):
    # Endpoint has to return response code 200
    # Response body should contain current date and server status

    response = {
        "date": date.today().isoformat(),
        "status": "OK"
    }

    return response, 200