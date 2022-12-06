from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
global_dict={}
# web server 路由設定
# 若有get request傳送到 / ，就會執行他下面的這個function，function名稱隨意，但不可重複
@app.route('/',methods=['GET'])
def root():
    return 'ok' # 發送response body 為 ok

@app.route('/set',methods=['POST'])
def root1():
    data = request.form.to_dict()
    if data['key'] in global_dict:
        return 'key exist'
    else:
        global_dict[data['key']]=data['value']
        return 'set success'

@app.route('/key_list',methods=['GET'])
def root2():
    return str(global_dict.keys())

@app.route('/get_value/<key>',methods=['GET'])
def root3(key):
    if key not in global_dict:
        return 'key not found'
    else:
        return global_dict[key]# 發送response body 為 ok

@app.route('/update_value',methods=['POST'])
def root4():
    data = request.form.to_dict()
    if data['key'] not in global_dict:
        return 'key not found'  # 發送response body 為 ok
    else:
        global_dict[data['key']]=data['value']
        return 'update success'
@app.route('/delete/<key>',methods=['GET'])
def root5(key):
    if key not in global_dict:
        return 'key not found' 
    else:
        del global_dict[key]
        return 'delete success'
app.run(host="0.0.0.0", port=3000, debug=True)
