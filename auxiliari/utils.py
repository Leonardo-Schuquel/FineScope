from colorama import Fore, Style, init
from datetime import datetime
import json
import os

init(autoreset=True)

def search_data():
    with open("data/data.json", 'r', encoding='utf-8') as file:
        release = json.load(file)

    return release

def event_color(event):
    return Fore.GREEN if event.lower() == 'entrada' else Fore.RED

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# create json in case the user does not have this file
def create_json():
    if not os.path.exists("data/data.json"):
        with open("data/data.json", "w") as file:
            json.dump({}, file)

# validates menu responses and handles errors
def validate_resp():
    try:
        resp = int(input('Escolha a partir dos indices uma operação a ser feita: '))
        return resp
    except (ValueError, UnboundLocalError):
        clear()
        print('Por favor, limitese aos indices')
        print(50 * '=')
        return -1

# 
def add_event(event):
    while True:
        try:
            value = float(input('Digite o valor: ').replace(',', '.'))
            clear()
            if value < 1:
                print('❌ Não são aceitos valores menores que R$1,00.')
                print(50 * '=')
                continue
            else:
                break
        except ValueError:
            clear()
            print('❌ Valor inválido. Digite um número válido.')
            print(50 * '=')
    
    while True:
        name_event = input('Qual é o nome do lançamento: ').strip()
        clear()
        if name_event and any(char.isalpha() for char in name_event):
            break # Sai do loop se for preenchido
        else:
            clear()
            print('❌ Esse campo é obrigatório e deve conter letras')
            print(50 * '=')

    annotations = input('Deseja fazer alguma anotação?(opcional): ')
    clear()
    date_time = datetime.now().strftime('%d/%m/%Y %H:%M')
    user_data = {
        'event': event,
        'value': value,
        'name_event': name_event,
        'annotation': annotations,
        'date_time': date_time,
    }
    return user_data

def show_launch(user_data):
    color = event_color(user_data['event'])

    print(50 * '=')
    print('Lançamento efetuado com sucesso')
    print(50 * '=')

    print(f'{color}Evento -> {user_data["event"]}{Style.RESET_ALL}')
    print(f'Nome do Lançamento -> {user_data["name_event"]}')
    print(f'Valor -> {color} R$ {user_data["value"]:.2f}{Style.RESET_ALL}')
    if user_data["annotation"]:
            print(f'{Fore.YELLOW}Anotação -> {user_data["annotation"]}{Style.RESET_ALL}')
    print(f'Data/Hora -> {user_data["date_time"]}')
    print(50 * '=')
    print()

    input('Pressione enter tecla para continuar ')
    clear()

# Save launches
def save_json(user_data):
    current_month = datetime.now().strftime('%m/%Y')

    if os.path.exists('data/data.json'):
        with open('data/data.json', 'r', encoding='utf-8')as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
    else: data = {}
    
    if current_month not in data:
        data[current_month] = [] # Check if you already have a record for the current month
    
    data[current_month].append(user_data)
    
    with open('data/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def show_current_month():
    clear()
    current_month = datetime.now().strftime('%m/%Y')
    releases = search_data()

    if current_month not in releases:
        print('Não há nenhum lançamento neste mes')
        print(50 * "=")
        input('Pressione enter para continuar')
        return

    print(f"{Fore.CYAN}📅 Lançamentos de {current_month}:{Style.RESET_ALL}")
    print(50 * '=')

    for i, item in enumerate(releases[current_month], start=1):
        color = event_color(item['event'])
        print(f"{i}-> {color} {item['name_event']} | {item['event']} | R$ {item['value']:.2f} | {item['date_time']}{Style.RESET_ALL}")
        if item['annotation']:
            print(f"{Fore.YELLOW}Anotação: {item['annotation']}{Style.RESET_ALL}")
        print(50 * '=')

# the next two functions are intended to list the releases of months prior to the current one
def show_month(selected_month):
    print(selected_month)
    clear()
    releases = search_data()

    for i, item in enumerate(releases[selected_month], start=1):
            color = event_color(item['event'])
            print(f"{i}-> {color} {item['name_event']} | {item['event']} | R$ {item['value']:.2f} | {item['date_time']}{Style.RESET_ALL}")
            if item['annotation']:
                print(f"{Fore.YELLOW}Anotação: {item['annotation']}{Style.RESET_ALL}")
            print(50 * '=')

    input('Pressione enter para continuar ')
    every_month()
    clear()
    
def every_month():
    clear()
    current_month = datetime.now().strftime('%m/%Y')
    releases = search_data()
    
    month_save = list(releases.keys())
    other_months = [month for month in month_save if month != current_month]
    index_other_months = len(other_months) + 1

    if not other_months:
        print('Não há registro de outros meses')
        print(50 * "=")
        input('Pressione enter para voltar. ')
        return
    
    print(50 * '=')
    for i, item in enumerate(other_months, start=1):
        print(f"[{i}] {item}")
    print(f"[{index_other_months}] Voltar ao Menu Anterior")
    print(50 * '=')

    resp = validate_resp()

    if resp == index_other_months:
        return
    elif 1 <= resp <= len(other_months):
        selected_month = other_months[resp - 1]
        show_month(selected_month)
    else:
        print('Indice invalido')
        print(50 * "=")
        input('Pressione enter para tentar novamente')
        every_month()

# excui releases of the current month
def dell_launch():
    clear()
    current_month = datetime.now().strftime('%m/%Y')
    releases = search_data()
    
    if current_month not in releases:
        print('Não há registro para serem excluidos')
        print(50 * '=')
        input('Pressione enter para voltar. ')
        return
    
    for i, item in enumerate(releases[current_month], start=1):
            color = event_color(item['event'])
            print(f"{i}-> {color} {item['name_event']} | {item['event']} | R$ {item['value']:.2f} | {item['date_time']}{Style.RESET_ALL}")
            if item['annotation']:
                print(f"{Fore.YELLOW}Anotação: {item['annotation']}{Style.RESET_ALL}")
            print(50 * '=')

    try:
        resp = int(input('Escolha a partir dos indices o lançamento que desaja excluir: '))
    except (ValueError, UnboundLocalError):
        clear()
        print('Por favor, limitese aos indices')
        print(50 * '=')
        input('Pressione Enter para voltar')
        return

    if 1 <= resp <= len(releases[current_month]):
        clear()
        confirms = input('Tem certeza que deseja excluir esse lançamento? (s/n): ').lower()

        if confirms in ['s', 'sim', '']:
            del releases[current_month][resp - 1]
            if not releases[current_month]:
                del releases[current_month]
            with open("data/data.json", "w") as file:
                json.dump(releases, file, indent=4, ensure_ascii=False)
            clear()
            print('✅ Lançamento excluído com sucesso!')
        else:
            clear()
            print('❌ Operação cancelada.')
    
    else:
        print('❌ Índice inválido.')
    
    print(50* "=")
    input('Pressione Enter para tentar novamente.')
    return