from flask import render_template, redirect, Flask, request, session, url_for
from flask_session import Session
from cs50 import SQL
from helpers import errors, country_name
import requests
from datetime import *  
app = Flask(__name__)


#session=======================================================================
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
#==============================================================================


#database seting=======================================================================
db = SQL("sqlite:///multi Service.db")
#======================================================================================


#weather seting=======================================================================
API_key = "51241000b805407308f5a6dee017192f"
#=====================================================================================



#to do list================================================================================================================================
@app.route("/",methods=["GET","POST"])
def index():

    #To protect against intrusion without logging in
    if len(session) <= 0:
        return redirect("/login")
    #===============================================

    if request.method == "POST":
        todo_name = request.form["todo_name"]
        db.execute("INSERT INTO todos (user_id, Content, done, deleted) VALUES (?,?,?,?)",session["user_id"], todo_name, "False", "False")


    if len(session) >= 1:
        todos = db.execute("SELECT * FROM todos WHERE user_id  = ? AND deleted = ?",session["user_id"],"False") 
        return render_template("index.html",todos=todos)
    
    return redirect("/login")

# delete button-----------------------------------------------------------------------------------
@app.route("/delete", methods=["GET","POST"])
def delete():
    delete_value = request.form["delete"].split(",!@#$%^&*(sosossdfs222)")

    #To modify the value of the deleted in the database
    db.execute("UPDATE todos SET deleted = ? WHERE user_id = ?  AND id = ? AND Content = ? ", "True", session["user_id"], delete_value[0],delete_value[1])
    return redirect(url_for('index'))
# -----------------------------------------------------------------------------------

# checkBox button-----------------------------------------------------------------------------------
@app.route("/checkBox", methods=["GET","POST"])
def checkBox():
    checkBox_value = request.form["checkBox"].split(",!@#$%^&*(sosossdfs222)")

    #To modify the value of the done in the database
    db.execute("UPDATE todos SET done = ? WHERE user_id = ?  AND id = ? " ,'True', session["user_id"], checkBox_value[0])
    return redirect(url_for('index'))
   
#-----------------------------------------------------------------------------------

#========================================================================================================================================

@app.route("/logout", methods=["GET"])
def logout():

    session.clear()
    return redirect("/")



@app.route("/login", methods=["GET","POST"])
def login():

    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username:
            return errors("The username field must be filled",404)

        elif not password:
            return errors("The password field must be filled",404)
            

            
        row = db.execute("SELECT * FROM users WHERE username = ?",username)

        


        if len(row) != 1 or password != row[0]["password"]:
            return errors("There is an error in the login information",404)

                  

        elif len(row) != 0:
            session["user_id"] = row[0]["id"]
            return redirect("/")
        
    else:         
        return render_template("login.html") 


@app.route("/register", methods=["GET","POST"])
def register():

    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        
        if not username:
            return errors("The username field must be filled",505)

        elif not password:
            return errors("The password field must be filled",505)
        
        elif not confirm:
            return errors("The confirm password field must be filled",505)
          
        elif password != confirm:
            return errors("Password fields must match",505)

        check = db.execute("SELECT * FROM users WHERE username = ?",username)     

        if len(check) != 0:
            return errors("Username already taken",505)

       
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)",username, password)
        return redirect("/")
    return render_template("register.html")



@app.route("/calculator", methods=["GET","POST"])
def calculator():
     #To protect against intrusion without logging in
    if len(session) <= 0:
        return redirect("/login")
    #===============================================
    return render_template("calculator.html")


@app.route("/weather-news", methods=["GET","POST"])
def weatherNews():

    #To protect against intrusion without logging in
    if len(session) <= 0:
        return redirect("/login")
    #===============================================

    #Default mode for variables used on the page
    weather_data = ""
    city_name = "City name"
    temperature = "temperature"
    country__name = "country name"
    weather = "weather"
    image = "weather"
    images = ["clear sky","few clouds","clouds","mist","snow","rain","thunderstorm","	shower rain","broken clouds","scattered clouds"]
    #====================================================================================================================================

    if request.method == "POST":
        
        #Requirement to know whether the weather field is empty
        if request.form.get("weather") == "":
            return redirect("/weather-news")
        

        # get_weather_data 
        name = request.form.get("weather")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={API_key}"
        req = requests.get(url)
        weather_data = req.json()
        #======================================================================================

        #A condition to know if the connection is valid
        if weather_data["cod"] != "404":
            city_name = weather_data["name"]
           # An equation to convert the following value from API to Kelvin scale
            temperature = round(weather_data ["main"]["temp"] - 273.15,2)
           #=================================================================== 
            country__name = country_name[weather_data["sys"]["country"]]
            image = weather_data["weather"][0]["description"]
            weather = image
            if image not in images:
                image = "weather"

            #Store data after query    
            db.execute("INSERT INTO weather (user_id, city_name, weather_condition, temperature, country_name,image) VALUES (?,?,?,?,?,?)",session["user_id"],city_name,weather,temperature,country__name,image)    
        else:
            return errors(weather_data["message"],weather_data["cod"])     
        #====================================================================
    return render_template("weather-news.html",city_name = city_name , temperature=temperature, country_name = country__name, weather=weather, image=image)

    







@app.route("/sleep", methods=["GET","POST"])
def sleep():
     #To protect against intrusion without logging in
    if len(session) <= 0:
        return redirect("/login")
    #===============================================
    if request.method == "POST":

        masseg  = "You should sleep at exactly the same time"

        #Fetch information
        time = request.form.get("time")
        hours = request.form["select"].split(":")
        #========================================

        # Check for empty boxes
        if time == "":
            return redirect("/sleep")
        #==============================================


        #To adjust the time to match my code here
        t = datetime.strptime(time,"%H:%M")
        sleep_time = str(t - timedelta(hours=int(hours[0]), minutes=int(hours[1]))).split(" ")
        #======================================================================================

        # To convert the time of the sleep time variable from 24 hours to 12 hours
        hour = sleep_time[1]
        system_24_hour =  hour[:len(hour) -3]
        system_12_hour = datetime.strptime(system_24_hour, "%H:%M").strftime("%I:%M %p")
        #=========================================================================

        # Adding information to the database
        db.execute("INSERT INTO Sleep_cycles (user_id, Desired_wake_up_time, system_12_hour, system_24_hour) VALUES (?,?,?,?)",session["user_id"],time,system_12_hour, system_24_hour)    


        return render_template("sleep.html", masseg=masseg, hour=system_12_hour)
    return render_template("sleep.html")



# Logs secten=======================================================================

@app.route("/log", methods=["GET","POST"])
def log():
    #To protect against intrusion without logging in
    if len(session) <= 0:
        return redirect("/login")
    #===============================================

    return render_template("log.html")




@app.route("/to_do_list_log", methods=["GET"])
def To_Do_list_logs():
    #To protect against intrusion without logging in
    if len(session) <= 0:
        return redirect("/login")
    #===============================================
    
    data = db.execute("SELECT Content, done, deleted, Date_created FROM todos WHERE user_id = ?",session["user_id"])
    return render_template("to_do_list_log.html",data=data)


@app.route("/weather_log", methods=["GET"])
def weather_logs():
    #To protect against intrusion without logging in
    if len(session) <= 0:
        return redirect("/login")
    #===============================================

    data = db.execute("SELECT city_name, weather_condition, temperature, country_name, image, Query_history FROM weather WHERE user_id = ?",session["user_id"])
    print(data)
    return render_template("weather_log.html",data=data)


@app.route("/sleep_log", methods=["GET"])
def sleep_logs():
    #To protect against intrusion without logging in
    if len(session) <= 0:
        return redirect("/login")
    #===============================================

    data = db.execute("SELECT Desired_wake_up_time,system_12_hour,system_24_hour,Query_history FROM Sleep_cycles WHERE user_id = ?",session["user_id"])

    
    return render_template("sleep_log.html",data=data)
# End # Logs secten=================================================================