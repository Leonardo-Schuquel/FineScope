from auxiliari import clear, validate_resp, add_event, show_launch, save_json, show_current_month, every_month, dell_launch, create_json, record_by_type, cumulative_balance, total_balance, gen_financial_pdf, entries_list, outputs_list, full_balance
from colorama import Fore, Style

options = {
    1: 'Entrada',
    2: 'Saida',
    3: 'Registros',
    4: 'Encerrar Programa',
}

record_options = {
    1: 'Registros do Mês',
    2: 'Todos os Registros',
    3: 'Excluir Lançamento',
    4: 'Gerar Relatório',
    5: 'Voltar ao Menu Anterior',
}

balance_options = {
    1: 'Todos os registros',
    2: 'Registros de entrada',
    3: 'Registros de saida',
    4: 'Voltar ao menu anterior'
}

def balance_menu():
    while True:
        clear()
        print(50 * '=')
        for i, item in balance_options.items():
            print(f'[{i}]', item)
        print(50 * '=')

        resp = validate_resp()

        if resp == 1:
            show_current_month()
            total_balance()
        elif resp == 2:
            record_by_type('Entrada')
        elif resp == 3:
            record_by_type('Saida')
        elif resp == 4:
            break
        else:
            clear()
            print('Indice invalido')
            print(50 * '=')

def menu_record():
    while True:
        clear()
        print(50 * '=')
        for i, item in record_options.items():
            print(f'[{i}]', item)
        print(50 * '=')

        resp = validate_resp()

        if resp == 1:
            balance_menu()
        elif resp == 2:
            every_month()
        elif resp == 3:
            dell_launch()
        elif resp == 4:
            clear()
            gen_financial_pdf(entries_list(), outputs_list(), cumulative_balance())
            input("Pressione ENTER para continuar ")
        elif resp == 5:
            clear()
            return
        else:
            clear()
            print('Indice invalido')
            print(50 * '=')

while True:
    create_json()
    balance = full_balance()
    color = Fore.GREEN if balance >= 0 else Fore.RED
    clear()
    print(f'Saldo atual: {color}R$ {balance:.2f}{Style.RESET_ALL}')
    print(50 * "=")
    for i, item in options.items():
        print(f'[{i}]', item)
    print(50 * '=')

    resp = validate_resp()

    if resp == 1 or resp == 2:
        clear()
        user_data = add_event(options[resp])
        show_launch(user_data)
        save_json(user_data)
    elif resp == 3:
        menu_record()
    elif resp == 4:
        break
    else:
        clear()
        print('Indice invalido')
        print(50 * '=')