
from todo import create_app
import todo.models as models

app = create_app('development')
# models.init_db()

if __name__ == '__main__':
    app.run()   