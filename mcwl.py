# -*- coding: utf-8 -*-
import re
import json

permission = 2

usage = {
    'tag': '-------------------- \u00A7bMCWL 帮助文档 \u00A7r--------------------',
    'help': '''    添加玩家白名单 \u00A76> \u00A7r!!whitelist add [玩家名]
    删除玩家白名单 \u00A76> \u00A7r!!whitelist remove [玩家名]
    获取白名单列表 \u00A76> \u00A7r!!whitelist list
    重新加载白名单 \u00A76> \u00A7r!!whitelist reload''',
    'add': ' 用法 \u00A76> \u00A7r!!whitelist add [玩家名]',
    'remove': ' 用法 \u00A76> \u00A7r!!whitelist remove [玩家名]'
}
display = {
    'add': '\u00A7a已将 \u00A76{} \u00A7a加入白名单',
    'remove': '\u00A7a已将 \u00A76{} \u00A7a移出白名单',
    'list': '\u00A76白名单列表 > \u00A7r{}',
    'reload': '\u00A76已重新读取白名单',
    'permission': '\u00A7c权限不足'
}

def on_info(server, info):
    if info.is_player == 1:
        if info.content.startswith('!!whitelist') or info.content.startswith('!!wl'):
            args = info.content.split()
            if len(args) == 1:
                server.say(usage['tag'])
                for line in usage['help'].splitlines():
                    server.say(line)
                server.say(usage['tag'])
            elif args[1] == 'add':
                if len(args) == 2:
                    server.say(usage['tag'])
                    server.say(usage['add'])
                    server.say(usage['tag'])
                else:
                    if server.get_permission_level(info) >= permission:
                        server.execute('whitelist add {}'.format(args[2]))
                        server.say(display['add'].format(args[2]))
                    else:
                        server.say(display['permission'])
            elif args[1] == 'remove':
                if len(args) == 2:
                    server.say(usage['tag'])
                    server.say(usage['remove'])
                    server.say(usage['tag'])
                else:
                    if server.get_permission_level(info) >= permission:
                        server.execute('whitelist remove {}'.format(args[2]))
                        server.say(display['remove'].format(args[2]))
                    else:
                        server.say(display['permission'])
            elif args[1] == 'list':
                server.execute('whitelist list')
                players = json.load(open('./server/whitelist.json'))
                playernames = ''
                for player in players:
                    playernames = playernames + player['name'] + ', '
                playernames = playernames[:-2]
                server.say(display['list'].format(playernames))
            elif args[1] == 'reload':
                server.execute('whitelist reload')
                server.say(display['reload'])