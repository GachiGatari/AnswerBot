class Button:
    def __init__(self, text, callback):
        self.callback = callback
        self.text = text


class MainButton(Button):
    def __init__(self, text, callback, childs):
        super().__init__(text, callback)
        self.childs = childs


class ChildButton(Button):
    def __init__(self, text, callback):
        super().__init__(text, callback)


MainKeyBoard = {
    'counters': MainButton('Показания счетчиков',
                           'counters',
                           [
                               ChildButton("Сведения о поверке счетчика/Пропали приборы учета", 'data'),
                               ChildButton("Почему я не могу ввести показания счётчиков", 'wrong_input')
                           ]
                           ),
    'registration': MainButton("Проблема регистрации",
                               'registration',
                               [
                                   ChildButton("Не могу зарегистрироваться", 'cant_reg'),
                                   ChildButton("Как подключить еще один ЛС?", 'how_connect'),
                                   ChildButton("Не получается ввести код регистрации", "wrong_reg_code")
                               ]
                               ),
    'pay': MainButton("Оплата",
                      "pay",
                      [
                          ChildButton("До какого числа месяца необходимо оплатить КУ?", "month"),
                          ChildButton("Произвели оплату, но в личном кабинете до сих пор нет оплаты", "fail_pay")
                      ]
                      ),
    'other': MainButton("Другое",
                        "other",
                        [
                            ChildButton("Куда я могу потратить бонусы?", "bonus"),
                            ChildButton("За что могут быть начислены пени?", "fine")
                        ]
                        )
}
