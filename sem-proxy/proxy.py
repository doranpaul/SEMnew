from flask import request, Response, Flask
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://sem-frontend.40070680.qpc.hal.davecutting.uk/", supports_credentials=True)

# Mapping service names to URLs
service_map = {
    'sem-maxmin': "http://sem-maxmin.40070680.qpc.hal.davecutting.uk",
    'sem-sort': "http://sem-sort.40070680.qpc.hal.davecutting.uk",
    'sem-totalhours': "http://sem-totalhours.40070680.qpc.hal.davecutting.uk",
    'sem-stdengagement': "http://sem-stdengagement.qpc.hal.davecutting.uk",
    'sem-riskoffail': "http://sem-riskoffail.40070680.qpc.hal.davecutting.uk",
    'sem-improvementplan': "http://sem-improvementplan.40070680.qpc.hal.davecutting.uk"
}

@app.route('/<string:service_name>', methods=['GET'])
def proxy(service_name):
    # Get the URL for the requested service
    service_url = service_map.get(service_name)
    if not service_url:
        return "Invalid service name", 400

    # Forward the request to the appropriate service
    res = requests.get(service_url, params=request.args)

    # Create the response
    response = Response(res.content, res.status_code)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)