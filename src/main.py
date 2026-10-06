import sys

from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class KritrPlayer(QWidget):

    def __init__(self):
        super().__init__()

        self.drag_position = QPoint()

        self.setup_window()
        self.setup_ui()

    # -----------------------------------------
    # WINDOW
    # -----------------------------------------

    def setup_window(self):

        self.setWindowTitle("Kritr Player")

        self.setFixedSize(340, 150)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

    # -----------------------------------------
    # UI
    # -----------------------------------------

    def setup_ui(self):

        self.setStyleSheet("""
            QWidget {
                color: #eeeeee;
                font-family: "Segoe UI";
            }

            #card {
                background: #111111;
                border: 1px solid #292929;
                border-radius: 14px;
            }

            #title {
                font-size: 11px;
                font-weight: bold;
                color: #eeeeee;
            }

            #song {
                font-size: 16px;
                font-weight: 600;
            }

            #artist {
                font-size: 12px;
                color: #777777;
            }

            QPushButton {
                background: transparent;
                border: none;
                color: #aaaaaa;
                font-size: 18px;
                border-radius: 7px;
                padding: 5px;
            }

            QPushButton:hover {
                background: #242424;
                color: white;
            }

            #play {
                background: #eeeeee;
                color: #111111;
                border-radius: 8px;
                font-size: 14px;
            }

            #play:hover {
                background: white;
            }
        """)

        card = QWidget()
        card.setObjectName("card")

        layout = QVBoxLayout(card)

        layout.setContentsMargins(
            16,
            12,
            16,
            12
        )

        layout.setSpacing(4)

        # -------------------------------------
        # TOP BAR
        # -------------------------------------

        top = QHBoxLayout()

        title = QLabel("KRITR")
        title.setObjectName("title")

        menu = QPushButton("···")

        menu.setFixedSize(
            30,
            25
        )

        top.addWidget(title)
        top.addStretch()
        top.addWidget(menu)

        layout.addLayout(top)

        # -------------------------------------
        # SONG
        # -------------------------------------

        self.song = QLabel(
            "Nothing playing"
        )

        self.song.setObjectName(
            "song"
        )

        self.artist = QLabel(
            "Drop some music here"
        )

        self.artist.setObjectName(
            "artist"
        )

        layout.addWidget(
            self.song
        )

        layout.addWidget(
            self.artist
        )

        # -------------------------------------
        # CONTROLS
        # -------------------------------------

        controls = QHBoxLayout()

        previous = QPushButton("‹")
        previous.setFixedSize(
            35,
            35
        )

        self.play = QPushButton("▶")

        self.play.setObjectName(
            "play"
        )

        self.play.setFixedSize(
            44,
            35
        )

        next_button = QPushButton("›")

        next_button.setFixedSize(
            35,
            35
        )

        controls.addStretch()

        controls.addWidget(
            previous
        )

        controls.addWidget(
            self.play
        )

        controls.addWidget(
            next_button
        )

        controls.addStretch()

        layout.addLayout(
            controls
        )

        # -------------------------------------
        # MAIN LAYOUT
        # -------------------------------------

        main_layout = QVBoxLayout(
            self
        )

        main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        main_layout.addWidget(
            card
        )

    # -----------------------------------------
    # DRAG WINDOW
    # -----------------------------------------

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.drag_position = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )

            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() & Qt.LeftButton:

            self.move(
                event.globalPosition().toPoint()
                - self.drag_position
            )

            event.accept()


# ---------------------------------------------
# START
# ---------------------------------------------

def main():

    app = QApplication(
        sys.argv
    )

    player = KritrPlayer()

    player.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()