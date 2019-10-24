from app import create_app,db
from flask_script import Manager, Server
from app.models import User,Pitch,Comment
from flask_migrate import Migrate, MigrateCommand


app =  create_app('production')
manager = Manager(app)
manager.add_command('server', Server)

@manager.command
def test():
   '''run unittest'''
   import unittest
   tests = unittest.TestLoader().discover('test')
   unittest.TextTestRunner(verbosity=2).run(tests)
@manager.shell
def make_shell_context():
   return dict(app = app, db = db, User = User,Pitch = Pitch, Comment = Comment )
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
   app.secret_key = '123456'
   manager.run()
