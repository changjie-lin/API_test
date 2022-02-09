"""
Title:  HTTP module API
Author: changjie.lin
Date:   March 31, 2021    
"""

from flask import Flask, request, jsonify
app = Flask(__name__)

# The response JSON
CODES = {
    "SUCCESS":    { "error_code": 0, "error_message": "success" },
    "SYSTEM_ERR": { "error_code": 11, "error_message": "system error" },
    "PARAMS_ERR": { "error_code": 21, "error_message": "empty or wrong params" }
}

@app.route("/shopee/test", methods = ['GET', 'POST'])
def query_example():
    resp = Response()

    if 'GET' != request.method:
        errors = resp.get_error(CODES["SYSTEM_ERR"])
        errors.set_ref("System Error")
        return resp.get_json()

    (is_params_exist, ref_msg) = check_params_exist(request.args)
    if not is_params_exist:
        errors = resp.get_error(CODES["PARAMS_ERR"])
        errors.set_ref(ref_msg)
        return resp.get_json()

    value_a = request.args.get('a')
    value_b = request.args.get('b')
    (is_params_legal, ref_msg) = check_params_legal(value_a, value_b)
    if not is_params_legal:
        errors = resp.get_error(CODES["PARAMS_ERR"])
        errors.set_ref(ref_msg)
        return resp.get_json()

    return resp.get_json()


def check_params_exist(params):
    ref_msg = "Parameters Missing "
    is_exist = True

    if 'a' not in params:
        ref_msg += 'a'
        is_exist = False

    if 'b' not in params:
        ref_msg += 'b'
        is_exist = False

    return is_exist, ref_msg

def check_params_legal(param_int, param_str):
    ref_msg = "Parameter Illegal "
    is_legal = True

    if not is_int(param_int):
        ref_msg += "Parameter \'a\' needs to be int type"
        is_legal = False
    
    if is_empty(param_int):
        ref_msg += "Parameter \'a\' should not be empty"
        is_legal = False

    if is_empty(param_str):
        ref_msg += "Parameter \'b\' should not be empty"
        is_legal = False

    return is_legal, ref_msg

def is_int(param):
    try:
        int(param)
    except ValueError:
        return False

    return True

def is_empty(param):
    return not bool(param)


class Response:
    def __init__(self):
        self.error_code = 0
        self.error_message = "success"
        self.reference = "success"

    def get_error(self, code):
        self.error_code = code["error_code"]
        self.error_message = code["error_message"]
        return self

    def set_ref(self, ref):
        self.reference = ref

    def get_json(self):
        return jsonify({ 
            "error_code": self.error_code,
            "error_message": self.error_message,
            "reference": self.reference })

if __name__ == "__main__":
    app.run(host="entrytask")