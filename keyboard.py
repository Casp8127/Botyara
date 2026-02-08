from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_main_keyboard() ->   ReplyKeyboardMarkup:
    """
    Главное меню с Reply-кнопками
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📦 Товары"), KeyboardButton(text="🛒 Корзина")],
            [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="ℹ️ О нас")],
            [KeyboardButton(text="🆘 Помощь")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Выберите действие..."
    )
    return keyboard


def get_categories_keyboard() -> ReplyKeyboardMarkup:
    """
    Клавиатура с категориями товаров
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⚡️ Электроника"), KeyboardButton(text="👕 Одежда")],
            [KeyboardButton(text="📚 Книги"), KeyboardButton(text="🏠 Дом")],
            [KeyboardButton(text="🔙 Назад")]
        ],
        resize_keyboard=True
    )


def get_back_keyboard() -> ReplyKeyboardMarkup:
    """
    Простая кнопка "Назад"
    """
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🔙 Назад")]],
        resize_keyboard=True
    )


def get_inline_menu() -> InlineKeyboardMarkup:
    """
    Inline-меню для дополнительных опций
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📱 Наш сайт", url="https://dengusrazu.ru/"),
                InlineKeyboardButton(text="📢 Канал", url="")
            ],
            [InlineKeyboardButton(text="🔔 Подписаться", callback_data="subscribe")]
        ]
    )


def get_products_inline_keyboard() -> InlineKeyboardMarkup:
    """
    Inline-кнопки для товаров с пагинацией
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🛒 Купить", callback_data="buy_1"),
                InlineKeyboardButton(text="❤️ В избранное", callback_data="favorite_1")
            ],
            [
                InlineKeyboardButton(text="⬅️ Назад", callback_data="prev_page"),
                InlineKeyboardButton(text="1/5", callback_data="page_info"),
                InlineKeyboardButton(text="Вперед ➡️", callback_data="next_page")
            ]
        ]
    )