from auxiliari.utils import clear, event_color, search_data
from datetime import datetime
from colorama import Style, Fore

def cumulative_balance():
    release = search_data()
    positive = 0.0
    negative = 0.0

    for month in release:
        for item in release[month]:
            if item['event'] == 'Entrada':
                positive += item['value']
            else:
                negative += item['value']
    
    cumulative = positive - negative
    return cumulative

def entries():
    sum_entries = 0.0
    release = search_data() # pega o que tem no arquivo json inteiro
    current_month = datetime.now().strftime('%m/%Y')

    if not current_month in release:
        return 0.0

    for i, item in enumerate(release[current_month]):
        if item['event'] == 'Entrada':
            sum_entries += item['value']

    return sum_entries
    
def output():
    sum_output = 0.0
    release = search_data() # pega o que tem no arquivo json inteiro
    current_month = datetime.now().strftime('%m/%Y')

    if not current_month in release:
        return 0.0

    for i, item in enumerate(release[current_month]):
        if item['event'] == 'Saida':
            sum_output += item['value']

    return sum_output

def total_balance():
    positive = entries()
    negative = output()
    total = positive - negative
    color = Fore.GREEN if total >= 0 else Fore.RED
    
    print(f'O saldo total do mês é de: {color}R${total:.2f}{Style.RESET_ALL}')
    print(50 * '=')
    input('Pressione ENTER para continuar ')

def record_by_type(event_type: str):
    current_month = datetime.now().strftime('%m/%Y')
    release = search_data()
    clear()

    if current_month not in release:
        print("Não foram feitos registros nesse mês")
        return 0.0
    
    total = 0.0
    entries = []
    for item in release[current_month]:
        if item['event'] == event_type:
            color = event_color(item['event'])
            entries.append(f"{color}{event_type} | R$ {item['value']:.2f} | Titulo: {item['name_event']}")
            total += item['value']
    
    for line in entries:
        print(line)
    
    total_color = event_color(event_type)
    print(50 * "=")
    print(f"{total_color}O total de {event_type.lower()}s foi de R$ {total:.2f}")
    print(50 * '=')
    
    input("Pressione Enter para continuar")

def entries_list():
    release = search_data()
    current_month = datetime.now().strftime('%m/%Y')

    return [item for item in release.get(current_month, []) if item['event'] == 'Entrada']


def outputs_list():
    release = search_data()
    current_month = datetime.now().strftime('%m/%Y')

    return [item for item in release.get(current_month, []) if item['event'] == 'Saida']