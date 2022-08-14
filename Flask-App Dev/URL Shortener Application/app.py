from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyshorteners
import os

app = Flask(__name__)

short_url=''
long_url=''
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqllite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
migrate = Migrate(app, db)

class URLData(db.Model):
    __tablename__='url_shortener'
    id=db.Column(db.Integer,primary_key=True)
    long_url=db.Column(db.String(100))
    short_url = db.Column(db.String(50))
    
    def __init__(self,long_url,short_url): 
        self.long_url=long_url
        self.short_url=short_url
        
        
    # def __repr__(self):
    #    return "Long url - {} and Short url-{}".format(self.long_url,self.short_url)

@app.before_first_request
def create_tables():
    db.create_all()

# db.session.query(URLData).delete()    
# db.session.commit


@app.route('/',methods=["GET","POST"])
def home():
    global short_url,long_url
    if request.method=='POST':
        long_url=request.form.get('in_1')
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(long_url)
        url_append=URLData(long_url,short_url)
        db.session.add(url_append)
        db.session.commit()

    return render_template('index.html',s=short_url)


@app.route('/history')
def history():
    
    all_urls=URLData.query.all()
    return render_template('history.html',all_urls=all_urls)


if __name__ == '__main__':
    app.run(debug=True)    
