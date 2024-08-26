#Bibliotecas importadas
import requests 
from requests import RequestException
import tkinter as tk
from tk import *     


#Variavel "ano" & "mes" com função input() para perguntar ao usuário
ano = input('Digite o ano que voce deseja: ')
mes = input('Digite o mes que voce deseja: ')

#Link da API
link = f"https://brasilapi.com.br/api/feriados/v1/{ano}"

#Função definida linkchecker()
def leitorapi():
    try:
        
        r1 = requests.get(link)#Requisição da API
        convert = r1.json()#Coerção de tipo para JSON
        return convert#Retorna a coerção

    except  RequestException as e:#Tratativa de erros com Requests
        print(f"Ocorreu um erro{e}")

typeshow = leitorapi()#Variavel "typeshow" para printar a DEF


#Função definida chamada date()
def date():
    try: 
        for date in typeshow:#Verifica se contem "date" na requisição de typeshow
            data = date['date'].split('-')#Função split para dividir os items
            if data[1] == mes:#IF com data, para verificar se a um mês disponível
                print(f'{date['date']}: {date['name']}')#Print do nome do feriado que está no JSON
    except RequestException as e:#Trativa de erro com RequestsException
        return(f"Ocorreu um erro{e}")

date()



'''
def limpar():
    mes_entrada.delete(0, tk.END)
    ano_entrada.delete(0, tk.END)
    cal.delete(1.0, tk.END)


#Criar DEF para tratar o dado da API, e também criar um DEF para limpar os dados no GUI


#Janela principal - Para criar a tela
root = tk.Tk()
root.title("Feriados Nacionais")
janela = tk.Label(width=128, height= 32, bg="black", fg="white").pack()
janela = root.configure(bg="black")
mes_label = tk.Label( text="Mês", font=('Arial', '10', 'bold'),bg="black",fg='white')
mes_label.place(relx=0.2, rely=0.2)
mes = tk.IntVar()
mes_entrada = tk.Entry(textvariable=mes,justify="center")
mes_entrada.place(relx=0.3, rely=0.2, relwidth=0.1)
cal = tk.Text(width=33, height=8, relief="ridge", borderwidth=2)
cal.place(relx=0.4, rely=0.35)
ano_label = tk.Label( text="Ano", font=('Arial', '10', 'bold'),bg="black",fg='white')
ano_label.place(relx=0.5, rely=0.2)
ano = tk.IntVar()
ano_entrada = tk.Entry(textvariable=ano,justify="center")
ano_entrada.place(relx=0.6, rely=0.2, relwidth=0.15)
mostrarb = tk.Button( text="Mostrar", font=('verdana', 10, 'bold'), command=None)
mostrarb.place(relx=0.3,rely=0.85)
limparb = tk.Button( text="Limpar", font=('verdana', 10, 'bold'), command=limpar)
limparb.place(relx=0.5,rely=0.85)
exitb = tk.Button(root, text="Exit", font=('verdana', 10, 'bold'), command=exit)
exitb.place(relx=0.7,rely=0.85)
root.mainloop()
'''
#Decidimos deixar o Tkinter em docstring pois precisamos tirar dúvidas sobre ele