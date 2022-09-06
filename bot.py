import config
import telebot
import requests


bot = telebot.TeleBot(config.bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(m):
	bot.reply_to(m, "Привет, я просто бот и вряд ли смогу научить тебя чему-то, поэтому не трать моё время.")

@bot.message_handler(func = lambda m: True)
def get_ip(m):
	if (m.from_user.username == config.admin):
		response_ips = requests.get("https://ipqualityscore.com/api/json/ip/"+config.ips_token+"/"+m.text+"?strictness=1&mobile=false")
		response_ipdata = requests.get("https://api.ipdata.co/"+m.text+"?api-key="+config.ipdata_token)
		'''bot.send_message(m.chat.id, "IPDATA:\n\nСтрана: "+str(response_ipdata.json()["country_name"])+" "+str(response_ipdata.json()["emoji_flag"])+"\nГород: "+str(response_ipdata.json()["city"])+"\nИндекс: "+str(response_ipdata.json()["postal"])+"\n\nASN:\nASN: "+str(response_ipdata.json()["asn"]["asn"])+"\nИмя: "+str(response_ipdata.json()["asn"]["name"])+"\nМаршрут: "+str(response_ipdata.json()["asn"]["route"])+"\nТип: "+str(response_ipdata.json()["asn"]["type"])+"\n\nАнонимность:\nTor: "+str(response_ipdata.json()["threat"]["is_tor"])+"\nПрокси: "+str(response_ipdata.json()["threat"]["is_proxy"])+"\nАнонимный: "+str(response_ipdata.json()["threat"]["is_anonymous"])+"\nAttacker: "+str(response_ipdata.json()["threat"]["is_known_attacker"])+"\nАбузер: "+str(response_ipdata.json()["threat"]["is_known_abuser"]))'''
		if (response_ips.json()["success"]):
			bot.send_message(m.chat.id, "IPDATA:\n\nСтрана: "+str(response_ipdata.json()["country_name"])+" "+str(response_ipdata.json()["emoji_flag"])+"\nГород: "+str(response_ipdata.json()["city"])+"\nИндекс: "+str(response_ipdata.json()["postal"])+"\n\nASN:\nASN: "+str(response_ipdata.json()["asn"]["asn"])+"\nИмя: "+str(response_ipdata.json()["asn"]["name"])+"\nМаршрут: "+str(response_ipdata.json()["asn"]["route"])+"\nТип: "+str(response_ipdata.json()["asn"]["type"])+"\n\nАнонимность:\nTor: "+str(response_ipdata.json()["threat"]["is_tor"])+"\nПрокси: "+str(response_ipdata.json()["threat"]["is_proxy"])+"\nАнонимный: "+str(response_ipdata.json()["threat"]["is_anonymous"])+"\nAttacker: "+str(response_ipdata.json()["threat"]["is_known_attacker"])+"\nАбузер: "+str(response_ipdata.json()["threat"]["is_known_abuser"])+"\n\n IPQUALITYSCORE\nFraud Score: "+str(response_ips.json()["fraud_score"])+'\n\n'+"Страна: "+response_ips.json()["country_code"]+'\n'+"Город: "+str(response_ips.json()["city"])+'\n'+"Регион: "+str(response_ips.json()["region"])+'\n\nASN:\n'+"Провайдер: "+str(response_ips.json()["ISP"])+'\n'+"Организация: "+str(response_ips.json()["organization"])+'\n'+"ASN: "+str(response_ips.json()["ASN"])+'\n\nАнонимность:\n'+"Мобильный: "+str(response_ips.json()["mobile"])+'\n'+"Прокси: "+str(response_ips.json()["proxy"])+'\n'+"VPN: "+str(response_ips.json()["vpn"])+'\n'+"Tor: "+str(response_ips.json()["tor"])+'\n'+"Активный VPN: "+str(response_ips.json()["active_vpn"])+'\n'+"Активный Tor: "+str(response_ips.json()["active_tor"])+'\n'+"Недавний абуз: "+str(response_ips.json()["recent_abuse"])+'\n'+"Ботнет: "+str(response_ips.json()["bot_status"])+'\n'+"Часовой пояс: "+str(response_ips.json()["timezone"]))
		else:
			bot.send_message(m.chat.id, response_ips.json()["message"])
	else:
		pass


bot.infinity_polling()
