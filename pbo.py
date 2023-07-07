import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QDateEdit, QPushButton, QVBoxLayout, QRadioButton, QMessageBox, QGroupBox, QHBoxLayout
from PyQt5.QtCore import QDate

class InputForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Form Data Mahasiswa')
        self.setGeometry(300, 300, 300, 200)
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        self.name_label1 = QLabel('FORM DATA MAHASISWA')
    
        self.name_label = QLabel('Nama:')
        self.name_input = QLineEdit()

        self.birth_label = QLabel('Tanggal Lahir:')
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())

        self.program_label = QLabel('Prodi:')
        self.program_input = QLineEdit()

        self.gender_label = QLabel('Jenis Kelamin:')
        self.gender_group = QGroupBox()

        self.male_radio = QRadioButton('Laki-Laki')
        self.female_radio = QRadioButton('Perempuan')

        self.button_submit = QPushButton('Submit')
        self.button_cancel = QPushButton('Batal')

        layout.addWidget(self.name_label1)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.birth_label)
        layout.addWidget(self.date_edit)
        layout.addWidget(self.program_label)
        layout.addWidget(self.program_input)
        layout.addWidget(self.gender_label)

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        self.gender_group.setLayout(gender_layout)
        layout.addWidget(self.gender_group)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_submit)
        button_layout.addWidget(self.button_cancel)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.button_submit.clicked.connect(self.show_output)
        self.button_cancel.clicked.connect(self.close)

    def show_output(self):
        try:
            name = self.name_input.text()
            if not name.isalpha():
                raise ValueError("Nama hanya boleh berisi huruf.")
            
            birth = self.date_edit.text()
            program = self.program_input.text()
            if not program.isalpha():
                raise ValueError("Prodi hanya boleh berisi huruf.")

            gender = 'Laki-Laki' if self.male_radio.isChecked() else 'Perempuan'

            output = f'Nama: {name}\nTanggal Lahir: {birth}\nProdi: {program}\nJenis Kelamin: {gender}'

            QMessageBox.information(self, 'Output', output)
        except ValueError as e:
            QMessageBox.critical(self, 'Error', str(e))
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Terjadi kesalahan: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = InputForm()
    form.show()
    sys.exit(app.exec_())
