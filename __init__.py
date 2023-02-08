from flask import Flask, jsonify, request

from .sample import Sample, SampleSchema

app = Flask(__name__)

samples = [ Sample('HelloWorld') ]

@app.route("/samples")
def get_sample():
    schema = SampleSchema(many=True)
    result = schema.dump(samples)
    return jsonify(result)

@app.route("/sample")
def get_sample_by_name():
    name = request.args.get('name')
    schema = SampleSchema(many=True)
    result = schema.dump(
        filter(lambda s: name in s.name, samples)
    )
    return jsonify(result)

@app.route("/sample", methods=['POST'])
def add_sample():
    newSample = request.get_json()
    samples.append(newSample)
    return '', 204
