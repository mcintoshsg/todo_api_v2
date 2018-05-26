
from todo import create_app
from todo import models

app = create_app('testing')

if __name__ == '__main__':
    models.initialize()
    app.run()   