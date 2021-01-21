# -*# -*- coding: utf-8 -*-
import multiprocessing
import time

wars = {
    "0": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "0",
        "id_channel": -546546446,
        "pack_name": "lobo",
        "channel_name": "lobos",
        "action": "start",
        "stopped": False,
        "time": 10
    },
    "1": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "1",
        "id_channel": -546546446,
        "pack_name": "Anime",
        "channel_name": "anime",
        "action": "start",
        "stopped": False,
        "time": 3
    },
    "2": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "2",
        "id_channel": -546546446,
        "pack_name": "ONE PIECE",
        "channel_name": "onepiece",
        "action": "start",
        "stopped": False,
        "time": 5
    },
    "3": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "3",
        "id_channel": -546546446,
        "pack_name": "dragonball",
        "channel_name": "dragon",
        "action": "start",
        "stopped": False,
        "time": 1
    }
}

wars_pojo = {
    "0": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "0",
        "id_channel": -546546446,
        "pack_name": "lobo",
        "channel_name": "lobos",
        "action": "start",
        "stopped": False,
        "time": 10
    },
    "1": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "1",
        "id_channel": -546546446,
        "pack_name": "Anime",
        "channel_name": "anime",
        "action": "start",
        "stopped": False,
        "time": 3
    },
    "2": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "2",
        "id_channel": -546546446,
        "pack_name": "ONE PIECE",
        "channel_name": "onepiece",
        "action": "start",
        "stopped": False,
        "time": 5
    },
    "3": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "3",
        "id_channel": -546546446,
        "pack_name": "dragonball",
        "channel_name": "dragon",
        "action": "start",
        "stopped": False,
        "time": 1
    },
    "4": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "0",
        "id_channel": -546546446,
        "pack_name": "lobo",
        "channel_name": "lobos",
        "action": "stop",
        "stopped": False,
        "time": 10
    },
    "5": {
        "cid": 113213,
        "mid": 23,
        "id_user": 2213123123,
        "id_pack": "0",
        "id_channel": -546546446,
        "pack_name": "lobo",
        "channel_name": "lobos",
        "action": "start",
        "stopped": True,
        "time": 4
    },
}

def war_process(cid, mid, id_user, id_pack, id_channel, pack_name, channel_name, action, stopped, wait_time):
    wait_time = wars[id_pack]["time"] 
    time_end = wait_time 
    stopped_war = wars[id_pack]["stopped"] 
    action_war = wars[id_pack]["action"] 
    
    if action == "stop" and stopped is False:
        time.sleep(5)
        print(f'Paramos guerra: {pack_name} del grupo {channel_name} {wars[id_pack]["time"]}')
        wars[id_pack]["stopped"] = True
        
        
    elif action == "start" and stopped is False:
        print(f'Procesamos guerra: {pack_name} del grupo {channel_name} {wait_time}')
        for x in range(wait_time):
            time_end = time_end -1
            wars[id_pack]["time"] = time_end
            # print("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(f"{pack_name}")
            # print(wars)
            # print("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1)
            if time_end == 0:
                print(f'Terminamos guerra: {pack_name} del grupo {channel_name} {wars[id_pack]["time"]}')
                
    elif action == "stop" and stopped:
        print(f'Reanudamos guerra: {pack_name} del grupo {channel_name} {wait_time}')
        for x in range(wait_time):
            time_end = time_end -1
            wars[id_pack]["time"] = time_end
            time.sleep(1)
            if time_end == 0:
                print(f'Terminamos guerra: {pack_name} del grupo {channel_name} {wars[id_pack]["time"]}')
    
    elif action == "stop" and stopped is False:
        pass
        

def war_management(cid, mid, id_user, id_pack, id_channel, pack_name, channel_name, action, stopped, wait_time):
    processes = []
    # war_args = kwargs
    # p = Pool(1)
    p = multiprocessing.Process(target=war_process, args=[cid, mid, id_user, id_pack, id_channel, pack_name, channel_name, action, stopped, wait_time])
    processes.append(p)
    print(processes)
    
    p.start()
    
                      
for war in wars_pojo:
    cid=wars_pojo[war]["cid"]
    mid=wars_pojo[war]["mid"]
    id_user=wars_pojo[war]["id_user"]
    id_pack=wars_pojo[war]["id_pack"]
    id_channel=wars_pojo[war]["id_channel"]
    pack_name=wars_pojo[war]["pack_name"]
    channel_name=wars_pojo[war]["channel_name"]
    action=wars_pojo[war]["action"]
    stopped=wars_pojo[war]["stopped"]
    wait_time=wars_pojo[war]["time"]
    war_management(cid, mid, id_user, id_pack, id_channel, pack_name, channel_name, action, stopped, wait_time)

