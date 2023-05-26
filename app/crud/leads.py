from typing import List

import requests
import json
import hashlib
import urllib.request
import urllib.parse

from app.schemas import LeadOut
from app.db.models import Leads


def collect_leads() -> List[LeadOut]:
    encode = hashlib.md5("Demo".encode('utf-8'))
    encoded_pass = encode.hexdigest()
    login_args = {'user_auth': {'user_name': 'Demo', 'password': encoded_pass}}
    crmUrl = 'https://suitecrmdemo.dtbc.eu/service/v4/rest.php'
    data = json.dumps(login_args)
    args = {'method': 'login', 'input_type': 'json',
            'response_type': 'json', 'rest_data': data}
    params = urllib.parse.urlencode(args).encode('utf-8')
    response = urllib.request.urlopen(crmUrl, params)
    data = json.load(response)
    session_id = data["id"]

    response = requests.post(crmUrl, data={
        'method': 'get_entry_list',
        'input_type': 'JSON',
        'response_type': 'JSON',
        'rest_data': f'{{"session": "{session_id}", "module_name": "Leads", "query": "", "order_by": "", "offset": 0, "select_fields": ["phone_work", "first_name", "last_name"], "link_name_to_fields_array": [], "max_results": 200, "deleted": 0}}'
    })

    leads = response.json()['entry_list']
    lead_list = []

    for lead in leads:
        phone_work = lead['name_value_list']['phone_work']['value']
        first_name = lead['name_value_list']['first_name']['value']
        last_name = lead['name_value_list']['last_name']['value']
        lead_dict = {"phone_work": phone_work, "first_name": first_name, "last_name": last_name}
        lead_obj = Leads(**lead_dict)
        lead_list.append(lead_obj)

    return lead_list
