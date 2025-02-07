import re

def resultados_Barrnap():
    # Abrir fichero gff de Barrnap
    input = open("Metagenome_hits.gff", "r")
    
    # Diccionario para almacenar la información relevante optenida
    dicc_barrnap = {}
    
    # Leer fichero gff y extraer los resultados
    for line in input:
        if line.startswith("#"):
            continue
        
        # Obtener el identificador de la secuencia (seqid)
        seqid = re.search("(.+)(?=\tbarrnap)", line).group(1)
        
        # Obtener los tipos de rrna encontrados en la secuencia
        if seqid not in dicc_barrnap:
            arn = []
            arn.append(re.search("(?<=Name=)(.+)(?=;product)", line).group(1))
        else:
            arn.append(re.search("(?<=Name=)(.+)(?=;product)", line).group(1))
        
        dicc_barrnap[seqid] = arn
    input.close()
    
    # Escribir resultados Barrnap en un tsv
    with open("Barrnap.tsv", "w") as out:
        out.write("seqid\trna_type\n")
        for key in dicc_barrnap.keys():
            for i in dicc_barrnap[key]:
                out.write(f"{key}\t{i}\n")


def resultados_Kraken2():
    input = open("kraken.txt", "r")


def main():
    # Analizar resultados de Barrnap
    resultados_Barrnap()
    
    # Analizar resultados de Kraken
    
    return 0


if __name__ == "__main__":
    main()
