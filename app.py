from flask import Flask, request, jsonify
from query_website import get_result

app = Flask(__name__)

@app.route('/', methods=["POST"])
def sunatAPI():
    dataObject = request.get_json(force=True) 

    typeOfVoucher = {
                    'RECEIPT BY ELECTRONIC FEES': '01',
                    'ELECTRONIC BILL': '03',
                    'ELECTRONIC TICKET': 'TCF'
                    }
    typeOfDocument = {
                    'NO DOCUMENT': '-',
                    'DOC. NATIONAL IDENTITY': '1',
                    'REG. SOLE OF TAXPAYERS': '6'
                    }
    voucher_type = dataObject['voucher_type']
    dataObject['voucher_type'] = typeOfVoucher[voucher_type]
    document_type = dataObject['document_type']
    dataObject['document_type'] = typeOfDocument[document_type]
    
    result = get_result(dataObject)

    return jsonify(result)
