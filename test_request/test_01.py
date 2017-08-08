import requests
import json
from base_settings import *

def run_zelig_req():

    test_input1 = get_file_contents_as_json('test_input_1a.json')
    test_input1['zsessionid'] = 'a'
    del test_input1['zusername'] #= None

    json_str = json.dumps(test_input1)

    print (test_input1)
    print (type(test_input1))

    r = requests.post(URL_ZELIG_APP,
                      data=dict(solaJSON=json_str))

    print (40 * '=')
    print (r.text)
    d = r.json()
    print (json.dumps(d, indent=4))
    print (r.status_code)

if __name__ == '__main__':
    run_zelig_req()
