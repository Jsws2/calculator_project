from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLineEdit
import sys

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("계산기")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.input_box = QLineEdit(self)
        layout.addWidget(self.input_box)

        self.grid_layout = QGridLayout()


#계산기 버튼

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]


#버튼 생성하고 배치

        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(lambda checked, b=text: self.on_button_click(b))
            self.grid_layout.addWidget(button, row, col)

        layout.addLayout(self.grid_layout)
        self.setLayout(layout)

#버튼 클릭 시 실행하기

    def on_button_click(self, button_text):
        """버튼 클릭 시 실행"""
        current_text = self.input_box.text()

        if button_text == '=':
            try:
                result = str(eval(current_text))
                self.input_box.setText(result)
            except Exception:
                self.input_box.setText("Error")
        else:
            self.input_box.setText(current_text + button_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())

