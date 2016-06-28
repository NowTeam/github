import telebot
import urllib
from telebot import types
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot('YOUR TOKEN')

@bot.message_handler(commands=['start', 'help'])
def m(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Inline Mode', switch_inline_query='taylor-team'))
    bot.send_message(m.chat.id, 'Hi Welcome Github bot\ncommands : \n/git [username]\n\ncreated By Taylor Team \ndeveloper : @negative_officiall', reply_markup=markup)
    print 'bot send help command'

@bot.message_handler(regexp='^(/git) (.*)')
def gif(m):
    text = m.text.split()[1]
    r = requests.get('https://api.github.com/users/{}'.format(text))
    json_data = r.json()
    if 'id' in json_data:
        url_html = json_data['html_url']
        typee = json_data['type']
        name = json_data['name']
        company = json_data['company']
        blog = json_data['blog']
        location = json_data['location']
        bio = json_data['bio']
        public_repos = json_data['public_repos']
        followers = json_data['followers']
        following = json_data['following']
        avatar_url = json_data['avatar_url']
        urllib.urlretrieve("{}".format(avatar_url), "git.png")
        bot.send_sticker(m.chat.id, open('git.png'))
        bot.send_message(m.chat.id, 'Name : <b>{}</b>\nType : <b>{}</b>\nCompany : <b>{}</b>\nblog : <code>{}</code>\nlocation : <b>{}</b>\nbio : <i>{}</i>\n\nUrl : <code>{}</code>\nfollowers : <code>{}</code>\nfollowing : <code>{}</code>\nRepos : <code>{}</code>\n\xE2\x97\xBC \xE2\x97\xBB \xE2\x97\xBC \xE2\x97\xBB \xE2\x97\xBC \xE2\x97\xBB \xE2\x97\xBC \n@taylor_team'.format(name,typee,company,blog,location,bio,url_html,followers,following,public_repos), parse_mode='HTML')
        print 'bot send git command'
    if 'message' in json_data:
        bot.send_message(m.chat.id, 'Error \n/git [username]')
        return

@bot.inline_handler(lambda query: len(query.query.split()) == 1)
def qq(q):
    text = q.query
    r = requests.get('https://api.github.com/users/{}'.format(text))
    json_data = r.json()
    if 'avatar_url' in json_data:
        url_html = json_data['html_url']
        typee = json_data['type']
        name = json_data['name']
        company = json_data['company']
        blog = json_data['blog']
        location = json_data['location']
        bio = json_data['bio']
        public_repos = json_data['public_repos']
        followers = json_data['followers']
        following = json_data['following']
        avatar_url = json_data['avatar_url']
        tmp = 'http://ericsteinborn.com/github-for-cats/img/ironcat.png'
        gitss = types.InlineQueryResultArticle('1', 'Git username\xE2\x9C\x8F\xEF\xB8\x8F', types.InputTextMessageContent('Name : <b>{}</b>\nUrl : <b>{}</b>\nBlog : <b>{}</b>\nLocation : <b>{}</b>\nBio : <i>{}</i>\n\nRepos : <code>{}</code>\nfollowers : <code>{}</code>\nfollowing : <code>{}</code>'.format(name,url_html,blog,location,bio,public_repos,followers,following), parse_mode="HTML"), thumb_url=tmp)
        avatarr = types.InlineQueryResultPhoto('2', '{}'.format(avatar_url), '{}'.format(avatar_url), description='avatar', caption='Name : {}\nUrl : {}\nBlog : {}\nLocation : {}\nBio : {}\n\nRepos : {}'.format(name,url_html,blog,location,bio,public_repos))
        bot.answer_inline_query(q.id, [gitss, avatarr], cache_time=1)

bot.polling(True)
# _____           _              _____
#|_   _|_ _ _   _| | ___  _ __  |_   _|__  __ _ _ __ ___
#  | |/ _` | | | | |/ _ \| '__|   | |/ _ \/ _` | '_ ` _ \
#  | | (_| | |_| | | (_) | |      | |  __/ (_| | | | | | |
#  |_|\__,_|\__, |_|\___/|_|      |_|\___|\__,_|_| |_| |_|
#           |___/
