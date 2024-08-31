from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sectorSearchUSA.html')

@app.route('/sectorAnalyzeCA')
def sectorCAHomepage():
    return render_template('sectorSearchCA.html')

@app.route('/sectorAnalyzeUSA')
def sectorUSAHomepage():
    return render_template('sectorSearchUSA.html')

@app.route('/getInfoNYSE/<sector>', methods=['GET'])
def get_infoNyse(sector):
    data_dict = {}
    sendBackList = []
    with open('./static/nyse.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key, value in data_dict.items():
        if value == sector:
            sendBackList.append(key)
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)

@app.route('/getInfoNASDAQ/<sector>', methods=['GET'])
def get_infoNasdaq(sector):
    data_dict = {}
    sendBackList = []
    with open('./static/nasdaq.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key, value in data_dict.items():
        if value == sector:
            sendBackList.append(key)
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)

@app.route('/getInfoCse/<sector>', methods=['GET'])
def get_infoCse(sector):
    data_dict = {}
    sendBackList = []
    with open('./static/cse.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key, value in data_dict.items():
        if value == sector:
            sendBackList.append(key)
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)



@app.route('/getInfoTsx/<sector>', methods=['GET'])
def get_infoTsx(sector):
    data_dict = {}
    sendBackList = []
    with open('./static/cse.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key, value in data_dict.items():
        if value == sector:
            sendBackList.append(key)
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)


@app.route('/getInfoTsxv/<sector>', methods=['GET'])
def get_infoTsxv(sector):
    data_dict = {}
    sendBackList = []
    with open('./static/cse.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key, value in data_dict.items():
        if value == sector:
            sendBackList.append(key)
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)