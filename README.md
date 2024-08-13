# ArtifactsMMO

## Description

Full API client wrapper for the game ArtifactsMMO: https://artifactsmmo.com/

Simplifies sending requests and receiving responses from the game server. Handles cooldown and some errors, but you can turn off both of them. If you can't decode json, you can set the number of times to retry requests to the server with a time range of 10 seconds.

## Installation

Python 3.10+
```sh
cd <path to your project>
git clone https://github.com/dev-nightmare/ArtifactsMMO
pip install -r ArtifactsMMO\\requirements.txt
```

## Usage

### Modules, Classes and Methods

You will find more detailed information in the description of the methods.

```python
- enums.py
  - Sort            #Needs for method 'get_all_characters' in class 'Game'
  - ContentType     #Needs for method 'get_all_maps' in class 'Game'
  - Type            #Needs for method 'get_all_items' in class 'Game'
  - CraftSkill      #Needs for method 'get_all_items' in class 'Game'
  - Skill           #Needs for method 'get_all_resources' in class 'Game'
  - Skin            #Needs for method 'create_character' in class 'MyAccount'
  - Slot            #Needs for methods 'equip' and 'unequip' in class 'MyCharacter'

- api.py
  - Client # Simple interface for combining classes: MyCharacter, MyAccount, Game
    - static generate_token(username:str, password:str, errors_handler:bool=True, request_attempts:int=3) -> json

  - MyCharacter
    - python move(x:int, y:int) -> json
    - equip(code:str, slot:Slot) -> json
    - unequip(slot:Slot) -> json
    - fight() -> json
    - gather() -> json
    - craft(code:str, quantity:int=1) -> json
    - deposit_bank(code:str, quantity:int) -> json
    - deposit_bank_gold(quantity:int) -> json
    - recycle(code:str, quantity:int=1) -> json
    - withdraw_bank(code:str, quantity:int) -> json
    - withdraw_bank_gold(quantity:int) -> json
    - buy_ge_item(code:str, quantity:int, price:int) -> json
    - sell_ge_item(code:str, quantity:int, price:int) -> json
    - accept_new_task() -> json
    - complete_task() -> json
    - exchange_task() -> json
    - delete_item(code:str, quantity:int) -> json

  - MyAccount
    - get_my_characters() -> json
    - get_bank_items(item_code:str=None, page:int=None, size:int=None) -> json
    - get_bank_golds() -> json
    - change_password(password:str) -> json
    - create_character(name:str, skin:Skin) -> json
    - delete_character(name:str) -> json

  - Game
    - get_status() -> json
    - get_all_characters(page:int=None, size:int=None, sort:Sort=Sort.DEFAULT) -> json
    - get_character(name:str) -> json
    - get_all_maps(content_code:str=None, content_type:ContentType=ContentType.DEFAULT, page:int=None,
                   size:int=None) -> json
    - get_map(x:int, y:int) -> json
    - get_all_items(craft_material:str=None, craft_skill:CraftSkill=CraftSkill.DEFAULT, max_level:int=None,
                    min_level:int=None, name:str=None, page:int=None, size:int=None, _type:Type=Type.DEFAULT) -> json
    - get_item(code:str) -> json
    - get_all_monsters(drop:str=None, max_level:int=None, min_level:int=None, page:int=None, size:int=None) -> json
    - get_monster(code:str) -> json
    - get_all_resources(drop:str=None, max_level:int=None, min_level:int=None, page:int=None, size:int=None,
                        skill:Skill=Skill.DEFAULT) -> json
    - get_resource(code:str) -> json
    - get_all_events(page:int=None, size:int=None) -> json
    - get_all_ge_items(page:int=None, size:int=None) -> json
    - get_ge_item(code:str) -> json
    - create_account(self, username:str, password:str, email:str) -> json
```

### Example

```python
from ArtifactsMMO.api import Client

client = Client(TOKEN)
print(client.game.get_status())
print(client.characters[0].move(3, 5))
print(client.account.get_my_characters())
```

### Best practice

```python
from ArtifactsMMO.api import MyCharacter, MyAccount, Game, Client
from ArtifactsMMO.enums import *

import threading


def learn_resource_skill(game:Game, account:MyAccount, character:MyCharacter, skill:Skill):
    pass


def main():
    threads = []
    work = {
        "Prototype-0": [learn_resource_skill, Skill.WOODCUTTING],
        "Prototype-1": [learn_resource_skill, Skill.WOODCUTTING],
        "Prototype-2": [learn_resource_skill, Skill.WOODCUTTING],
        "Prototype-3": [learn_resource_skill, Skill.WOODCUTTING],
        "Prototype-4": [learn_resource_skill, Skill.WOODCUTTING]
    }

    client = Client("token")

    for index, character in enumerate(client.characters):
        t = threading.Thread(target=work[character.name][0], name=index, args=(client.game, client.account,
                             client.characters[index], *work[character.name][1:]))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
```
