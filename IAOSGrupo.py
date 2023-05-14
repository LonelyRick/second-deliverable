from grobid_client.grobid_client import GrobidClient
import matplotlib.pyplot as plt
import re
import pathlib
import sys
import os


# Creamos el cliente
grobid_client = GrobidClient("http://localhost:8070")


# Obtener la ruta donde estan los pdfs
ruta = sys.argv[1]


# Crear y abrir los fichero de salida  en modo de escritura
archivoTitulos = open(os.path.join(os.getcwd(), "orden.txt"), "w")
archivoAbstract = open(os.path.join(os.getcwd(), "abstracts.txt"), "w")
archivoAcknowledges = open(os.path.join(os.getcwd(), "acknowledges.txt"), "w")

# Obtenemos el directorio con los articulos
directorio = pathlib.Path(ruta)

# Recorremos el directorio
for fichero in directorio.iterdir():



    response = grobid_client.process_pdf("processFulltextDocument", str(fichero), generateIDs=False,
                                     consolidate_header=False, consolidate_citations=False,
                                     include_raw_citations=False, include_raw_affiliations=False,
                                     tei_coordinates=False, segment_sentences=False)
    texto = str(response)

    # Verificar si la respuesta es correcta
    if response[1]==200:

        print("Codigo HTTP ",response[1])

        title1 = texto[texto.find("<titleStmt>"):]
        title = title1[title1.find("<title level=" + '"' + "a" + '"' + " " + "type=" + '"' "main" + '"' + ">") + len("<title level=" + '"' + "a" + '"' + " " + "type=" + '"' "main" + '"' + ">"):title1.find("</title>")]
        archivoTitulos.write(title + "\n")
        # Obtener informacion abstracta
        abstract = texto[texto.find("<abstract>"):]
        abstract = abstract[abstract.find("<p>") + len("<p>"):abstract.find("</p>")]
        archivoAbstract.write(abstract + "\n" + "---" + "\n")

        # Obtener Acknowledges
        ack = texto[texto.find('<div type="acknowledgement">'):]
        ack = ack[ack.find("<p>") + len("<p>"):ack.find("</p>")]
        archivoAcknowledges.write(ack + "\n" + "---" + "\n")

    else:
        print("Codigo HTTP ", response[1])

