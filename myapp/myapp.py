#import requests
import psutil
import json
import time
import os




from flask import Flask, render_template, send_from_directory,request
app = Flask(__name__, static_url_path='')
app.debug = True


@app.route('/')
def hello_world():

    cpuLoad = str( psutil.cpu_percent())
    return '<h2>Hello, World!</h2> <h3>my CPU Load is at: '+cpuLoad+'</h3>'



@app.route('/test')
def api_test():
    name = "anyuser"
    if "name" in request.args: 
        name = request.args.get("name")
    company = request.args.get("company")
    return render_template('test.html',name=name,company=company)


@app.route('/index')
def api_index():
    return render_template('index.html')

@app.route('/news')
def api_news():
    return render_template('news.html')

@app.route('/contact')
def api_contact():
    return render_template('contact.html')

@app.route('/contactTestFormular')
def api_contactTestFormular():
    return render_template('contactTestFormular.html')

@app.route('/about')
def api_about():
    return render_template('about.html')

# POST : Information wird von Postman ausgegeben für das Konatkformular
# und wird in JSON-Form gespeichert
@app.route('/api/contactform', methods=["POST"] )
def contactform(): 
    #curDirTest = "/home /manuha /myapp /jsons/"            # zum Testen für den richtigen Pfad
    targetDir= '/home/manuha/myapp/jsons'
    #real_path = os.path.realpath(curDirTest)
    #real_path_test = os.path.dirname(os.path.realpath(curDirTest))
    #curDir = os.path.dirname(os.path.realpath(__file__))    # Pfad so ändern, dass die curDir in einen separaten Ordner für die JSON führt? (os.path.realpath(__file__) -> jsons folder)
    curTime = int(time.time())                      #aktuelle Zeit wird deklariert und initialisiert
    kvStore ={}                                     #Array für keys & values
    if len(request.form) > 0:                       #wenn Anzahl größer 0 der requests aus dem Formular
        for key,val in request.form.items():        #wird für jeden key und value aus der request 
            kvStore[key] = val                      #ein key einem value zugeordnet

    jsonOut = json.dumps(kvStore)                   #json.dumps() wandelt values aus dem kv-array in json-Format um
    #f = open(curDir+"/"+ str(curTime)+".txt","w+")  #open() erstellt neuen File, hier in .txt Format 
    f = open(targetDir+"/"+ str(curTime)+".txt","w+")
    f.write(jsonOut)                                #write schreibt JSON in den von open() erstellten file
    return jsonOut 





if __name__ == '__main__':
    app.run(host="0.0.0.0")