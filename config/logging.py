import json_log_formatter
import hashlib
from datetime import datetime
from cryptography.fernet import Fernet

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
        extra['inDate'] = datetime.fromtimestamp(record.__dict__['created']).strftime('%Y-%m-%dT%X.%f')[:-3]+'Z'
        extra['detail'] = {'message': message, 'levelname':record.__dict__['levelname']}
        extra.pop('request', None)
        # return extra
        
        # full log data encrypt
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypt_str = fernet.encrypt(f"{extra}".encode('ascii'))
        return encrypt_str