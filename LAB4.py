from fastapi import FastAPI
from datetime import datetime
import random
app = FastAPI()


class Player:
#1
    def __init__(self,id,name,hp):
        self._id=id
        self._name=name.strip().title()
        self._hp=max(0,hp)
#7.1
    def handle_event(self, event):
        if event._type == "ATTACK":
            self._hp -= event._data["damage"]
        elif event._type == "HEAL":
            self._hp += event._data["heal"]
        elif event._type == "LOOT":
            self._inventory.add_item(event._data["item"])
    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}',hp={self._hp})"
    def __del__(self):
        print(f"Player {self._name} удален")
#2
    @classmethod
    def from_string(cls, data: str):
        pr = data.split(',')
        if len(pr) != 3:
            raise ValueError
        player_id = int(pr[0].strip())
        player_name = pr[1].strip()
        player_hp = int(pr[2].strip())
        return cls(player_id,player_name,player_hp)
@app.get("/1")
def result_1():
    p = Player(21,"Azamat",67)
    return {
        "str_result": str(p),
        "player_info":{"id":p._id,"name":p._name,"hp":p._hp}
    }
@app.get("/2")
def result_2():
    p = Player.from_string("1,beka,100")
    return {
        "str_result": str(p),
        "player_info":{"id":p._id,"name":p._name,"hp":p._hp}
    }
#3
class Item:
    def __init__(self,id,name,power):
        self._id = int(id)
        self._name = name.strip().title()
        self._power = int(power)
    def __str__(self):
        return f"Item(id={self._id},name={self._name},power={self._power})"
    def __eq__(self,other):
        if isinstance(other,Item):
            return self._name == other._id
        return False
    def __hash__(self):
        return hash(self._id)
@app.get("/3")
def show_task3():
    i = Item(1, " Sword ", 50)
    return {
        "str_result": str(i),
        "player_data": {"id": i._id, "name": i._name, "power": i._power}
    }

#4
class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self,item):
        if item not in self._items:
            self._items.append(item)
            print(f"{item._name} added to inventory")
        else:
            print(f"{item._name} duplicate")
    def remove_item(self,item_id):
        for item in self._items:
            if item._id == item_id:
                self._items.remove(item)
                print(f"ID {item_id} removed fro inventory")
                return
    def get_items(self):
        return self._items
    def unique_items(self):
        return set(self._items)
    def to_dict(self):
        return {item._id: {"name": item._name,"power": item._power,}for item in self._items}
#5
    def strong(self,min_power: int):
        is_strong = lambda item: item._power >= min_power
        return [item for item in self._items if is_strong(item)]
@app.get("/4")
def show_task4():
    bag = Inventory()
    sword = Item(1, "Sword", 50)
    axe = Item(2, "Axe", 80)
    bag.add_item(sword)
    bag.add_item(axe)
    bag.add_item(sword)
    return {
        "message": "4-ші тапсырма (Инвентарь)",
        "inventory_dict": bag.to_dict()
    }
@app.get("/5")
def show_task5(min_power: int=60):
    bag = Inventory()
    sword = Item(1, "Sword", 50)
    axe = Item(2, "Battle Axe", 80)
    magic_wand = Item(3, "Magic Wand", 120)
    bag.add_item(sword)
    bag.add_item(axe)
    bag.add_item(sword)
    strong_items_list= bag.strong(min_power)
    result = [{"id": i._id, "name": i._name, "power": i._power} for i in strong_items_list]
    return {
        "message": "5-ші тапсырма (Мықты қарулар)",
        "min_power_filter": min_power,
        "strong_items": result
    }
#6
class Event:
    def __init__(self,type,data):
        self._type = type
        self._data = data
        self._timestamp = datetime.now()
    def __str__(self):
        return f"EVENT(type='{self._type}', data='{self._data}', timestamp='{self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}')"
@app.get("/6")
def result_6():
    e = Event("ATTACK",{"damage":20})
    return {
        "str result":str(e)
    }
#7
class Warrior(Player):
    def handle_event(self, event):
        if event._type == "ATTACK":
            event._data["damage"] = int(event._data["damage"] * 0.9)
        super().handle_event(event)
class Mage(Player):
    def handle_event(self, event):
        if event._type == "LOOT":
            event._data["item"]._power = int(event._data["item"]._power*1.1)
        super().handle_event(event)
@app.get("/7")
def result():
    w = Warrior(1,"Archi",100)
    attack_eze = Event("ATTACK",{"damage":30})
    w.handle_event(attack_eze)
    result = {"id":w._id,"name":w._name,"hp":w._hp}
    return {
        "result str":str(result)
    }
#8
class Logger:
    def log(self,event,player,filename):
        log_text = f"{event._timestamp.strftime('%Y-%m-%d %H:%M:%S')};{player._id};{event._type};{event._data}\n"
        with open(filename, "a", encoding='utf-8') as f:
            f.write(log_text)
#9
    def read_logs(self,filename):
        events_list = []
        with open(filename, "r", encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(";")
                e = Event(parts[2],eval(parts[3]))
                events_list.append(e)
        return events_list
@app.get("/8")
def result_8():
    q = Warrior(2,"Aza",100)
    e = Event("ATTACK",{"damage":30})
    logger = Logger()
    logger.log(e,q,"game_logs.txt")
    return {"message": "8-ші тапсырма орындалды. Файлды тексер!"}
@app.get("/9")
def result_9():
    logger = Logger()
    events = logger.read_logs("game_logs.txt")
    result = [{"type":e._type,"data":e._data} for e in events]
    return {
        "logs":result
    }
#10
class IventIterator:
    def __init__(self,one_list):
        self._events = one_list
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._events):
            element = self._events[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration
#11
def damage_stream(events):
    for i in events:
        if i._type == "ATTACK":
            yield i._data["damage"]
@app.get("/10")
def result_10():
    adv = [
        Event("ATTACK",{"damage":40}),
        Event("HEAL",{"damage":40}),
        Event("LOOT",{"item":Item(1,"Sword",10)})
    ]
    my_iterator = EventIterator(adv)
    result = []
    for event in my_iterator:
        result.append({"type":{event._type},"data":{str(event._data)}})
    return {
        "iterated_events":result
    }
@app.get("/11")
def show_task11():
    turli = [
        Event("ATTACK", {"damage": 50}),
        Event("HEAL", {"heal": 20}),
        Event("ATTACK", {"damage": 30}),
        Event("LOOT", {"item": Item(1, "Shield", 50)}),
        Event("ATTACK", {"damage": 15})
    ]
    damage_generator = damage_stream(turli)
    result = list(damage_generator)
    return {
        "message": "11-ші тапсырма сәтті орындалды!",
        "damage_values": result
    }
#12
def generate_events(players,items,n):
    all_events = []
    pick_type = lambda: random.choice(["ATTACK","HEAL","TOOL"])
    for i in players:
        for _ in range(n):
            t = pick_type()
            if t == "ATTACK":
                event_data = {"damage":random.randint(10,50)}
            elif t == "HEAL":
                event_data = {"heal":random.randint(10,50)}
            elif t == "TOOL":
                event_data = {"item":random.choice(items)}
            new_event = Event(t,event_data)
            all_events.append(new_event)
        return all-events
#13
def analyze_logs(events):
    total_damage = []
    sum_damage = sum([v._data["damage"] for v in events if v._type == "ATTACK"])
    events_count = {}
    for s in events:
        if s._type in events_count:
            events_count[s._type] += 1
        else:
            events_count[s._type] = 1
    most_common = max(events_count, key = events_count.get)
    player_damage = {}
    for l in events:
        if l._type == "ATTACK":
            player_id = l._data["player_id"]
            if player_id in player_damage:
                player_damage[player_id] += l._data["damage"]
            else:
                player_damage[player_id] = l._data[("damage")]
    top_player = max(player_damage, key = player_damage.get)
    return {
        "total_damage":sum_damage,
        "top_player":top_player,
        "most_common_event":most_common
    }
#14
decide_action = lambda hp, inventory: "HEAL" if hp < 30 else "LOOT" if len(inventory) == 0 else "ATTACK"

@app.get("/12")
def show_task12():
    test_players = [Player(1, "Nurdaulet"), Player(2, "Samgar")]
    test_items = [Item(1, "Sword", 50), Item(2, "Shield", 50), Item(3, "Potion", 0)]
    generated_events = generate_events(test_players, test_items, 3)
    result = [{"type": e._type, "data": str(e._data)} for e in generated_events]
    return {
        "message": "12-ші тапсырма сәтті орындалды!",
        "total_events_generated": len(generated_events),
        "events": result
    }
@app.get("/13")
def show_task13():
    test_events = [
        Event("ATTACK", {"damage": 20, "player_id": "Batyr"}),
        Event("HEAL", {"heal": 15, "player_id": "Batyr"}),
        Event("ATTACK", {"damage": 50, "player_id": "Arman"}),
        Event("ATTACK", {"damage": 10, "player_id": "Batyr"}),
        Event("LOOT", {"item": "Sword", "player_id": "Arman"}),
        Event("HEAL", {"heal": 25, "player_id": "Arman"}),
        Event("ATTACK", {"damage": 100, "player_id": "Arman"})
    ]
    analytics_result = analyze_logs(test_events)
    return {
        "message": "13-ші тапсырма сәтті орындалды!",
        "dashboard": analytics_result
    }
@app.get("/14")
def show_task14():
    decide_action = lambda hp, inventory: "HEAL" if hp < 30 else "LOOT" if len(inventory) == 0 else "ATTACK"
    action1 = decide_action(20, ["Sword", "Shield"])
    action2 = decide_action(80, [])
    action3 = decide_action(100, ["Axe"])
    return {
        "message": "14-ші тапсырма сәтті орындалды!",
        "AI_decisions": [
            {"hp": 20, "inventory": ["Sword", "Shield"], "decision": action1},
            {"hp": 80, "inventory": [], "decision": action2},
            {"hp": 100, "inventory": ["Axe"], "decision": action3}
        ]
    }