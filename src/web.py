from microdot_asyncio import Microdot ,send_file, Response
import ujson
from cfg import configs, update_configs , iSpindels 



app = Microdot()

def populate_template(filename,values):
    try:
        with open(filename,"r") as f:
            f = f.read()
        return f.format(**values)
    except:
        return "nanoi"


@app.route('/')
async def hello(request):
   
    responce = send_file("/www/header.html")
    return responce

@app.get("/config")
async def config_get(request):
    #with open("/www/config.html","r") as index:
        #htmldoc = index.read().format(STA_essid = configs["STA_essid"] ,  STA_password =  configs["STA_password"] ,     ubidots_token =  configs["ubidots_token"] , update_interval = configs["update_interval"]  , AP_password = configs["AP_password"] )
        #htmldoc = index.read().format(**configs)   
    #return Response(body=htmldoc, headers={'Content-Type': 'text/html'})
    
    return Response(body=populate_template("/www/config.html" , configs) , headers={'Content-Type': 'text/html'})

@app.get("/iSpindel_view")
async def iSpindel_view(request):
    name = list(iSpindels.keys())[0]
    return Response(body=populate_template("/www/iSpindel_view.html" , iSpindels[name]) ,headers={'Content-Type': 'text/html'})


@app.post("/config")
async def config_post(request):

    configs["STA_essid"] = request.form["STA_essid"]
    configs["STA_password"] = request.form["STA_password"]
    configs["ubidots_token"] = request.form["ubidots_token"]
    configs["update_interval"] = request.form["update_interval"]
    configs["AP_password"] = request.form["AP_password"]
    print(update_configs(configs))

    return send_file("/www/index.html")

@app.route('/gravity' ,methods = "POST")
async def gravity(request):
    global iSpindels
    recive = ujson.loads(request.body.decode("utf-8"))    
    
    iSpindels[recive["name"]] = recive
    
    iSpindels[recive["name"]].pop("temp_units")
    #iSpindels[recive["name"]].pop("name")
        
    return

@app.post("/clicked")
def clicked(request):
    htmldoc = "HOLA"
    return Response(body=htmldoc, headers={'Content-Type': 'text/html'})

@app.get("/www/htmx.min.js")
def htmx(request):
    return send_file("/www/htmx.min.js")
