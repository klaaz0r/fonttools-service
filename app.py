import subset
import convert
import health
from logger import log
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

log.info("starting subset service..")

@app.route("/subset", methods=["POST"])
def handleSubset():
    try:
        text = request.json['text']
        font = request.json['font']
        log.info("subsetting font..")
        subset = subset.subsetFont(font, text)
        return make_response(jsonify(subset), 200)
    except:
        log.warn("subsetting font went wrong", request)
        return make_response(jsonify(error="subsetting went wrong"), 500)

@app.route("/convert", methods=["POST"])
def handleConvert():
    try:
        kind = request.json['type']
        font = request.json['font']
        log.info('conerting font..')
        converted = convert.convertFont(font, kind)
        return make_response(jsonify(converted), 200)
    except:
        log.warn("converting font went wrong")
        return make_response(jsonify(error="subsetting went wrong"), 500)

@app.route("/health", methods=["GET"])
def handleHealth():
    return make_response(jsonify(health.getHealth()), 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9097)
