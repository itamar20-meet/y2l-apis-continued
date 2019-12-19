from flask import Flask, render_template, request
app = Flask(__name__)
import requests,json

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    headers = {'Authorization':"b31090b2c4664a2c88472391c9fa2f1a"}
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response.status_code
    response.content
    return render_template('home.html', results=response.content)

if __name__ == '__main__':
    app.run(debug=True)