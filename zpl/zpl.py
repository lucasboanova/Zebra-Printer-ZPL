from models.modelZpl import ZplModel
import logging

class ZplFile():
    """Classe para manipulação de arquivos ZPL."""
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w', encoding='utf-8')
        logging.info(f"Opened file for writing: {filename}")

    def write(self, data):
        """Escreve dados no arquivo."""
        self.file.write(data)
        logging.info(f"Wrote data to file: {data}")

    def close(self):
        """Fecha o arquivo."""
        self.file.close()
        logging.info(f"Closed file: {self.filename}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def generate_zpl_label(self, zplModel: ZplModel):
        """Gera a etiqueta ZPL com base no modelo fornecido."""
        zpl = (
            "^XA\n"
            "^FO32,288^GFA,05888,05888,00092,:Z64:\n"
            "^FT164,130^A0N,56,55^FH\\^FDDe: Dimed Matriz^FS\n"
            "^FT116,271^A0N,56,55^FH\\^FDPara: Panvel Filial ^FS\n"
            f"^FT548,271^A0N,56,55^FH\\^FD{zplModel.branch}^FS\n"
            "^FT181,371^A0N,56,55^FH\\^FDTurno: ^FS\n"
            f"^FT366,371^A0N,56,55^FH\\^FD{zplModel.turn}^FS\n"
            "^FT181,471^A0N,56,55^FH\\^FDTipo: ^FS\n"
            f"^FT366,471^A0N,56,55^FH\\^FD{zplModel.typeTonner}^FS\n"
            "^FT181,551^A0N,56,55^FH\\^FDRampa: ^FS\n"
            f"^FT366,551^A0N,56,55^FH\\^FD{zplModel.ramp}^FS\n"
            "^FT203,689^A0N,56,55^FH\\^FDA\\1FC: Resp. Filial^FS\n"
            "^FO32,46^GB732,711,8^FS\n"
            "^FO41,573^GB717,0,12^FS\n"
            "^FO34,163^GB730,0,12^FS\n"
            "^PQ1,0,1,Y^XZ"
        )
        self.write(zpl)
        logging.debug(f"Generated ZPL label: {zpl}")
        return zpl