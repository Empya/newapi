from flask import Flask, request, jsonify

app = Flask(__name__)

data = [
{
"name":"1"
}, 
{
"name":"2"
}, 
{
"name":"3"
}, 
{
"name":"4"
}
]

@app.get("/names") 

def show_names():
    return jsonify(data)
    
@app.get("/name/<int:id>")

def get_name(id):
    if request.is_json:
        for any in data:
            if str(any["name"]) == str(id):
            
                return jsonify(any)
                
            else:
                return {"error": 404}                

    else: 
        return {"error": "not json request"}    
    
    

