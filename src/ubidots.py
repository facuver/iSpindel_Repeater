import usocket as socket

def send_data(token,name, body):
    
    s = socket.socket()
    s.connect(("industrial.api.ubidots.com", 80))
    request=bytes('POST /api/v1.6/devices/%s HTTP/1.1\r\nHost: industrial.api.ubidots.com\r\nX-Auth-Token: %s\r\nContent-Type: application/json\r\nContent-Length: %s\r\n\r\n%s\r\n' % ( name , token, len(body), body), 'utf8')
    
    print("Sending data to Ubidots")
    s.send(request)
    dump_socket(s)

def dump_socket(s):
    try:
        while True:
            data = s.recv(100)
            if data:
                print(str(data, 'utf8'), end='')
            else:
                print('')  # end with newline
                s.close()
                break
    except:
        s.close()
        raise
    



