from datetime import datetime as dt, timedelta
import random as rd, csv, json, math

fim = dt.now()
inicio = dt(2025, 10, 1, 00, 00, 00)

dados_csv= "dados/dados.csv"
dados_json= "dados/dados.json"
consumo_acima_5GB_txt = "logs/consumo_acima_5GB.txt"
consumo_txt = "logs/consumo.txt"
log_txt = "logs/logs.txt"


class Cliente:
    def __init__(self):

        lista_de_nomes = ["Leonel dos Anjos", "Carlos Manuel", "Pedro Almeida", "João Batista", "Miguel Ferreira",
        "André Santos", "Rui Pereira", "Fábio Costa", "Daniel Rocha", "Tiago Martins",
        "Lucas Nogueira", "Bruno Lopes", "Samuel Teixeira", "Henrique Pacheco", "Paulo Ribeiro",
        "Victor Moreira", "Eduardo Fonseca", "Matheus Barros", "Alexandre Neves", "Ricardo Cunha",
        "Nelson Araujo", "Jorge Macedo", "Wilson Correia", "António Figueiredo", "Guilherme Tavares",
        "Marcos Pinheiro", "Ivan Mendonça", "Flávio Cardoso", "Cristiano Rangel", "Sérgio Coelho",
        "Adriano Borges", "Hélio Monteiro", "Emanuel Viana", "Diogo Guedes", "Rafael Lemos",
        "Oscar Brito", "Leandro Paixão",
        "Roberto Peixoto", "Diego Siqueira", "Alan Freitas", "Fernando Assunção", "Vasco Morais",
        "Kelvin Matos", "Igor Falcão", "Natanael Cruz", "Pablo Rezende", "José Andrade"]
        ID = 0
        dados_dos_clientes = []
        for i in lista_de_nomes:
            nome = rd.choice(lista_de_nomes)
            consumo_diario = rd.randint(1, 20480)
            data = (dt.fromtimestamp(rd.randint(int(inicio.timestamp()), int(fim.timestamp()))).strftime("%d/%m/%Y %H:%M:%S"))

            ID += 1
            dados_dos_clientes.append({
                "ID": ID,
                "Nome": nome,
                "Consumo diario(MB)": consumo_diario,
                "Data": data
            })

        SistemaConsumo().armazenar_dados(dados_dos_clientes)
        SistemaConsumo().consumo()

class SistemaConsumo:
    def __init__(self):
        pass

    def armazenar_dados(self, dados_dos_clientes):
     
        with open(dados_json, "w", encoding="utf-8") as arquivo:
            json.dump(dados_dos_clientes, arquivo, indent=4)
            

        coluna = ["ID", "Nome", "Consumo diario(MB)", "Data"]
        with open(dados_csv, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=coluna)
            f.seek(0, 2)
            if f.tell() == 0:
                escritor.writeheader()
            escritor.writerows(dados_dos_clientes) 

    def limpar_dados(self):
        dados_dos_clientes = []
        self.armazenar_dados(dados_dos_clientes)

    def carregar_dados(self):
        with open(dados_json, "r") as f:
            lista = json.load(f)
        return lista

    def consumo(self):
        dados = self.carregar_dados()
        consumo = []
        consumo_max = []
        for lista in dados:
            consumo.append(lista["Consumo diario(MB)"])
            if lista["Consumo diario(MB)"] > 5120:
                consumo_max.append(f"{lista["Nome"]}, consome diariamente {lista["Consumo diario(MB)"]}MB |Data da actualizacao: {fim.strftime("%d/%m/%Y %H:%M:%S")}\n")
        self.consumo_max(consumo_max)

        consumo_total = f"Consumo minimo diario por usuario {min(consumo)}MB, \nConsumo medio diario por usuario {int(sum(consumo) / len(consumo))}MB \nConsumo maximo diario por usuario {max(consumo)}MB"
        with open(consumo_txt, "w") as arquivo:
            arquivo.writelines(consumo_total)

    def consumo_max(self, consumo_max):
        with open(consumo_acima_5GB_txt, "w") as arquivo:
            arquivo.writelines(consumo_max)
    
    def logs(self):
        with open(log_txt, "a") as arquivo:
            arquivo.write(f"Data de execucao do codigo {fim}\n")


