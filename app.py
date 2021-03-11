from PyQt5 import uic, QtWidgets


#
# INIT VARIAVEIS
#

style_line_edit_ok = ("QLineEdit{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255,207,0);\n"
"}")

# Error

style_line_edit_error = ("QLineEdit{\n"
"    border: 2px solid rgb(255,85,127);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255,207,0);\n"
"}")

# TEXT EDIT

style_text_edit_ok = ("QTextEdit{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255,207,0);\n"
"}")


style_text_edit_error = ("QTextEdit{\n"
"    border: 2px solid rgb(255,85,127);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255,207,0);\n"
"}")

# STYLE POPUP

style_popup_error = ("background-color: rgb(239, 41, 41); border-radius: 10px;")

style_popup_ok = ("background-color: rgb(0, 255, 123); border-radius: 10px;")


#
# INIT FUNCTIONS
#

# Fechar a msg de popup
def close_popup_x():
    home.frame_error.hide()

# Checar se todos os campos estão preenchidos
def generate_txt():
    name_project = home.lineEdit_name.text()
    language_progamming = home.lineEdit_language.text()
    date = home.lineEdit_date.text()
    description = home.textEdit_description.toPlainText()

    #Exibindo a mensagem de erro ou sucesso
    def show_message(message):
        home.frame_error.show()
        home.label_error.setText(message)

    #Field 1
    if not home.lineEdit_name.text():
        name_project = "Name Empyt "
        home.lineEdit_name.setStyleSheet(style_line_edit_error)
    else:
        name_project = ""

    #Field 2
    if not home.lineEdit_language.text():
        language_progamming = "Language Empyt "
        home.lineEdit_language.setStyleSheet(style_line_edit_error)
    else:
        language_progamming = ""

    #Field 3
    if not home.lineEdit_date.text():
        date = "Date Empyt "
        home.lineEdit_date.setStyleSheet(style_line_edit_error)
    else:
        date = ""

    #Field 4
    if not home.textEdit_description.toPlainText():
       description = "Description Empyt"
       home.textEdit_description.setStyleSheet(style_text_edit_error)
    else:
        description = ""

    # Message 
    if name_project + language_progamming + date + description != '':
        text = name_project + language_progamming + date + description
        show_message(text)
        home.frame_error.setStyleSheet(style_popup_error)
    else:
        text = " Dados gerados com Sucesso!"
        show_message(text)
        home.frame_error.setStyleSheet(style_popup_ok)
        
        #Gera o arquivo txt
        name_project = home.lineEdit_name.text()
        language_progamming = home.lineEdit_language.text()
        date = home.lineEdit_date.text()
        description = home.textEdit_description.toPlainText()

        # Mascara do arquivo txt
        generate_data = "Nome do Projeto: " +name_project+ "\n""\n" "Linguagem de Programação: " +language_progamming+ "\n""\n" "Data: " +date+"\n""\n" "Descrição do Projeto: " +description
        
        # Funcionalidade que escolhe o diretorio que salva o arquivo
        file_txt = QtWidgets.QFileDialog.getSaveFileName()[0]
        
        # Criando o arquivo txt
        with open(file_txt + '.txt', 'w') as file_saved:
            file_saved.write(str(generate_data) + '\n')
            file_saved.close()
        

        # lIMPAR OS CAMPOS AṔOS SALVAR OS ARQUIVOS
        home.lineEdit_name.setText("")
        home.lineEdit_language.setText("")
        home.lineEdit_date.setText("")
        home.textEdit_description.setPlainText("")
        home.frame_error.hide()
     
#
# END FUNCTIONS
#

# instancia
app = QtWidgets.QApplication([])

# Load da GUI
home = uic.loadUi("home.ui")

# Actions PushButtons
home.frame_error.hide()
home.close_popup.clicked.connect(close_popup_x)
home.pushButton_generate.clicked.connect(generate_txt)

# Executando a aplicação
home.show()
app.exec()