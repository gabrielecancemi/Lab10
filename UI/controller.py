import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._partenza = None

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        anno = self._view._txtAnno.value
        if anno is None or anno == "":
            self._view._txt_result.controls.append(ft.Text("Inserire un anno", color="red"))
            self._view.update_page()
            return
        try:
            anno = int(anno)
        except:
            self._view._txt_result.controls.append(ft.Text("Inserire un anno intero", color="red"))
            self._view.update_page()
            return

        if anno < 1816 or anno > 2016:
            self._view._txt_result.controls.append(ft.Text("Inserire un anno tra 1816 e 2016", color="red"))
            self._view.update_page()
            return

        nodi = self._model.createGraph(anno)
        self._view._txt_result.controls.append(ft.Text(f"Creato grafo con {self._model.conComponents()} componenti connesse", color="green"))
        for n in nodi:
            self._view._txt_result.controls.append(ft.Text(f"{n[0]} -- GRADO: {n[1]}"))

        self.fillDD(nodi)

        self._view.update_page()

    def handleCerca(self, e):
        self._view._txt_result.controls.clear()
        if self._partenza is None:
            self._view._txt_result.controls.append(ft.Text("Inserire uno stato di partenza", color="red"))
            self._view.update_page()
            return


        nodi = self._model.statiRaggiungibili(self._partenza)
        self._view._txt_result.controls.append(
            ft.Text(f"Nodi raggiungibili da {self._partenza} ({len(nodi)}):", color="green"))
        for n in nodi:
            self._view._txt_result.controls.append(ft.Text(f"{n}"))

        nodi = self._model.statiRaggiungibili2(self._partenza)
        self._view._txt_result.controls.append(
            ft.Text(f"Nodi raggiungibili da {self._partenza} ({len(nodi)}):", color="orange"))
        for n in nodi:
            self._view._txt_result.controls.append(ft.Text(f"{n}"))

        self._view.update_page()

    def fillDD(self, nodi):
        for n in nodi:
            self._view._ddStato.options.append(ft.dropdown.Option(text=n[0], data=n[0], on_click=self.salva))

    def salva(self, e):
        self._partenza = e.control.data