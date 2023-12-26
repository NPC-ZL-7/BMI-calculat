from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class BMIApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.layout.add_widget(Label(text='Добро пожаловать в ИМТ-калькулятор!'))
        
        self.weight_input = TextInput(hint_text='Введите ваш вес (кг)')
        self.layout.add_widget(self.weight_input)
        
        self.height_input = TextInput(hint_text='Введите ваш рост (см)')
        self.layout.add_widget(self.height_input)
        
        self.age_input = TextInput(hint_text='Введите ваш возраст (13-18)')
        self.layout.add_widget(self.age_input)
        
        self.name_input = TextInput(hint_text='Введите ваше имя')
        self.layout.add_widget(self.name_input)
        
        self.gender_input = TextInput(hint_text='Введите ваш пол (1 - Мужской, 2 - Женский)')
        self.layout.add_widget(self.gender_input)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        self.calculate_button = Button(text='Рассчитать ИМТ', on_press=self.calculate_bmi)
        self.layout.add_widget(self.calculate_button)

        return self.layout

    def calculate_bmi(self, instance):
        try:
            weight = float(self.weight_input.text)
            height = float(self.height_input.text)
            age = float(self.age_input.text)
            name = self.name_input.text
            gender = self.gender_input.text

            bmi = weight / ((height / 100) * (height / 100))
            self.result_label.text = f'Уважаемый, {name}, ваш ИМТ равен {round(bmi, 2)}'

            # Ваш код для расчета и вывода рекомендаций по ИМТ и возрасту
            if age == 13:
                if bmi >= 21.9 and bmi <= 25:
                    self.result_label.text += '\nСядь на легкую диету, и не ешь много жирного! Сбрось эти лишние килограммы!'
                elif bmi <= 15.4:
                    self.result_label.text += '\nКушай немного больше и набери немного веса, после чего занимайся спортом!'
                elif bmi >= 25 and bmi <= 29.3:
                    self.result_label.text += '\nУ вас слишком большой вес, лучше садитесь на диету, и не ешьте много жирного, особенно чипсы и быстрое питание!'
                else:
                    self.result_label.text += "\nМолодец!!! ТАК ДЕРЖАТЬ!"

            elif age == 14:
                if bmi >= 22.7 and bmi <= 26.3:
                    self.result_label.text += '\nУ тебя лишний вес! Иди займись спортом и найди подругу!!!'
                elif bmi <= 16:
                    self.result_label.text += '\nКушай и занимайся спортом! Имей хорошее тело!'
                elif bmi >= 26.3 and bmi <= 30:
                    self.result_label.text += '\nСядь на диету и восстанови тело!'
                else:
                    self.result_label.text += '\nУф, иди развлекайся, но не теряй форму!'

            if age == 15:
                if bmi >= 23.5 and bmi <= 26.5:
                    self.result_label.text += '\nУ вас лишние пару килограмм!'
                elif bmi <= 16.5:
                    self.result_label.text += '\nКушайте, и всё будет хорошо!'
                elif bmi >= 26.5 and bmi <= 31:
                    self.result_label.text += '\nВоу, Воу, меньше кушайте!'
                else:
                     self.result_label.text += '\nМолодец! Держи себя в форме!'

        except ValueError:
            self.result_label.text = 'Пожалуйста, введите корректные данные'

            if age == 16:
                 if bmi >= 24.2 and bmi <= 27.7:
                     self.result_label.text += '\nУ вас лишний вес, может быть скоро ожирение. Начните меньше кушать чипсы и колбасу!'
                 elif bmi <= 17.1:
                    self.result_label.text += '\nКушайте больше, у вас недоедание.'
                 elif bmi >= 27.7 and bmi <= 31.2:
                    self.result_label.text += '\nУ вас, вероятно, ожирение!'
                 else:
                     self.result_label.text += '\nВсё ок'

            if age == 17:
                 if bmi >= 25 and bmi <= 29:
                     self.result_label.text += '\nУ вас лишний вес. Меньше кушайте много сладкого!'
                 elif bmi >= 29 and bmi <= 31.5:
                        self.result_label.text += '\nМеньше поедайте вкусности и сядьте, наконец, на диету!'
                 elif bmi <= 17.6:
                        self.result_label.text += '\nУ вас недоедание'
                 else:
                     self.result_label.text += '\nУ вас отличный ИМТ! Поздравляю!'

            if age == 18:
                 if bmi >= 25.7 and bmi <= 29:
                    self.result_label.text += '\nУ вас лишний вес. Начните заниматься спортом и ходить в тренажерный зал!'
                 elif bmi <= 18.2:
                    self.result_label.text += '\nУ вас недоедание!'
                 elif bmi >= 29 and bmi <= 35:
                     self.result_label.text += '\nУ вас, возможно, слишком избыточный вес! Обратитесь к врачу!'
                 else:
                     self.result_label.text += '\nУ вас нормальный ИМТ! Поздравляю!'



if __name__ == '__main__':
    BMIApp().run()
