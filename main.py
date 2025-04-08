import telebot 

TOKEN = '7539618081:AAHmJ5EDTDLVR6CNvihQGQ7qET4g49qgmqM'
bot = telebot.TeleBot(TOKEN)

#Diccionario de productos por pasillo:
pasillos = {
    1: ['carne', 'queso', 'jamón'],
    2: ['leche', 'yogurth', 'cereal'],
    3: ['bebidas', 'jugos'],
    4: ['pan', 'pasteles', 'tortas'],
    5: ['detergente', 'lavaloza']
}


## Creación de comandos simples como "/start" y "/help"
#Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola! Soy el bot de la actividad sumativa de la Semana 3, creado con Telebot para encontrar productos en un supermercado.')

#comando /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Hola, dime uno de los siguientes productos: Carne, Queso, Jamón, Leche, Yogurth, Cereal, Bebidas, Jugos, Pan, Pasteles, Tortas, Detergente o lavaloza y te diré en qué pasillo encontrarlos.')



##decorador con función anónima que repite el texto del user
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

##decorador con función anónima para respuestas personalizadas:
# @bot.message_handler(func=lambda m: True)
# def respuesta_personalizada(message):
#     texto = message.text.lower()

#     if 'hola' in texto:
#         bot.reply_to(message, 'Hola, ¿cómo estás?')
#     elif 'adiós' in texto:
#         bot.reply_to(message, 'Hasta luego, ¡que tengas un buen día!')
#     elif 'gracias' in texto:
#         bot.reply_to(message, 'De nada, ¡que tengas un buen día!')
#     else:
#         bot.reply_to(message, 'No entiendo, ¿puedes repetir?')


#Función para manejar productos 
@bot.message_handler(func=lambda message: True)
def buscar_producto(message):
    texto = message.text.lower().strip()

    encontrado = False
    for numero_pasillo, productos in pasillos.items():
        if texto.strip() in productos:
            bot.reply_to(message, f'El producto {texto} se encuentra en el pasillo {numero_pasillo}.')
            encontrado = True
            break 
    
    if not encontrado:
        bot.reply_to(message, 'Lo siento, no entiendo la pregunta.')




#método que verifica si hay nuevos mensajes. 
if __name__ == "__main__":
    bot.polling(none_stop=True) 