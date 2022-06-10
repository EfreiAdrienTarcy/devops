from distutils.log import debug
import os
import requests
from flask import FLASK
import json

app = FLASK(__name__)


@app.route('/<data>', methods=['GET'])
def main(data):

    #latitude = os.environ["LAT"]
    #longitude = os.environ["LONG"]

    split = data.split('&')

    latitude = split[0]
    longitude = split[1]

    key = os.environ["API_KEY"]

    complete_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
        str(latitude)+"&lon="+str(longitude)+"&appid="+str(key)

    response = requests.get(complete_url)

    rep = response.json()

    if rep["cod"] != "404":
        html_data = f"""
            <table border="1">
            <tr>
                <td>country_code</td>
                <td>coordinate</td>
                <td>temp</td>
                <td>pressure</td>
                <td>humidity</td>
            </tr>
            <tr>
                <td>{str(rep['sys']['country'])}</td>
                <td>{str(rep['coord']['lon']) + ' ' 
                                + str(rep['coord']['lat'])}</td>
                <td>{str(rep['main']['temp']) + 'k'}</td>
                <td>{str(rep['main']['pressure'])}</td>
                <td>{str(rep['main']['humidity'])}</td>
            </tr>

            </table>
                """
    else:
        html_data = f" Location Not Found "
    return html_data


if __name__ == '__main__':
    app.run(port = 8081,debug=True)

