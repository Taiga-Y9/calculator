# main.py

import sys
from PySide6.QtWidgets import QApplication
from calculator_app import CalculatorApp  # CalculatorAppクラスをインポート

if __name__ == "__main__":
  app = QApplication(sys.argv)
  calculator = CalculatorApp()
  calculator.show()
  sys.exit(app.exec())
