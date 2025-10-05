from PySide6.QtCore import Qt, QRegularExpression
from ui_window import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, 
                    QHeaderView, QAbstractItemView, QMessageBox, QButtonGroup)
from manager import Management
from PySide6.QtGui import QRegularExpressionValidator, QFont, QColor
from datetime import datetime
import sys
import utils
import report

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.selected_row = None

        self.list_edit_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #type: ignore
        self.historical.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #type: ignore

        nav_buttons = [
        self.btn_home,
        self.btn_release,
        self.btn_edit,
        self.btn_history
        ]

        # 1) marque-os como checkable
        for b in nav_buttons:
            b.setCheckable(True)

        # 2) crie um QButtonGroup para garantir exclusividade mesmo que os widgets tenham parents diferentes
        self._nav_group = QButtonGroup(self)
        self._nav_group.setExclusive(True)
        for b in nav_buttons:
            self._nav_group.addButton(b)

        # opcional: defina o botão inicial como ativo (ex.: Home)
        self._setActiveButton(self.btn_home)

        fonte = QFont()
        fonte.setPointSize(12)
        self.list_edit_2.setFont(fonte)
        self.historical.setFont(fonte)
        self.list_edit_2.verticalHeader().setDefaultSectionSize(30)
        self.historical.verticalHeader().setDefaultSectionSize(30)

        
        self.list_edit_2.setSelectionBehavior(QAbstractItemView.SelectRows) #type: ignore
        self.list_edit_2.setSelectionMode(QAbstractItemView.SingleSelection) #type: ignore

        self.list_edit_2.itemSelectionChanged.connect(self.onRowSelected)

        regex = QRegularExpression(r"^\d+([.,]\d{1,2})?$")  
        validator = QRegularExpressionValidator(regex)

        self.value_release.setValidator(validator)
        self.value_release_2.setValidator(validator)


        self.setWindowTitle('FineScope')

        self.balanceEntryText("Entrada", self.value_balance)
        self.balanceEntryText("Saida", self.value_debts)
        self.totalBalance()

        # Linking buttons to corresponding methods
        self.btn_home.clicked.connect(self._callHome)
        self.btn_release.clicked.connect(lambda: (self._callPage(self.page_release),
                                          self._setActiveButton(self.btn_release)))
        self.btn_edit.clicked.connect(lambda: (self._openEditPage(),
                                       self._setActiveButton(self.btn_edit)))
        self.btn_quit.clicked.connect(self.close)
        self.save.clicked.connect(self.saveRelease)
        self.btn_edit_2.clicked.connect(self._openEditRelease)
        self.edit_save.clicked.connect(self._saveEditRelease)
        self.cancel.clicked.connect(self.cancel_save)
        self.last_month.clicked.connect(lambda: self.loadCurrentMonth(self.historical))
        self.btn_history.clicked.connect(self._viewHistorical)
        self.last_month.clicked.connect(self._viewLastMonth)
        self.entrance_historical.clicked.connect(self._viewEntrance)
        self.departure_historical.clicked.connect(self._viewOutgoing)
        self.btn_exclude.clicked.connect(self.delletingRelease)
        self.exclude.clicked.connect(self._excludeRelease)
        self.btn_pdf.clicked.connect(self._generatePDF)

    def _callHome(self):
        self._callPage(self.page_home)
        self.balanceEntryText("Entrada", self.value_balance)
        self.balanceEntryText("Saida", self.value_debts)
        self.totalBalance()
        self._setActiveButton(self.btn_home)   

    def balanceEntryText(self, prefix, pathLabel):
        entry = utils.balance(prefix)

        textEntry = f"R${entry}"
        pathLabel.setText(textEntry)

    def totalBalance(self):
        total = utils.total_balance()
        textTotal = f"R${total}"

        if float(total) >= 0:
            self.sum_release.setStyleSheet("color: #11e000; font-size: 30px;" \
            " font-weight: 600;")
        elif float(total) < 0:
            self.sum_release.setStyleSheet("color: #ff0303; font-size: 30px;" \
            " font-weight: 600;")

        self.sum_release.setText(textTotal)

    def cancel_save(self):
        self.clear()
        self._callPage(self.page_home)

    def _callPage(self, page):
        self.pages.setCurrentWidget(page)

    def _collectReleaseData(self, prefix=""):
        """Coleta e valida os dados da tela. prefix='' para criação, '_2' para edição"""
        title = getattr(self, f"input_title{prefix}").text().strip()
        value_widget = getattr(self, f"value_release{prefix}")
        value = value_widget.text().replace(',', '.')
        description = getattr(self, f"description_release{prefix}").text().strip()

        try:
            value = float(value)
        except ValueError:
            print('valor invalido')
            return
        
        if not title:
            print("O título é obrigatório!")  # depois vira QMessageBox
            return

        if not description.strip():
            description = None

        entrance = getattr(self, f'entrance{prefix}')
        departure = getattr(self, f'departure{prefix}')

        if entrance.isChecked():
            event = "Entrada"
        elif departure.isChecked():
            event = "Saida"
        else:
            print('Selecione uma saida')
            return
        
        return Management(event, value, title, description)

    def clear(self):
        self.input_title.clear()
        self.value_release.clear()
        self.description_release.clear()

        self.entrance.setAutoExclusive(False)
        self.departure.setAutoExclusive(False)

        self.entrance.setChecked(False)
        self.departure.setChecked(False)

        self.entrance.setAutoExclusive(True)
        self.departure.setAutoExclusive(True)

    def saveRelease(self):
        
        release = self._collectReleaseData()
        if release:
            data = release.collecting()
            release.save(data)

        self.clear()

    def delletingRelease(self):
        if not hasattr(self, 'selected_id') or self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Nenhum lançamento selecionado")
            return
        
        reply = QMessageBox.question(
            self, 
            "Confirmar exclução", 
            "Tem certeza que deseja excluir esse lançamento?", 
            QMessageBox.Yes | QMessageBox.No # type: ignore
        )

        if reply != QMessageBox.Yes: # type: ignore
            return
        
        success = Management.delRelease(self.selected_id)

        if success:
            QMessageBox.information(self, 'Sucesso', "Lançamento excluido com sucesso")
            self.loadCurrentMonth(self.list_edit_2)
            self.selected_id = None
            self.selected_row = None

    def _openEditPage(self):
        self.loadCurrentMonth(self.list_edit_2)
        self._callPage(self.list_edit)

    def _viewHistorical(self):
        self.loadHistorical()
        self._callPage(self.page_historical)
        self._setActiveButton(self.btn_history)

    def _viewLastMonth(self):
        currentMonth = datetime.now().strftime("%m/%Y")
        self.loadHistorical(month=currentMonth)
        self._callPage(self.page_historical)

    def _viewEntrance(self):
        self.loadHistorical(event="Entrada")
        self._callPage(self.page_historical)

    def _viewOutgoing(self):
        self.loadHistorical(event="Saida")
        self._callPage(self.page_historical)

    def loadCurrentMonth(self, _list):
        releases = Management.getCurrentMonth()

        _list.clearContents()
        _list.setRowCount(len(releases))  # type: ignore

        columns = ['id', 'event', 'title', 'value', 'date_time']

        for row, release in enumerate(releases):  # type: ignore

            for col, key in enumerate(columns):
                item = QTableWidgetItem(str(release.get(key, "")))

                if key == 'id':
                    item.setData(Qt.UserRole, release.get('id')) # type: ignore
                
                if release.get("event") == "Entrada":
                    item.setForeground(QColor("lightgreen"))
                else:
                    item.setForeground(QColor("salmon"))

                _list.setItem(row, col, item)

    def populateHistorical(self, table_widget, launches, columns=None):
        if columns is None:
            columns = ['id', 'event', 'title', 'value', 'date_time']

        table_widget.clearContents()
        table_widget.setRowCount(len(launches))

        for row, launch in enumerate(launches):
            for col, key in enumerate(columns):
                item = QTableWidgetItem(str(launch.get(key, '')))

                if key == 'id':
                    item.setData(Qt.UserRole, launch.get('id')) #type: ignore

                if launch.get("event") == "Entrada":
                    item.setForeground(QColor("lightgreen"))
                else:
                    item.setForeground(QColor("salmon"))

                self.historical.setItem(row, col, item)

    def loadHistorical(self, month=None, event=None):
        releases = utils.loadJson()
        all_launches = []

        for m, launches in releases.items():
            if month and m != month:
                continue
            for l in launches:
                if event and l.get("event") != event:
                    continue
                all_launches.append(l)
        
        self.populateHistorical(self.historical, all_launches)

    def onRowSelected(self):
        selected = self.list_edit_2.selectedItems()
        if selected:
            row = selected[0].row()
            id_item = self.list_edit_2.item(row, 0)
            if id_item:
                select_id = id_item.data(Qt.UserRole) # type: ignore
                self.selected_row = row
                self.selected_id = select_id
               
    def _openEditRelease(self):
        if not hasattr(self, 'selected_id') or self.selected_id is None:
            print("Nenhum lançamento selecionado.")
            return

        releases = Management.getCurrentMonth()
        release_to_edit = next((r for r in releases if r['id'] == self.selected_id), None)

        if release_to_edit:
            print("Carregando lançamento:", release_to_edit)  # debug
            self.input_title_2.setText(release_to_edit.get("title", ""))
            self.value_release_2.setText(str(release_to_edit.get("value", "")))
            self.description_release_2.setText(release_to_edit.get("description", ""))

            if release_to_edit.get("event") == "Entrada":
                self.entrance_2.setChecked(True)
            else:
                self.departure_2.setChecked(True)

            # 🚀 Importante: trocar a página no QStackedWidget interno
            self._callPage(self.edit)

    def _saveEditRelease(self):
        if not hasattr(self, 'selected_id') or self.selected_id is None:
            print("Vou trocar isso")
            return
        
        release = self._collectReleaseData("_2")
        if release:
            release.edit_release(self.selected_id)
            print("Edição salva") # Também vou mudar isso
            self.loadCurrentMonth(self.list_edit_2)
            self._callPage(self.list_edit)

    def _excludeRelease(self):
        release_id = getattr(self, 'selected_id', None)
        if release_id is None:
            return

        reply = QMessageBox.question(
        self,
        "Confirmar exclusão",
        "Tem certeza que deseja excluir esse lançamento?",
        QMessageBox.Yes | QMessageBox.No #type: ignore
    )

        if reply != QMessageBox.Yes: #type: ignore
            return

        # Chama a função de exclusão do financial
        success = Management.exclude_release(release_id)

        if success:
            QMessageBox.information(self, "Sucesso", "Lançamento excluído com sucesso")
            self._callPage(self.list_edit)
            self.loadCurrentMonth(self.list_edit_2)  # Atualiza a tabela
            self.selected_id = None
            self.selected_row = None

    def _generatePDF(self):
        try:
            caminho = report.gen_financial_pdf()
            QMessageBox.information(self, "Sucesso", f"PDF gerado em:\n{caminho}")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao gerar o PDF:\n{str(e)}")

    def _setActiveButton(self, active_button):
        """Ativa apenas o botão selecionado (checa ele e descheca os outros)."""
        # lista explícita para evitar depender de ordem externa
        nav_buttons = [
            self.btn_home,
            self.btn_release,
            self.btn_edit,
            self.btn_history
        ]
        for btn in nav_buttons:
            # setChecked é suficiente — o QButtonGroup garante exclusividade
            btn.setChecked(btn is active_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec()