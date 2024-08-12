from libs import *
from requests.exceptions import JSONDecodeError

class MyRequest:
    def __init__(self, authorization:str, errors_handler:bool, request_attempts:int):
        self.__errors_handler = errors_handler
        self.__request_attempts = request_attempts
        self.__headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if authorization != None:
            self.__headers["Authorization"] = authorization

    def __errors(func):
        """Use in classes only for methods. A parameter '_errors_handler' (type bool) in your class
        control the state of this decorator. If _errors_handler == False -> return func
        with no errors handling."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if args[0].__errors_handler == False:
                return data
            while "error" in data:
                time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                match data["error"]["code"]:
                    case 485:
                        logging.warning(f" {time_now} | {args} | {data["error"]}")
                        return data
                    case 490:
                        logging.warning(f" {time_now} | {args} | {data["error"]}")
                        return data
                    case 499:
                        logging.warning(f" {time_now} | {args} | {data["error"]}")
                        msg_list = data["error"]["message"].split()
                        cooldown = float(msg_list[msg_list.index("cooldown:") + 1])
                        time.sleep(cooldown)
                    case _:
                        logging.error(f" {time_now} | {args} | {data["error"]}")
                        exit(data["error"]["code"])
                data = func(*args, **kwargs)
            else:
                time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                logging.info(f" {time_now} | {args}")
            return data
        return wrapper

    def __json_decoder(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            counter = args[0].__request_attempts
            if counter <= 0:
                counter = 1
            while counter > 0:
                response = func(*args, **kwargs)
                try:
                    return response.json()
                except JSONDecodeError:
                    counter -= 1
                    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                    logging.warning(f" {time_now} | {args} | JSONDecodeError | {counter} attempts left")
                    if counter == 0:
                        print(response.text)
                        raise
                    time.sleep(10)
        return wrapper
    
    @__errors
    @__json_decoder
    def _post(self, url:str, data:dict=dict()):
        return requests.post(url, headers=self.__headers, data=json.dumps(data), allow_redirects=True)

    @__errors
    @__json_decoder
    def _get(self, url:str, data:dict=dict()):
        for key, value in data.items():
            if value != None:
                if "?" not in url:
                    url += f"?{key}={value}"
                else:
                    url += f"&{key}={value}"
        return requests.get(url, headers=self.__headers)
