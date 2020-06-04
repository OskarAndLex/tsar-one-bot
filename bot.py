import telebot
import random
import os

from telebot import types

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))



@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("⚽️ИГРАТЬ⚽️")
	item2 = types.KeyboardButton("👮‍♂️АДМИН👮‍♂️")
	item3 = types.KeyboardButton("💡ИНФО💡")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, '''Приветствую, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы играть в игру 'Царство'.\nЗдесь ты сможешь заработать помогая друг другу. НАЖМИ "ИНФО" перед началом.\nP.S. извините за неудобства, это ранняя версия бота)'''.format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':

		if message.text == '⚽️ИГРАТЬ⚽️':

			markup_1 = types.InlineKeyboardMarkup(row_width=2)
			markup_2 = types.InlineKeyboardMarkup(row_width=2)
			markup_3 = types.InlineKeyboardMarkup(row_width=2)
			markup_4 = types.InlineKeyboardMarkup(row_width=2)
			markup_5 = types.InlineKeyboardMarkup(row_width=2)
			markup_6 = types.InlineKeyboardMarkup(row_width=2)
			markup_7 = types.InlineKeyboardMarkup(row_width=2)
			markup_8 = types.InlineKeyboardMarkup(row_width=2)
			markup_9 = types.InlineKeyboardMarkup(row_width=2)
			markup_10 = types.InlineKeyboardMarkup(row_width=2)

			item1 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_1')
			item2 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_1')
			item3 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_2')
			item4 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_2')
			item5 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_3')
			item6 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_3')
			item7 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_4')
			item8 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_4')
			item9 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_5')
			item10 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_5')
			item11 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_6')
			item12 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_6')
			item13 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_7')
			item14 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_7')
			item15 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_8')
			item16 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_8')
			item17 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_9')
			item18 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_9')
			item19 = types.InlineKeyboardButton("ВЫБРАТЬ!!!", callback_data='play_10')
			item20 = types.InlineKeyboardButton("<- Список игроков", callback_data='user_list_10')

			

			markup_1.add(item1, item2)
			markup_2.add(item3, item4)
			markup_3.add(item5, item6)
			markup_4.add(item7, item8)
			markup_5.add(item9, item10)
			markup_6.add(item11, item12)
			markup_7.add(item13, item14)
			markup_8.add(item15, item16)
			markup_9.add(item17, item18)
			markup_10.add(item19, item20)

			bot.send_message(message.chat.id, 'Отлично, какое царсвто выбираешь? Вот доступные!')
			bot.send_message(message.chat.id, 'Царсвто №1', reply_markup=markup_1)
			# bot.send_message(message.chat.id, 'Царсвто №2', reply_markup=markup_2)
			# bot.send_message(message.chat.id, 'Царсвто №3', reply_markup=markup_3)
			# bot.send_message(message.chat.id, 'Царсвто №4', reply_markup=markup_4)
			# bot.send_message(message.chat.id, 'Царсвто №5', reply_markup=markup_5)
			# bot.send_message(message.chat.id, 'Царсвто №6', reply_markup=markup_6)
			# bot.send_message(message.chat.id, 'Царсвто №7', reply_markup=markup_7)
			# bot.send_message(message.chat.id, 'Царсвто №8', reply_markup=markup_8)
			# bot.send_message(message.chat.id, 'Царсвто №9', reply_markup=markup_9)
			# bot.send_message(message.chat.id, 'Царсвто №10', reply_markup=markup_10)

		elif message.text == '👮‍♂️АДМИН👮‍♂️':
			markup = types.InlineKeyboardMarkup()
			markup.add(types.InlineKeyboardButton("Посетить", url="https://t.me/OskaRandL"))
			bot.send_message(message.chat.id, 'Хорошо, его имя Александр. Не обижай одмена)', parse_mode='html', reply_markup=markup)

		elif message.text == '💡ИНФО💡':

			markup = types.InlineKeyboardMarkup(row_width=2)

			item1 = types.InlineKeyboardButton("СУТЬ ИГРЫ", callback_data='info_1')
			item2 = types.InlineKeyboardButton("ПРАВИЛА", callback_data='info_2')
			item3 = types.InlineKeyboardButton("КАК НАЧАТЬ", callback_data='info_3')
			item4 = types.InlineKeyboardButton("КУДА ИДУТ ДЕНЬГИ", callback_data='info_4')
			item5 = types.InlineKeyboardButton("ЗАЧЕМ АДМИН", callback_data='info_5')
			item6 = types.InlineKeyboardButton("ВЫГОДА ПРОЭКТА", callback_data='info_6')
			item7 = types.InlineKeyboardButton("МОЙ СТАТУС", callback_data='info_7')
			item8 = types.InlineKeyboardButton("ВЫИГРЫШ", callback_data='info_8')
			item9 = types.InlineKeyboardButton("ПРОИГРАВШИЕ", callback_data='info_9')
			item10 = types.InlineKeyboardButton("ВДРУГ ОБМАН", callback_data='info_10')
			item11 = types.InlineKeyboardButton("МОШЕННИКИ", callback_data='info_11')
			item12 = types.InlineKeyboardButton("ПРОЧЕЕ", callback_data='info_12')

			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

			bot.send_message(message.chat.id, '''📝Здесь представлена вся актуальная информация которая тебе будет интересна📝''', parse_mode='html', reply_markup=markup)

		elif message.text == 'tsar1':
			bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №1👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar2':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №2👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar3':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №3👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar4':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №4👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar5':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №5👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar6':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №6👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar7':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №7👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar8':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №8👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar9':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №9👍\nУДАЧНОЙ ИГРЫ")

		# elif message.text == 'tsar10':
		# 	bot.send_message(message.chat.id, "👍Отлично, ты теперь принадлежишь Царству №10👍\nУДАЧНОЙ ИГРЫ")

		else:
			bot.send_message(message.chat.id, 'Извини, я не обучен понимать текстовые сообщения такого формата. Мой админ не такой умный 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'play_1':
				markup = types.InlineKeyboardMarkup()
				markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
				bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №1 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_2':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №2 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_3':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №3 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_4':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №4 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_5':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №5 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_6':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №6 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_7':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №7 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_8':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №8 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_9':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №9 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)
			# elif call.data == 'play_10':
			# 	markup = types.InlineKeyboardMarkup()
			# 	markup.add(types.InlineKeyboardButton("👮‍♂️ОДМЕН👮‍♂️", url="https://t.me/OskaRandL"))
			# 	bot.send_message(call.message.chat.id, '''✅✅✅ ЦАРСТВО №10 ВЫБРАНО ✅✅✅\nПиши Админу и говори какое царство выбрал)''', parse_mode='html', reply_markup=markup)

			elif call.data == 'user_list_1':
				f1 = open('user_list1.txt', encoding = "utf-8")
				line1 = f1.read()
				f1.close()
				bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №1👑\n', line1))
			# elif call.data == 'user_list_2':
			# 	f2 = open('user_list2.txt', encoding = "utf-8")
			# 	line2 = f2.read()
			# 	f2.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №2👑\n', line2))
			# elif call.data == 'user_list_3':
			# 	f3 = open('user_list3.txt', encoding = "utf-8")
			# 	line3 = f3.read()
			# 	f3.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №3👑\n', line3))
			# elif call.data == 'user_list_4':
			# 	f4 = open('user_list4.txt', encoding = "utf-8")
			# 	line4 = f4.read()
			# 	f4.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №4👑\n', line4))
			# elif call.data == 'user_list_5':
			# 	f5 = open('user_list5.txt', encoding = "utf-8")
			# 	line5 = f5.read()
			# 	f5.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №5👑\n', line5))
			# elif call.data == 'user_list_6':
			# 	f6 = open('user_list6.txt', encoding = "utf-8")
			# 	line6 = f6.read()
			# 	f6.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №6👑\n', line6))
			# elif call.data == 'user_list_7':
			# 	f7 = open('user_list7.txt', encoding = "utf-8")
			# 	line7 = f7.read()
			# 	f7.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №7👑\n', line7))
			# elif call.data == 'user_list_8':
			# 	f8 = open('user_list8.txt', encoding = "utf-8")
			# 	line8 = f8.read()
			# 	f8.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №8👑\n', line8))
			# elif call.data == 'user_list_9':
			# 	f9 = open('user_list9.txt', encoding = "utf-8")
			# 	line9 = f9.read()
			# 	f9.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №9👑\n', line9))
			# elif call.data == 'user_list_10':
			# 	f10 = open('user_list10.txt', encoding = "utf-8")
			# 	line10 = f10.read()
			# 	f10.close()
			# 	bot.send_message(call.message.chat.id, '{} {}'.format('👑ЦАРСТВО №10👑\n', line10))
			
			elif call.data == 'info_1':
				bot.send_message(call.message.chat.id, 
					"""Есть Царство. В Царстве 4 "касты". ЦАРЬ - 1 чел. КНЯЗЬЯ - 2 чел. БОЯРЕ - 4 чел. ХОЛОПЫ - 8 чел.
					Игрок в зоне ЦАРЬ получает деньги от игроков в зоне ХОЛОПЫ. После того как ЦАРЬ получил свои деньги - он выбывает из игры.
					Царство делится на ДВА Царства пополам. КНЯЗЬЯ стают ЦАРЯМИ в своих Царствах. БОЯРЕ стают КНЯЗЬЯМИ (по 2 чел. в каждое Царство). ХОЛОПЫ стают 
					БОЯРИНАМИ (по 4 чел. в каждое Царство). После этого происходит набор игроков в зону ХОЛОПЫ. И так до БЕСКОНЕЧНОСТИ. """)
			elif call.data == 'info_2':
				bot.send_message(call.message.chat.id, """1.Ознакомится с доступной информацией, выбрать доступное Царство, следовать инструкциям бота.
					2.Перевести 250 грн на реквизиты что укажет администратор, отправить чек об оплате "Администратору игры".(200 грн идут ЦАРЮ, 50 грн - АДМИН использует 
					для рекламы в различных проэктах)
					3.Администратор вставляет Ваше имя в список игроков Царства.
					4.Как только Царство полностью заполняется, игрок находящейся в зоне "ЦАРЬ" получает свой выигрыш 1600 гривен на карту и выбывает из игры.
					5.Все игроки перемещаются на следующую зону, и уже вновь прибывшему игроку в зоне "ЦАРЬ", игроки из зоны "ХОЛОПЫ" отправляют деньги.
					6.И так до бесконечности.
					7.В игру можно играть неограниченное количество раз, начиная заново с зоны "ХОЛОПЫ".
					8.Вы можете активно привлекать новых игроков в свое Царство, очень быстро заполняя места, а можете просто просто ждать заполнения, так как 
					администрация РЕКЛАМИРУЕТ проект на различных ресурсах.
					9.Не теряй времени зря, чем раньше ты вступишь в игру, тем быстрее получишь свои 1600 гривен.""")
			elif call.data == 'info_3':
				bot.send_message(call.message.chat.id, """1. Пополните фонд игры на 250 гривен на выданные администратором банковские реквизиты.
					2. После оплаты пришлите администратору чек и реквизиты карты с которой происходила оплата (в последствии туда будет зачислен Ваш выигрыш 1600 гривен)
					3. (ПО ЖЕЛАНИЮ) Размести пост или сторис о своем вступлении в игру с ссылкой на бота.
					4. Отслеживай свои перемещения и заполнение Царства твоей команды в Нашем боте через кнопку "Список игроков" прикрепленную к твоему Царству (Царство №1 "пример")
					5. Получай выигрыш 1600 гривен на свою карту и поделись скрином о зачислении и своем опыте участия в игре в отзыве и отправь администратору.""")
			elif call.data == 'info_4':
				bot.send_message(call.message.chat.id, """Администрация собирает фонд игрока в зоне "ЦАРЬ". Когда собирается 100% сумма - деньги переводятся ЦАРЮ.
					Все перечисления происходят открыто, любой игрок может запросить выписку перевода.
					Администрация также активно участвует в игре, 
					аналогично оплачивая свое участие игроку в зоне "ЦАРЬ".""")
			elif call.data == 'info_5':
				bot.send_message(call.message.chat.id, """Задача администратора: правильное функционирование игры,
					внесение в Царство новых игроков и создание комьюнити данного проекта.""")
			elif call.data == 'info_6':
				bot.send_message(call.message.chat.id, """Монетизация проекта происходит исключительно за счёт внесения 
					собственных средств в фонд игры игры принятия активного участия в привлечении новых игроков.""")
			elif call.data == 'info_7':
				bot.send_message(call.message.chat.id, """При вступлении в Царство Вы получаете, номер Царства (пример "ЦАРСТВО №1").
					Бот предоставляет актуальный список игроков в любое время.
					Все прозрачно, Вы можете следить за игрой 24/7.""")
			elif call.data == 'info_8':
				bot.send_message(call.message.chat.id, """Все зависит от скорости заполнения и Вашего места в Царстве.
					В среднем скорость заполнения царства и получения Вами выигрыша занимает около 48 часов
					*Все временные оценки являются приблизительными и полностью зависят от 
					совокупности актива игроков и носят ознакомительный характер.""")
			elif call.data == 'info_9':
				bot.send_message(call.message.chat.id, """Проигравших в игре "Царство" не бывает, рано или поздно 
					каждый игрок получает свой выигрыш в размере 1600 гривен.""")
			elif call.data == 'info_10':
				bot.send_message(call.message.chat.id, """Никакого обмана нет, при желании все легко поддается анализу, внося 250 гривен в фонд игры (200 грн ЦАРЮ, 50 грн на пиар проэкта) и 
					находясь в зоне "ХОЛОПЫ", Вы пополняете фонд игрока который находиться в зоне "ЦАРЬ". 
					В зоне "ХОЛОПЫ" 8 мест*200грн=1600грн выигрыш игрока находящегося в зоне "ЦАРЬ".
					Администрация хранит фонд ЦАРЯ до момента 100% сбора суммы 1600 грн и потом перечисляет их ЦАРЮ. Все перечисления происходят 
					ИСКЛЮЧИТЕЛЬНО через администрацию, соответственно Администрация ведет полный учет движения средств. По запросу может предоставить информацию любому игроку.""")
			elif call.data == 'info_11':
				bot.send_message(call.message.chat.id, """У БОТА есть кнопка для связи с администратором.
					Чтобы не стать жертвой ФЭЙК админов,пользуйтесь только услугами администратора через КНОПКУ.""")
			elif call.data == 'info_12':
				bot.send_message(call.message.chat.id, """Режим работы: ежедневно с 08:00 до 23:00 по Киевскому времени.
					Во избежании недоразумений все платежи осуществляем только после связи с администратором, 
					и только на выданные им реквизиты.
					Всем победы!!!""")


			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="УДАЧНО")

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)