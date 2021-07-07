from microdot_asyncio import Microdot ,send_file, Response
import ujson
from cfg import configs, update_configs , iSpindels ,ip
import wifi

app = Microdot()

def populate_template(filename,values):
    try:
        with open(filename,"r") as f:
            f = f.read()
        return f.format(**values)
    except Exception:
        return "ERROR POPULATING TEMPLATE"


@app.route('/')
async def hello(request):
   
    return send_file('/www/header.html')

@app.get("/main_view")
async def main_view(request):

    return send_file("/www/main_view.html")

@app.get("/config")
async def config_get(request):

    return Response(body=populate_template("/www/config.html" , configs) , headers={'Content-Type': 'text/html'})


@app.post("/config")
async def config_post(request):
    old_sta = configs["STA_essid"]
    configs["STA_essid"] = request.form["STA_essid"]
    configs["STA_password"] = request.form["STA_password"]
    configs["ubidots_token"] = request.form["ubidots_token"]
    configs["update_interval"] = request.form["update_interval"]
    configs["AP_password"] = request.form["AP_password"]
    print(update_configs(configs))
    if old_sta != configs["STA_essid"]:
        from machine import reset
        reset()
       
    return send_file("/www/main_view.html")



@app.get("/iSpindel_view")
async def iSpindel_view(request):
    #name = list(iSpindels.keys())[0]
    htmldoc = '<div class="">'

    for i in iSpindels:

        htmldoc += populate_template("/www/iSpindel_view.html" , iSpindels[i])

    htmldoc += "</div>"
    return Response(body = htmldoc ,headers={'Content-Type': 'text/html'})



@app.post('/gravity' )
async def gravity(request):
    global iSpindels
    recive = ujson.loads(request.body.decode("utf-8"))    
    
    iSpindels[recive["name"]] = recive
    iSpindels[recive["name"]].pop("temp_units")
        
    return

@app.get("/alive")
async def alive(request):
    return "yes"

@app.get("/get_ip")
async def get_ip(request):
    return str(ip)

@app.get("/www/htmx.min.js")
async def htmx(request):
    return send_file("/www/htmx.min.js")


@app.get("/www/style.css")
async def style(request):
    return send_file("/www/style.css")

# @app.get("/www/htmx.min.js")
# async def htmx_gz(request):
#     with open("/www/htmx.min.js.gz","rb") as f:
#         f= f.read()

#     return Response(body=f,status_code=200 , headers={'Content-Type': 'application/javascript' , 'Content-Encoding': 'gzip'})



@app.route('/shutdown')
async def shutdown(request):
    request.app.shutdown()
    