
from datetime import datetime


def validar_data(data):

    try:

        data_convertida = datetime.strptime(data, "%d/%m/%Y")

        return data_convertida.strftime("%Y-%m-%d")

    except ValueError:

        raise ValueError("Data inválida. Utilize DD/MM/AAAA.")
