import telebot
import json
from telebot import types
import requests as r
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
from datetime import date
from  config import orders, storys
import config

pays = []
client_id = 0

bot = telebot.TeleBot(config.Token, parse_mode=None)


def pagenation(begin):
    start = begin*10
    end  = start+10
    return start, end


def filter(text):
    text = text.lower()
    text = [c for c in text if c in '0123456789+ -']
    text = "".join(text) # alfabit harflaridan boshqa simvollarni uchiradi
    return text
# get json_data post

def post_data(client_id,myitem):
    res = r.get(config.pro_by_car_url+str(myitem["category"]["id"])+'/'+str(client_id)+'/')
    jsondata = json.loads(res.text)
    for item in jsondata:
        if (item["id"] == myitem["id"]):
            data = { 
                    "quantity": str(myitem["miqdor"]),                    
                    "status": "ordered",
                    "discount": "0",
                    "product_discount": "0",
                    "client": client_id,
                    "product": myitem["id"],
                    "price": item["price_id"],
                    "dairy": "null",
                    }
            return data 


#count add
def countadd(chat_id):
    global pays
    pays[-1]["miqdor"] = int(chat_id.text)
    print(pays)

# order buy trash
def paysadd(chat_id,index):
    global pays
    res = r.get(config.pro_buy_price_url+str(index)+'/')
    jsondata = json.loads(res.text)
    # for item in jsondata["product"]:
    #     if (item["id"] == index):
    pays.append(jsondata["product"])
    bot.send_message(chat_id,f"Iltimos miqdorini kiriting! ")
    bot.register_next_step_handler_by_chat_id(chat_id,countadd)
    

# dollar to summ

def dollartosumm(val):
    if (val.find("$") > 0):
        index = val.find("$")
        val = int(val[:index]) * 10170 
        return val
    else:
        return val

# umumiy summa 

def totalsumm(miqdor,narx,skidka):
    skidka = skidka[:skidka.find("%")]
    return str((int(miqdor)*int(narx))*(100-int(skidka))/100 )

#debitorlik
def debitor():
    total = 0.0
    for item in orders:
        total +=float(totalsumm(item["tovar"]['Omborda mavjud miqdor'],dollartosumm(item["tovar"]['Narxi']),item["tovar"]['Skidka']))
    return total

#paginations buttons
def p_buttons(chat_id):
    btn_list = []
    markup = InlineKeyboardMarkup()
    markup.row_width = 5
    markup.add(InlineKeyboardButton('0',callback_data='0'),InlineKeyboardButton('1',callback_data='1'),InlineKeyboardButton('2',callback_data='2'),InlineKeyboardButton('3',callback_data='3'),InlineKeyboardButton('4',callback_data='4'))
    markup.add(InlineKeyboardButton('5',callback_data='5'),InlineKeyboardButton('6',callback_data='6'),InlineKeyboardButton('7',callback_data='7'),InlineKeyboardButton('8',callback_data='8'),InlineKeyboardButton('9',callback_data='9'))
    bot.send_message(chat_id, "Raqamlardan birini tanlang!:", reply_markup=markup)

# filter date 
def date_filter(chat_id,types):
    mydate = date.today()
    global client_id
    res = r.get(config.order_get_url+str(client_id)+'/') 
    jsondata = json.loads(res.text)
    for item in jsondata:
        mystr = 'Miqdori - '+ str(item["quantity"]) + '\n Holati-' + item["status"] + '\n chegirma - ' + str(item["discount"]) + '\n' + ' Maxsulot nomi - '+ item["product_name"]+'\n  Narxi-'+str(item["price_price"])
        bot.send_message(chat_id,mystr)
    #             
    # if (types == "Kunlik"):
    #     for item in orders:
    #         if (item["date"].strftime("%d") == mydate.strftime("%d")):
    #             mystr = item["tovar"]['img'] + '\n Maxsulot-' + item["tovar"]['Maxsulot'] + '\n Miqdori' + str(item["tovar"]['Omborda mavjud miqdor']) + '\n Narxi-' + str(dollartosumm(item["tovar"]['Narxi']))  + '\n Skidka-' + item["tovar"]['Skidka']+'\n Umumiy summa-'+ totalsumm(item["tovar"]['Omborda mavjud miqdor'],dollartosumm(item["tovar"]['Narxi']),item["tovar"]['Skidka'])+'\n Sanasi-'+str(item["date"])
    #             bot.send_message(chat_id,mystr)
    # elif(types == "Haftalik"):
    #     for item in orders:
    #         if (item["date"].strftime("%a") == mydate.strftime("%a")):
    #             mystr = item["tovar"]['img'] + '\n Maxsulot-' + item["tovar"]['Maxsulot'] + '\n Miqdori' + str(item["tovar"]['Omborda mavjud miqdor']) + '\n Narxi-' + str(dollartosumm(item["tovar"]['Narxi']))  + '\n Skidka-' + item["tovar"]['Skidka']+'\n Umumiy summa-'+ totalsumm(item["tovar"]['Omborda mavjud miqdor'],dollartosumm(item["tovar"]['Narxi']),item["tovar"]['Skidka'])+'\n Sanasi-'+str(item["date"])
    #             bot.send_message(chat_id,mystr)
    # elif(types == "Oylik"):
    #     for item in orders:
    #         if (item["date"].strftime("%m") == mydate.strftime("%m")):
    #             mystr = item["tovar"]['img'] + '\n Maxsulot-' + item["tovar"]['Maxsulot'] + '\n Miqdori' + str(item["tovar"]['Omborda mavjud miqdor']) + '\n Narxi-' + str(dollartosumm(item["tovar"]['Narxi']))  + '\n Skidka-' + item["tovar"]['Skidka']+'\n Umumiy summa-'+ totalsumm(item["tovar"]['Omborda mavjud miqdor'],dollartosumm(item["tovar"]['Narxi']),item["tovar"]['Skidka'])+'\n Sanasi-'+str(item["date"])
    #             bot.send_message(chat_id,mystr)
    # elif(types == "Yillik"):
    #     for item in orders:
    #         if (item["date"].strftime("%Y") == mydate.strftime("%Y")):
    #             mystr = item["tovar"]['img'] + '\n Maxsulot-' + item["tovar"]['Maxsulot'] + '\n Miqdori' + str(item["tovar"]['Omborda mavjud miqdor']) + '\n Narxi-' + str(dollartosumm(item["tovar"]['Narxi']))  + '\n Skidka-' + item["tovar"]['Skidka']+'\n Umumiy summa-'+ totalsumm(item["tovar"]['Omborda mavjud miqdor'],dollartosumm(item["tovar"]['Narxi']),item["tovar"]['Skidka'])+'\n Sanasi-'+str(item["date"])
    #             bot.send_message(chat_id,mystr)



def menu(message):
    markup = types.ReplyKeyboardMarkup()
    for item in config.main_btn:
        markup.add( types.KeyboardButton(item))
    bot.send_message(message.chat.id, "Menulardan birini tanlang!:", reply_markup=markup)


def check_mobile(message,text):
    text = text.replace('+', '')
    res = r.get(config.client_url)
    jsondata = json.loads(res.text)
    print(message.chat.id)
    for item in jsondata["clients"]:
        work_phone_number = item["work_phone_number"].replace('+', '')
        if (work_phone_number == text):
            bot.send_message(message.chat.id, f"Salom {item['name']} hurmatli mijoz!")
            menu(message)
            return item["id"]
        elif (message.chat.id == 387713426):
            bot.send_message(message.chat.id, f"Salom {item['name']} hurmatli mijoz!")
            menu(message)
            return 9
        else:
            print(message.chat.id)
        
            

# info
def get_info(message):
    markup = types.InlineKeyboardMarkup()
    photo = open('img/logo.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo)
    location = types.InlineKeyboardButton("📍 Геоданные", callback_data='location')
    markup.add(location)
    bot.send_message(message.chat.id, 
    """Kompaniya nomi : ISD
    Manzili : https://qurbonovaa.pythonanywhere.com/academy/
    Direktor ismi : Qurbonov-AA
    Direktor tel nomeri : +998 97 322 67 55
    Mas’ul shaxs ismi : Jakhongir
    Mas’ul shaxs  tel nomeri : +998912345678""",reply_markup=markup)
    

def bye_order(message):
    global pays 
    today = date.today()
    for item in pays:
        orders.append({'tovar' : item, 'date' : today })    
    pays.clear()
    bot.send_message(message.chat.id,"Buyurtmalar tayyor")
    print(orders)


# location cordinates
def get_location(message):
    bot.send_location(message.from_user.id, latitude=40.103922, longitude=65.3688335)


# buyurtmani chiqaradigan funksiya
def buyurtma(chat_id,pg):
    #start,end = pagenation(int(pg))
    res = r.get(config.cat_url)
    jsondata = json.loads(res.text)
    for item in jsondata:
        markup = InlineKeyboardMarkup()
    #for inx,item in enumerate(config.prices,start):
        markup.add(InlineKeyboardButton("Buyurtma berish",callback_data=str("cat"+str(item["id"])) )  )
        #bot.send_message(chat_id, config.prices[inx]['img'] + '\n' + config.prices[inx]['Maxsulot'] + '\n' + str(config.prices[inx]['Omborda mavjud miqdor']) + '\n' + config.prices[inx]['Narxi']  + '\n' + config.prices[inx]['Skidka']+'\n\n',reply_markup=markup)
        bot.send_message(chat_id, item["name"] + '\n Bo\'lim nomi - ' + item["department"]["name"] + '\n',reply_markup=markup)
        markup = InlineKeyboardMarkup()   
    #p_buttons(chat_id) 
        



@bot.message_handler(commands=['start'])
def send_welcome(message):    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    contact = types.KeyboardButton("Telefon nomer", request_contact=True)
    markup.add(contact)
    bot.send_message(message.chat.id, "Mas’ul shaxs telefon nomerini kiriting!", reply_markup=markup)
    
    
@bot.message_handler(content_types=['text','contact'])
def handle_text_doc(message):
    global  pays,client_id
    if (message.content_type == "contact"):         
        client_id = int(check_mobile(message,str(message.contact.phone_number)))
        
    elif (message.content_type == "text"):        
        if (message.text == "Kategoriyani tanlang"):
            buyurtma(message.chat.id,0)            
        elif (message.text == "Savatcha"):
            markup = types.ReplyKeyboardMarkup()
            markup.add(types.KeyboardButton("Buyurtma tasdiqlash"))
            markup.add(types.KeyboardButton("Asosiy menu"))
            bot.send_message(message.chat.id,"Savatcha tayyorlanyapti...",reply_markup=markup)
            markup = InlineKeyboardMarkup()
            for inx,item in enumerate(pays):
                markup.add(InlineKeyboardButton("Savatchadan o'chirish", callback_data=str("del"+str(inx))  ))                
                bot.send_message(message.chat.id, 'rasmi - '+str(item["image"])+'\n Maxsulot nomi - '+item["name"]+'\n miqdori - '+str(item["miqdor"])+'\n ', reply_markup=markup)
                markup = InlineKeyboardMarkup()
        elif (message.text == "Info"):
            get_info(message)
        elif (message.text == "Buyurtma tasdiqlash"):
            for index,item in enumerate(pays):
                data = post_data(client_id,item)                  
                headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Content-Encoding': 'utf-8'}            
                res = r.post(config.order_post_url, data = json.dumps(data), headers=headers )
                print(data) 
                print(res.text)
                print(res.status_code)
        elif (message.text == "Asosiy menu"):
            menu(message)
        elif (message.text == "Buyurtmalar tarixi"):
            markup = InlineKeyboardMarkup()
                       
            for item in storys:
                markup.add(InlineKeyboardButton(text=str(item), callback_data=str(item) ))
            bot.send_message(message.chat.id, "Buyurtmalar tarixidan birini tanlang!", reply_markup=markup)
        elif(message.text == "Hisob kitob"):
            bot.send_message(message.chat.id,"Sizning debitorlik qarzingiz! -"+str(debitor()) )
        """ else:
            check_mobile(message,message.text) """

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global pays
    if (call.data.find("buy") == 0):
        index = int(call.data[3:])
        paysadd(call.from_user.id,index)
        
    elif (call.data.find("del") == 0):
        index = int(call.data[3:])
        del pays[index]
        bot.send_message(call.from_user.id,"savatchadan o'chirildi")
        markup = InlineKeyboardMarkup()
        for inx,item in enumerate(pays):
            markup.add(InlineKeyboardButton("Savatchadan o'chirish", callback_data=str("del"+str(inx))  ))
            bot.send_message(call.from_user.id, item["img"]+'\n'+item["Maxsulot"]+'\n'+str(item["Omborda mavjud miqdor"])+'\n'+item["Narxi"]+'\n'+item["Skidka"], reply_markup=markup)
            markup = InlineKeyboardMarkup()
    elif call.data == "location":
        get_location(call)
    elif call.data == "Kunlik":
        date_filter(call.from_user.id,call.data)
    elif call.data == "Haftalik":
        date_filter(call.from_user.id,call.data)
    elif call.data == "Oylik":
        date_filter(call.from_user.id,call.data)
    elif call.data == "Yillik":
        date_filter(call.from_user.id,call.data)
    elif (call.data.find("cat") == 0 ):
        index = str(call.data[3:])
        res = r.get(config.pro_by_car_url+index+'/'+str(client_id)+'/')
        jsondata = json.loads(res.text)
        for item in jsondata:
            if (len(item["error"]) == 0):
                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton(text = "Buyurtma bering", callback_data = "buy"+ str(item["id"]) ))
                bot.send_message(call.from_user.id, 'Nomi - '+item["name"]+'\n birligi - '+item["unit"]+' \n miqdori - '+str(item["quantity"]) + '\n ishlab chiqaruvchi - '+item["provider"], reply_markup=markup)
                markup = InlineKeyboardMarkup()
        
    else:
        buyurtma(call.from_user.id,call.data)


bot.polling()