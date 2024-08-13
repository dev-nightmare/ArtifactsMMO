from .libs import *
from .utils import MyRequest
from .enums import Sort, ContentType, Type, CraftSkill, Skill, Skin, Slot


BASE_URL = "https://api.artifactsmmo.com"


class MyCharacter(MyRequest):
    def __init__(self, token:str, name:str, cooldown_handler:bool=True, errors_handler:bool=True, request_attempts:int=3):
        super().__init__(f"Bearer {token}", errors_handler, request_attempts)
        self.name:str = name
        self.__cooldown_handler:bool = cooldown_handler

    def __repr__(self):
        return f"{MyCharacter.__name__}({self.name})"

    def __cooldown(func):

        """Use in classes only for methods. A parameter '_cooldown_handler' (type bool) in your class
        control the state of this decorator. If _cooldown_handler == False -> return func
        with no cooldown handling."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if args[0].__cooldown_handler == False:
                return data
            if "error" not in data:
                cooldown = data["data"]["cooldown"]["total_seconds"]
                time.sleep(cooldown)
            return data
        return wrapper

    @__cooldown
    def move(self, x:int, y:int) -> json:

        """Moves a character on the map using the map's X and Y position.
        https://api.artifactsmmo.com/docs/#/operations/action_move_my__name__action_move_post"""

        url = f"{BASE_URL}/my/{self.name}/action/move"
        post_data = {
            "x": x,
            "y": y
        }
        return self._post(url, post_data)

    @__cooldown
    def equip(self, code:str, slot:Slot) -> json:

        """Equip an item on your character.
        https://api.artifactsmmo.com/docs/#/operations/action_equip_item_my__name__action_equip_post"""

        url = f"{BASE_URL}/my/{self.name}/action/equip"
        post_data = {
            "code": code,
            "slot": slot.value
        }
        return self._post(url, post_data)

    @__cooldown
    def unequip(self, slot:Slot) -> json:

        """Unequip an item on your character.
        https://api.artifactsmmo.com/docs/#/operations/action_unequip_item_my__name__action_unequip_post"""

        url = f"{BASE_URL}/my/{self.name}/action/unequip"
        post_data = {
            "slot": slot.value
        }
        return self._post(url, post_data)

    @__cooldown
    def fight(self) -> json:

        """Start a fight against a monster on the character's map.
        https://api.artifactsmmo.com/docs/#/operations/action_fight_my__name__action_fight_post"""

        url = f"{BASE_URL}/my/{self.name}/action/fight"
        return self._post(url)

    @__cooldown
    def gather(self) -> json:

        """Harvest a resource on the character's map.
        https://api.artifactsmmo.com/docs/#/operations/action_gathering_my__name__action_gathering_post"""

        url = f"{BASE_URL}/my/{self.name}/action/gathering"
        return self._post(url)

    @__cooldown
    def craft(self, code:str, quantity:int=1) -> json:

        """Crafting an item. The character must be on a map with a workshop.
        https://api.artifactsmmo.com/docs/#/operations/action_crafting_my__name__action_crafting_post"""

        url = f"{BASE_URL}/my/{self.name}/action/crafting"
        post_data = {
            "code": code,
            "quantity": quantity
        }
        return self._post(url, post_data)

    @__cooldown
    def deposit_bank(self, code:str, quantity:int) -> json:

        """Deposit an item in a bank on the character's map.
        https://api.artifactsmmo.com/docs/#/operations/action_deposit_bank_my__name__action_bank_deposit_post"""

        url = f"{BASE_URL}/my/{self.name}/action/bank/deposit"
        post_data = {
            "code": code,
            "quantity": quantity
        }
        return self._post(url, post_data)

    @__cooldown
    def deposit_bank_gold(self, quantity:int) -> json:

        """Deposit golds in a bank on the character's map.
        https://api.artifactsmmo.com/docs/#/operations/action_deposit_bank_gold_my__name__action_bank_deposit_gold_post"""

        url = f"{BASE_URL}/my/{self.name}/action/bank/deposit/gold"
        post_data = {
            "quantity": quantity
        }
        return self._post(url, post_data)

    @__cooldown
    def recycle(self, code:str, quantity:int=1) -> json:

        """Recyling an item. The character must be on a map with a workshop
        (only for equipments and weapons).
        https://api.artifactsmmo.com/docs/#/operations/action_recycling_my__name__action_recycling_post"""

        url = f"{BASE_URL}/my/{self.name}/action/recycling"
        post_data = {
            "code": code,
            "quantity": quantity
        }
        return self._post(url, post_data)

    @__cooldown
    def withdraw_bank(self, code:str, quantity:int) -> json:

        """Take an item from your bank and put it in the character's inventory.
        https://api.artifactsmmo.com/docs/#/operations/action_withdraw_bank_my__name__action_bank_withdraw_post"""

        url = f"{BASE_URL}/my/{self.name}/action/bank/withdraw"
        post_data = {
            "code": code,
            "quantity": quantity
        }
        return self._post(url, post_data)

    @__cooldown
    def withdraw_bank_gold(self, quantity:int) -> json:

        """Withdraw gold from your bank.
        https://api.artifactsmmo.com/docs/#/operations/action_withdraw_bank_gold_my__name__action_bank_withdraw_gold_post"""

        url = f"{BASE_URL}/my/{self.name}/action/bank/withdraw/gold"
        post_data = {
            "quantity": quantity
        }
        return self._post(url, post_data)

    @__cooldown
    def buy_ge_item(self, code:str, quantity:int, price:int) -> json:

        """Buy an item at the Grand Exchange on the character's map.
        https://api.artifactsmmo.com/docs/#/operations/action_ge_buy_item_my__name__action_ge_buy_post"""

        url = f"{BASE_URL}/my/{self.name}/action/ge/buy"
        post_data = {
            "code": code,
            "quantity": quantity,
            "price": price
        }
        return self._post(url, post_data)

    @__cooldown
    def sell_ge_item(self, code:str, quantity:int, price:int) -> json:

        """Sell an item at the Grand Exchange on the character's map.
        https://api.artifactsmmo.com/docs/#/operations/action_ge_sell_item_my__name__action_ge_sell_post"""

        url = f"{BASE_URL}/my/{self.name}/action/ge/sell"
        post_data = {
            "code": code,
            "quantity": quantity,
            "price": price
        }
        return self._post(url, post_data)

    @__cooldown
    def accept_new_task(self) -> json:

        """Accepting a new task.
        https://api.artifactsmmo.com/docs/#/operations/action_accept_new_task_my__name__action_task_new_post"""

        url = f"{BASE_URL}/my/{self.name}/action/task/new"
        return self._post(url)

    @__cooldown
    def complete_task(self) -> json:

        """Complete a task.
        https://api.artifactsmmo.com/docs/#/operations/action_complete_task_my__name__action_task_complete_post"""

        url = f"{BASE_URL}/my/{self.name}/action/task/complete"
        return self._post(url)

    @__cooldown 
    def exchange_task(self) -> json:

        """Exchange 3 tasks coins for a random reward. Rewards are exclusive
        resources for crafting items.
        https://api.artifactsmmo.com/docs/#/operations/action_task_exchange_my__name__action_task_exchange_post"""

        url = f"{BASE_URL}/my/{self.name}/action/task/exchange"
        return self._post(url)

    @__cooldown
    def delete_item(self, code:str, quantity:int) -> json:

        """Delete an item from your character's inventory.
        https://api.artifactsmmo.com/docs/#/operations/action_delete_item_my__name__action_delete_post"""

        url = f"{BASE_URL}/my/{self.name}/action/delete"
        post_data = {
            "code": code,
            "quantity": quantity
        }
        return self._post(url, post_data)


class MyAccount(MyRequest):
    def __init__(self, token:str, errors_handler:bool=True, request_attempts:int=3):
        super().__init__(f"Bearer {token}", errors_handler, request_attempts)

    def __repr__(self):
        return f"{MyAccount.__name__}()"

    def get_all_characters_logs(self, page:int=None, size:int=None) -> json:

        """History of the last 100 actions of all your characters.
        https://api.artifactsmmo.com/docs/#/operations/get_all_characters_logs_my_logs_get"""

        url = f"{BASE_URL}/my/logs"
        get_data = {
            "page": page,
            "size": size
        }   
        return self._get(url, get_data)

    def get_my_characters(self) -> json:

        """List of your characters.
        https://api.artifactsmmo.com/docs/#/operations/get_my_characters_my_characters_get"""

        url = f"{BASE_URL}/my/characters"
        return self._get(url)

    def get_bank_items(self, item_code:str=None, page:int=None, size:int=None) -> json:

        """Fetch all items in your bank.
        https://api.artifactsmmo.com/docs/#/operations/get_bank_items_my_bank_items_get"""

        url = f"{BASE_URL}/my/bank/items"
        get_data = {
            "item_code": item_code,
            "page": page,
            "size": size
        }
        return self._get(url, get_data)

    def get_bank_golds(self) -> json:

        """Fetch golds in your bank.
        https://api.artifactsmmo.com/docs/#/operations/get_bank_golds_my_bank_gold_get"""

        url = f"{BASE_URL}/my/bank/gold"
        return self._get(url)

    def change_password(self, password:str) -> json:

        """Change your account password. Changing the password reset the account token.
        https://api.artifactsmmo.com/docs/#/operations/change_password_my_change_password_post"""

        url = f"{BASE_URL}/my/change_password"
        post_data = {
            "password": password
        }
        return self._post(url, post_data)

    def create_character(self, name:str, skin:Skin) -> json:

        """Create new character on your account. You can create up to 5 characters.
        https://api.artifactsmmo.com/docs/#/operations/create_character_characters_create_post"""

        url = f"{BASE_URL}/characters/create"
        post_data = {
            "name": name,
            "skin": skin.value
        }
        return self._post(url, post_data)

    def delete_character(self, name:str) -> json:

        """Delete character on your account.
        https://api.artifactsmmo.com/docs/#/operations/delete_character_characters_delete_post"""

        url = f"{BASE_URL}/characters/delete"
        post_data = {
            "name": name
        }
        return self._post(url, post_data)


class Game(MyRequest):
    def __init__(self, errors_handler:bool=True, request_attempts:int=3):
        super().__init__(None, errors_handler, request_attempts)

    def __repr__(self):
        return f"{Game.__name__}()"

    def get_status(self) -> json:

        """Return the status of the game server.
        https://api.artifactsmmo.com/docs/#/operations/get_status__get"""

        url = f"{BASE_URL}/"
        return self._get(url)

    def get_all_characters(self, page:int=None, size:int=None, sort:Sort=Sort.DEFAULT) -> json:

        """Fetch characters details.
        https://api.artifactsmmo.com/docs/#/operations/get_all_characters_characters__get"""

        url = f"{BASE_URL}/characters/"
        get_data = {
            "page": page,
            "size": size,
            "sort": sort.value
        }
        return self._get(url, get_data)

    def get_character(self, name:str) -> json:

        """Retrieve the details of a character.
        https://api.artifactsmmo.com/docs/#/operations/get_character_characters__name__get"""

        url = f"{BASE_URL}/characters/{name}"
        return self._get(url)

    def get_all_maps(self, content_code:str=None, content_type:ContentType=ContentType.DEFAULT,
                     page:int=None, size:int=None) -> json:

        """Fetch maps details.
        https://api.artifactsmmo.com/docs/#/operations/get_all_maps_maps__get"""

        url = f"{BASE_URL}/maps/"
        get_data = {
            "content_code": content_code,
            "content_type": content_type.value,
            "page": page,
            "size": size
        }
        return self._get(url, get_data)

    def get_map(self, x:int, y:int) -> json:

        """Retrieve the details of a map.
        https://api.artifactsmmo.com/docs/#/operations/get_map_maps__x___y__get"""

        url = f"{BASE_URL}/maps/{x}/{y}"
        return self._get(url)

    def get_all_items(self, craft_material:str=None, craft_skill:CraftSkill=CraftSkill.DEFAULT, max_level:int=None,
                      min_level:int=None, name:str=None, page:int=None, size:int=None, _type:Type=Type.DEFAULT) -> json:

        """Fetch items details.
        https://api.artifactsmmo.com/docs/#/operations/get_all_items_items__get"""

        url = f"{BASE_URL}/items/"
        get_data = {
            "craft_material": craft_material,
            "craft_skill": craft_skill.value,
            "max_level": max_level,
            "min_level": min_level,
            "name": name,
            "page": page,
            "size": size,
            "type": _type.value
        }
        return self._get(url, get_data)

    def get_item(self, code:str) -> json:

        """Retrieve the details of a item.
        https://api.artifactsmmo.com/docs/#/operations/get_item_items__code__get"""

        url = f"{BASE_URL}/items/{code}"
        return self._get(url)

    def get_all_monsters(self, drop:str=None, max_level:int=None, min_level:int=None,
                         page:int=None, size:int=None) -> json:

        """Fetch monsters details.
        https://api.artifactsmmo.com/docs/#/operations/get_all_monsters_monsters__get"""

        url = f"{BASE_URL}/monsters/"
        get_data = {
            "drop": drop,
            "max_level": max_level,
            "min_level": min_level,
            "page": page,
            "size": size
        }
        return self._get(url, get_data)

    def get_monster(self, code:str) -> json:

        """Retrieve the details of a monster.
        https://api.artifactsmmo.com/docs/#/operations/get_monster_monsters__code__get"""

        url = f"{BASE_URL}/monsters/{code}"
        return self._get(url)

    def get_all_resources(self, drop:str=None, max_level:int=None, min_level:int=None,
                          page:int=None, size:int=None, skill:Skill=Skill.DEFAULT) -> json:

        """Fetch resources details.
        https://api.artifactsmmo.com/docs/#/operations/get_all_resources_resources__get"""

        url = f"{BASE_URL}/resources/"
        get_data = {
            "drop": drop,
            "max_level": max_level,
            "min_level": min_level,
            "page": page,
            "size": size,
            "skill": skill.value
        }
        return self._get(url, get_data)

    def get_resource(self, code:str) -> json:

        """Retrieve the details of a resource.
        https://api.artifactsmmo.com/docs/#/operations/get_resource_resources__code__get"""

        url = f"{BASE_URL}/resources/{code}"
        return self._get(url)

    def get_all_events(self, page:int=None, size:int=None) -> json:

        """Fetch events details.
        https://api.artifactsmmo.com/docs/#/operations/get_all_events_events__get"""

        url = f"{BASE_URL}/events/"
        get_data = {
            "page": page,
            "size": size
        }
        return self._get(url, get_data)

    def get_all_ge_items(self, page:int=None, size:int=None) -> json:

        """Fetch Grand Exchange items details.
        https://api.artifactsmmo.com/docs/#/operations/get_all_ge_items_ge__get"""

        url = f"{BASE_URL}/ge/"
        get_data = {
            "page": page,
            "size": size
        }
        return self._get(url, get_data)

    def get_ge_item(self, code:str) -> json:

        """Retrieve the details of a Grand Exchange item.
        https://api.artifactsmmo.com/docs/#/operations/get_ge_item_ge__code__get"""

        url = f"{BASE_URL}/ge/{code}"
        return self._get(url)

    def create_account(self, username:str, password:str, email:str) -> json:

        """Create an account.
        https://api.artifactsmmo.com/docs/#/operations/create_account_accounts_create_post"""

        url = f"{BASE_URL}/accounts/create"
        post_data = {
            "username": username,
            "password": password,
            "email": email
        }
        return self._post(url, post_data)


class Client:

    """Simple interface for combining classes: 'MyCharacter', 'MyAccount', 'Game'"""

    def __init__(self, token:str=None, cooldown_handler:bool=True, errors_handler:bool=True, request_attempts:int=3):
        self.characters = []
        self.account = None
        self.game = None
        if token != None:
            self.account = MyAccount(token, errors_handler, request_attempts)
            data = self.account.get_my_characters()
            for character in data["data"]:
                self.characters.append(MyCharacter(token, character["name"], cooldown_handler, errors_handler, request_attempts))
        self.game = Game(errors_handler, request_attempts)

    @staticmethod
    def generate_token(username:str, password:str, errors_handler:bool=True, request_attempts:int=3) -> json:

        """Use your account as HTTPBasic Auth to generate your token to use the API.
        You can also generate your token directly on the website.
        https://api.artifactsmmo.com/docs/#/operations/generate_token_token__post"""

        # I hate this function!!!
        url = f"{BASE_URL}/token/"
        string_bytes = f"{username}:{password}".encode("ascii")
        basic_token = base64.b64encode(string_bytes).decode("ascii")
        req = MyRequest(f"Basic {basic_token}", errors_handler, request_attempts)
        return req._post(url)