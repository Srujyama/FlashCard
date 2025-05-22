import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QShortcut
from PyQt6.QtGui import QKeySequence
from PyQt6.QtCore import Qt

class FlashCardApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set size of the window
        self.resize(600, 400)

        self.layout = QVBoxLayout(self)
        self.question_label = QLabel(self)
        self.answer_label = QLabel(self)

        # Adjust font size
        self.question_label.setStyleSheet("font-size: 24px")
        self.answer_label.setStyleSheet("font-size: 24px")

        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.answer_label)

        # Set up keyboard shortcuts
        self.flip_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Space), self)
        self.next_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Right), self)
        self.prev_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Left), self)

        self.flip_shortcut.activated.connect(self.toggle_answer)
        self.next_shortcut.activated.connect(self.next_card)
        self.prev_shortcut.activated.connect(self.prev_card)

        self.cards = []
        self.current_card_index = 0
        self.is_flipped = False
        self.load_cards()

        self.show_current_card()

    def load_cards(self):
        with open('flash_cards.json', 'r') as f:
            self.cards = json.load(f)

    def show_current_card(self):
        card = self.cards[self.current_card_index]
        if self.is_flipped:
            self.question_label.setText(card['answer'])
            self.answer_label.setText(card['question'])
        else:
            self.question_label.setText(card['question'])
            self.answer_label.setText('')
        self.is_flipped = False

    def toggle_answer(self):
        self.is_flipped = not self.is_flipped
        self.show_current_card()

    def next_card(self):
        self.current_card_index = (self.current_card_index + 1) % len(self.cards)
        self.is_flipped = False
        self.show_current_card()

    def prev_card(self):
        self.current_card_index = (self.current_card_index - 1) % len(self.cards)
        self.is_flipped = False
        self.show_current_card()


app = QApplication(sys.argv)
window = FlashCardApp()
window.show()
sys.exit(app.exec())
