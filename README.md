<<<<<<< HEAD
# 💸 FinScope

**FinScope** é um organizador de finanças pessoais desenvolvido em Python com foco em controle simples e visual de entradas, saídas e saldos mensais. O projeto é modular e pensado para ser usado via terminal por enquanto, com geração automática de relatórios financeiros em PDF.

Este projeto tem como objetivo fornecer uma ferramenta simples e funcional para o gerenciamento consciente das finanças pessoais.

---

## 🚀 Funcionalidades Implementadas

- ✅ Registro de **entradas** e **saídas** com:
  - Valor
  - Nome do evento
  - Anotação opcional
  - Data e hora automáticas
- Histórico mensal de lançamentos
- Cálculo de **saldo do mês** e **saldo acumulado**
- Geração de **relatório financeiro em PDF** com design profissional
- Organização por mês (formato `mm/aaaa`)
- Destaque em cores:
  - Verde para saldo positivo ou entradas
  - Vermelho para saldo negativo ou saídas
- Exclusão de lançamentos do mês atual
- Interface por linha de comando (CLI)
- Modularização em pacotes Python (`financial.py`, `report.py`, etc.)

---

## 🚀 MVP Finalizado

Este repositório contém o MVP (Produto Mínimo Viável) pronto. O próximo passo será o desenvolvimento de uma **interface gráfica** utilizando **Django**.

---

## 🗂️ Estrutura de Diretórios

```
FineScope/
├── main.py
├── auxiliari/
│   ├── financial.py
│   ├── report.py
├── pdf/
├── dist/
├── build/
=======
# 💼 FineScope

**FineScope** é uma aplicação de **gestão financeira pessoal** desenvolvida em **Python**, com foco em **simplicidade, visualização de dados e geração de relatórios automáticos em PDF**.  
O sistema permite acompanhar receitas, despesas e o saldo mensal de forma prática, oferecendo uma visão clara da sua saúde financeira.

---

## 🚀 Funcionalidades

- 📊 **Visualização de dados**: exibe gráficos e resumos mensais.  
- 💰 **Cálculo de saldo automático**: o saldo atual é baseado no lucro ou prejuízo do mês anterior.  
- 🧾 **Geração de relatórios em PDF**: cria relatórios financeiros completos com apenas um clique.  
- 💡 **Interface amigável**: experiência intuitiva para qualquer nível de usuário.  
- 💾 **Armazenamento local em JSON**: seus dados são salvos de forma segura e independente.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Pyside6 + QtDesigner** (Para gerar a interface gráfica)
- **JSON** (Persistência de dados)
- **ReportLab** (Geração de PDFs)
- **PyInstaller** (Criação do executável para Windows)

---

## 💾 Download

Baixe o executável mais recente do FineScope:
👉 [Versão para Windows](https://github.com/seu-usuario/FineScope/releases/latest)
👉 [Versão para Linux](https://github.com/seu-usuario/FineScope/releases/latest)

## 📁 Estrutura do Projeto

```
FineScope/
├── src/
│   └── 
│   ├── main.py
│   ├── financial.py
│   ├── report.py
│   ├── utils.py
│   └── ...
├── window
│   └── window.ui
├── README.md
├── requirements.txt
└── LICENSE
>>>>>>> 0d2ca66 (First version of the MVP with graphical interface)
```

---

<<<<<<< HEAD
## 💼 Futuro

- Interface web com Django
- Cadastro de categorias de gastos
- Exportação para Excel ou CSV
- API RESTful para integração com apps móveis

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- **Colorama** — para aplicação de cores no terminal
- **JSON** — armazenamento local dos lançamentos
- **datetime** — manipulação de datas e horas

---

## 📌 Objetivos do Projeto

- Reforçar o aprendizado em Python, modularização, e manipulação de arquivos
- Criar uma ferramenta útil e funcional para controle financeiro pessoal
- Evoluir o sistema com futuras melhorias:
  - Exportação de relatórios em PDF
  - Geração de gráficos mensais



## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Leonardo-Schuquel/FineScope.git
   cd FinScope
   ```

2. Instale dependências, se houver:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

---

## 💡 Exemplos de uso

```
[1] Entrada
[2] Saída
[3] Registros
[4] Sair

Digite a opção: 1
Digite o valor: 100
Nome do lançamento: Salário
Anotação (opcional): Via Pix

✅ Lançamento efetuado com sucesso!
```

---

## 📄 Licença

Este projeto está licenciado sob a [Creative Commons BY-NC-SA 4.0](LICENSE.txt).  
Você pode usar, estudar e modificar o projeto para fins **não comerciais**, com atribuição. Para uso comercial, entre em contato com o autor.

---

## 👤 Autor

Desenvolvido por **Leonardo Schuquel** – 2025
Em desenvolvimento contínuo 🚀

---

## 🤝 Contato

- GitHub: [github.com/Leonardo-Schuquel](https://github.com/Leonardo-Schuquel)
- LinkedIn: [linkedin.com/in/leonardo-schuquel](www.linkedin.com/in/leonardoschuquel)
=======
## 📸 Exemplo de Relatório

O relatório em PDF inclui:
- Gráficos de receitas e despesas.
- Resumo do saldo mensal.
- Histórico de movimentações.
- Comparativo de meses anteriores.

---

## 🧠 Conceito

O FineScope foi projetado para unir **organização financeira** com **clareza visual**, ajudando o usuário a compreender onde seu dinheiro está sendo investido e qual o impacto de cada despesa.  
É o primeiro passo para **autonomia e educação financeira através da tecnologia**.

---

## 🧑‍💻 Autor

Desenvolvido com dedicação por **Leonardo Schuquel** 🧠  
📬 [linkedin.com/in/leonardoschuquel](https://www.linkedin.com/in/leonardoschuquel)

---

## 🪪 Licença

Este projeto é distribuído sob a licença **MIT**.  
Sinta-se livre para usar, modificar e contribuir.

---

⭐ **Dê uma estrela no repositório** se este projeto te ajudou ou inspirou!
>>>>>>> 0d2ca66 (First version of the MVP with graphical interface)
