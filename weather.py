from distutils.log import debug
import os
from flask import request
from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():

    latitude = request.args.get("lat")
    longitude = request.args.get("lon")

    key = os.environ["API_KEY"]

    complete_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
        str(latitude)+"&lon="+str(longitude)+"&appid="+str(key)

    response = requests.get(complete_url)

    rep = response.json()

    if rep["cod"] != "404":
        html_data = f"""
            |   {str(rep['sys']['country'])}   | {str(rep['coord']['lon']) + ' ' 
                                + str(rep['coord']['lat'])} | {str(rep['main']['temp']) + 'k'} | {str(rep['main']['pressure'])} | {str(rep['main']['humidity'])} |
                """
    else:
        html_data = f" Location Not Found "
    return html_data


if __name__ == '__main__':
    app.run(port = 8081,debug=True)
    main()

