from not_foss import app
from waitress import serve 

serve(app, host='127.0.0.1', port=8080)

if __name__ == '__main__':
    app.run(debug=True)