from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap
from sqlalchemy import desc
from mail import Mail

app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

# Define the Flask Form 
class CafeForm(FlaskForm):
    cafe_title = StringField("Cafe Name", validators=[DataRequired()])
    cafe_type = SelectField("Cafe Type", validators=[DataRequired()], choices=["Cafe", "Restaurant", "Library"])
    cafe_location = StringField("Cafe Location", validators=[DataRequired()])
    cafe_desc = StringField("Description", validators=[DataRequired()])
    cafe_power = SelectField("Power Outlet", choices=["⭐️","⭐️⭐️","⭐️⭐️⭐️","⭐️⭐️⭐️⭐️","⭐️⭐️⭐️⭐️⭐️"], validators=[DataRequired()])
    cafe_loc = SelectField("Location", choices=["⭐️","⭐️⭐️","⭐️⭐️⭐️","⭐️⭐️⭐️⭐️","⭐️⭐️⭐️⭐️⭐️"], validators=[DataRequired()])
    cafe_cq = SelectField("Cofe Quality", choices=["⭐️","⭐️⭐️","⭐️⭐️⭐️","⭐️⭐️⭐️⭐️","⭐️⭐️⭐️⭐️⭐️"], validators=[DataRequired()])
    cafe_wf = SelectField("Work Friendly", choices=["⭐️","⭐️⭐️","⭐️⭐️⭐️","⭐️⭐️⭐️⭐️","⭐️⭐️⭐️⭐️⭐️"], validators=[DataRequired()])
    cafe_url_map = StringField("Cafe URL Google maps", validators=[DataRequired(), URL()])
    cafe_img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Add")

# Define the DB Table for Cafe
class Cafe(db.Model):
    __tablename__ = "cafes"
    id = db.Column(db.Integer, primary_key="True")
    cafe_title = db.Column(db.String(30), unique=True, nullable=False)
    cafe_type = db.Column(db.String(50), nullable=False)
    cafe_type_img = db.Column(db.String(50), nullable=False)
    cafe_location =db.Column(db.String(100), nullable=False)
    cafe_desc = db.Column(db.String(1000))
    cafe_power = db.Column(db.String(10), nullable=False)
    cafe_loc = db.Column(db.String(10), nullable=False)
    cafe_cq = db.Column(db.String(10), nullable=False)
    cafe_wf = db.Column(db.String(10), nullable=False)
    cafe_or = db.Column(db.String(50), nullable=False)
    cafe_url_maps = db.Column(db.String(3000), nullable=False)
    cafe_img_url = db.Column(db.String(3000), nullable=False)

# db.create_all()

# Initialize mail object
mail = Mail()

# Home Route 
@app.route('/', methods=["GET", "POST"])
def home():
   
    if request.method == "POST":
        
        search = request.form["search"]
        # search_cafes = db.session.query(Cafe).filter_by(Cafe.cafe_title.like(search))
        search_cafes = Cafe.query.filter(Cafe.cafe_title.like("%{Oliva}%"))
        print(search_cafes)
        if search_cafes:
            print(search_cafes)
            return render_template("index.html", cafes=search_cafes)

    cafes = Cafe.query.order_by(desc(Cafe.cafe_or)).all()
    
    return render_template("index.html", cafes=cafes)

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        text = request.form["text"]

        body = f"Name: {name}\n Email: {email}\n Phone: {phone}\n Message: {text}"

        # Send the mail through SMTP protocol
        mail.send_email(body)

    return render_template("contact.html")

# Add new Cafe Route
@app.route("/add", methods=["GET", "POST"])
def add():
    form = CafeForm()

    if form.validate_on_submit():
        title = form.cafe_title.data
        type = form.cafe_type.data
        location = form.cafe_location.data
        description = form.cafe_desc.data
        power = form.cafe_power.data
        loc = form.cafe_loc.data
        cq = form.cafe_cq.data
        wf = form.cafe_wf.data
        map_url = form.cafe_url_map.data
        img_url = form.cafe_img_url.data

        if type == "Cafe":
            img_type = "https://cdn-icons-png.flaticon.com/512/3994/3994539.png"
        elif type == "Restaurant":
            img_type = "https://cdn-icons-png.flaticon.com/512/7577/7577691.png"
        else:
            img_type = "https://cdn-icons-png.flaticon.com/512/3994/3994539.png"

        average = ((int(len(power)) + int(len(loc)) + int(len(cq)) + int(len(wf))) / 2) / 4

        overall = f"⭐️ {round(average, 2)}"

        new_cafe = Cafe(cafe_title=title, cafe_type=type, cafe_type_img=img_type, cafe_location=location, cafe_desc=description, cafe_power=power, 
                        cafe_loc=loc, cafe_cq=cq, cafe_wf=wf, cafe_or=overall, cafe_url_maps=map_url, cafe_img_url=img_url)

        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for("add"))

    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
