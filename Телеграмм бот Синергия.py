from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 1. Определение ключевых слов и ответов
QA_DICT = {
    ("привет", "здравствуй", "начать", "hello"): "Привет! Я чат-бот для абитуриентов Университета Синергия. Спроси меня о факультетах, документах, сроках подачи или стоимости обучения.",
    ("факультет", "направлен", "специальность"): "В Университете Синергия много факультетов: Экономика, IT-менеджмент, Юриспруденция, Дизайн и др. Подробнее на сайте: synergy.ru/faculties",
    ("документ", "подать", "заявлен"): "Для подачи документов нужны: паспорт, аттестат/диплом, фото. Подать можно онлайн через личный кабинет на сайте или в приёмной комиссии.",
    ("срок", "подача", "когда"): "Приём документов на очную форму обычно до 25 августа, на заочную — дольше. Уточняйте актуальные даты на сайте synergy.ru/abitur.",
    ("стоимость", "цена", "обучен", "плат"): "Стоимость обучения зависит от факультета и формы. Примерный диапазон: от 50 до 200 тыс. руб. в год. Точную сумму рассчитает менеджер.",
    ("контакт", "телефон", "адрес", "связаться"): "Контакты приёмной комиссии: Москва, ул. Измайловский вал, д.2. Телефон: +7 (495) 800-10-01. Почта: priem@synergy.ru.",
    ("спасибо", "отличный", "помог"): "Рад был помочь! Удачи на вступительных испытаниях!",
}

# 2. Функция для распознавания ключевых слов и предоставления ответа
def get_answer(user_text: str) -> str:
    user_text_lower = user_text.lower()
    for keywords, answer in QA_DICT.items():
        if any(keyword in user_text_lower for keyword in keywords):
            return answer
    return "Извините, я ещё не знаю ответ на этот вопрос. Пожалуйста, обратитесь напрямую в приёмную комиссию по телефону +7 (495) 800-10-01."

# 3. Обработчик входящих текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    # Логируем сообщение
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # Получаем ответ
    response = get_answer(text)

    # Отправляем ответ
    await update.message.reply_text(response)

# 4. Основная функция
def main():
    # Указываем токен бота
    TOKEN = "ТОКЕН ТЕЛЕГРАМ"

    # Создаем приложение
    app = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    print("Бот запускается...")
    app.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()