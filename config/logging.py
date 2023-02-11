import json_log_formatter
import hashlib
from datetime import datetime
from cryptography.fernet import Fernet
import random
import json


from uuid import uuid1
from b64uuid import B64UUID



class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        if extra.get('request',0):
            _request = extra['request']
            extra['url'] = _request.__str__().split("'")[-2]
            extra['method'] = _request.method

            if not extra['url'].replace('/api/board/', ''):
                pass
            else:
                extra['board_id'] = int(extra['url'].replace('/api/board/', ''))
            
            if _request.user:
                extra['user_id'] = hashlib.sha256(f"{_request.user.id}".encode('ascii')).hexdigest()
            else:
                extra['user_id'] = None

        # extra['name'] = record.__dict__['name']
        # extra['inDate'] = datetime.fromtimestamp(record.__dict__['created']).strftime('%Y-%m-%dT%X.%f')[:-3]+'Z'
        extra['inDate'] = datetime.fromtimestamp(record.__dict__['created']).strftime('%Y%m%d%H%M%S')
        extra['detail'] = {'message': message, 'levelname':record.__dict__['levelname']}
        extra.pop('request', None)
        # return extra
        
        # full log data encrypt
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypt_str = fernet.encrypt(f"{extra}".encode('ascii'))
        
        # compress log data
        extra['user_id'] = B64UUID(extra['user_id']).string
        
        method = {'GET': 1, 'POST': 2, 'PUT': 3, 'PATCH': 4, 'DELETE': 5}
        extra['method'] = method[extra['method']]
        
        # record_id = random.randrange(10000000000000000000000000000000000000000000000000000000000000, 99999999999999999999999999999999999999999999999999999999999999)
        record_id = uuid1().hex
        short_id = B64UUID(record_id).string
        
        answer_string = {'recordId': short_id, 'logtimestamp': datetime.now().strftime('%Y%m%d%H%M%S'), 'data': encrypt_str}
        
        return answer_string