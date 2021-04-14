import requests,json
def get_request(url):
    try:
        data = requests.get(url).text
        data_json = json.loads(data)
        return data_json
    except:
        return False
    
def list_users(url):
    try:
        data_json = get_request(url)

        f = open('user_data.html', 'w')
        message = """
        <html>
        <head>
        <style>
        h1 {text-align: center;}
        </style>
        </head>
        <body>
        <h1>Hello ReqRes users!</h1>"""

        #</body>
        #</html>"""
        f.write(message)
        f.close()
        for name in data_json['data']:
            write_file('user_data.html', name['first_name'], name['email'], name['avatar'])

        f = open('user_data.html', 'a')
        content = """
        </body>
        </html>
        """
        f.write(content)
        f.close()
        return True
    except:
        return False




def write_file(filename, arg1, arg2, arg3,  *argv):
    try:
        f = open(filename, 'a')
        content = """
        <br><b> %s </b>
        <p> %s </p>
        <img src="%s" alt="%s" />
        """ % (arg1, arg2, arg3, arg1)
        f.write(content)
        f.close()
    except e:
        return e

url = "https://reqres.in/api/users?page=2"
list_users(url)
