import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class CalculatorApp(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Calculator")
    self.setGeometry(100, 100, 300, 300)

    self.sy = 0  # ステータス (0: n1の入力中, 1: n2の入力中, 2: 結果の表示中)
    self.n1 = 0  # 最初の数値
    self.n2 = 0  # 2番目の数値
    self.operator = None  # 演算子

    # レイアウトを作成
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    # 結果表示用のテキストボックスを作成
    self.result_display = QLineEdit()
    self.result_display.setReadOnly(True)  # ユーザーが直接入力できないように
    self.layout.addWidget(self.result_display)

    # グリッドレイアウトを作成
    self.grid_layout = QGridLayout()
    self.layout.addLayout(self.grid_layout)

    # 数字ボタンを作成
    buttons = [
        7, 8, 9, '÷',
        4, 5, 6, '*',
        1, 2, 3, '-',
        0, 'C', '=', '+'
    ]

    # ボタンをグリッドに挿入
    for i, button in enumerate(buttons):
      self.add_button(button, i // 4, i % 4)

  def add_button(self, text, row, col):
    button = QPushButton(str(text))  # ボタンのテキストを文字列に変更
    button.setStyleSheet(
        "font-size: 18px; padding: 10px; background-color: lightblue;")  # ボタンのスタイル設定
    button.clicked.connect(
        lambda: self.on_button_click(text))  # ボタンが押されたときの処理を設定
    self.grid_layout.addWidget(button, row, col)

  def on_button_click(self, text):
    if isinstance(text, int) and self.sy < 2:  # 数字ボタンがクリックされた場合
      if self.sy == 0:  # n1の入力中
        self.n1 = self.n1 * 10 + text
        self.result_display.setText(str(self.n1))
      elif self.sy == 1:  # n2の入力中
        self.n2 = self.n2 * 10 + text
        self.result_display.setText(str(self.n2))
    elif text in ('+', '-', '*', '÷'):  # 演算子ボタンがクリックされた場合
      if self.sy == 0:  # n1の入力が完了したら
        self.operator = text
        self.sy = 1  # 次はn2の入力
        self.result_display.setText("")  # 入力をクリア
    elif text == '=':  # =ボタンがクリックされた場合
      if self.sy == 1:  # n2の入力完了後に計算
        result = self.calculate(self.n1, self.n2, self.operator)
        self.result_display.setText(str(result))
        self.sy = 2  # 結果表示中にステータスを変更
        self.n1 = result  # 結果を次の計算のn1として使用できるように
        self.n2 = 0
        self.operator = None
    elif text == 'C':  # Cボタンがクリックされた場合
      self.clear()  # 計算機の状態をリセット

  def calculate(self, n1, n2, operator):
    if operator == '+':
      return n1 + n2
    elif operator == '-':
      return n1 - n2
    elif operator == '*':
      return n1 * n2
    elif operator == '÷':
      return n1 / n2 if n2 != 0 else 'Error'  # ゼロで割った場合のエラーチェック

  def clear(self):
    """ 計算機の状態を初期化します。 """
    self.n1 = 0
    self.n2 = 0
    self.operator = None
    self.sy = 0
    self.result_display.clear()  # 入力表示をクリア


if __name__ == "__main__":
  app = QApplication(sys.argv)
  calculator = CalculatorApp()
  calculator.show()
  sys.exit(app.exec())
