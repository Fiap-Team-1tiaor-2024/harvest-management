import oracledb
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk
import json

# Configurações para conexão com Oracle Database
dsn_tns = oracledb.makedsn('localhost', '1521', service_name='xe')
conexao = None

def conectar_ao_banco():
    global conexao
    try:
        conexao = oracledb.connect(user='rm560453', password="010790", dsn='oracle.fiap.com.br:1521/ORCL')
        print("Conexão com Oracle estabelecida com sucesso.")
    except oracledb.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados Oracle: {e}")
        conexao = None
        messagebox.showerror("Erro de Conexão", "Erro ao conectar ao banco de dados Oracle. Verifique as credenciais e tente novamente.")

conectar_ao_banco()

# Lista para armazenar os campos e seus dados
campos = []

# Função para adicionar um campo à tabela no banco de dados Oracle
def adicionar_campo_interface():
    """
    Adiciona um novo campo à tabela de campos no banco Oracle.
    """
    if not conexao:
        conectar_ao_banco()
        if not conexao:
            return

    nome = entry_nome.get()
    area_ha = entry_area_ha.get()
    produtividade_estimada = entry_produtividade.get()
    data_colheita = entry_data_colheita.get()
    maquinas_alocadas = entry_maquinas.get()
    custo_fixo = entry_custo_fixo.get()
    
    if not nome or not area_ha or not produtividade_estimada or not data_colheita or not maquinas_alocadas:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return
    
    try:
        area_ha = float(area_ha)
        produtividade_estimada = float(produtividade_estimada)
        custo_fixo = float(custo_fixo)
    except ValueError:
        messagebox.showerror("Erro", "Alguns campos numéricos não possuem valores válidos.")
        return
    
    try:
        # Verificando e convertendo a data estimada de colheita para o formato correto
        data_colheita = datetime.strptime(data_colheita.strip(), "%d-%m-%Y")
    except ValueError:
        messagebox.showerror("Erro", "Data de colheita inválida. Use o formato dd-mm-yyyy.")
        return

    # Inserir no Banco de Dados
    try:
        cursor = conexao.cursor()
        sql = """
            INSERT INTO campos_agro (nome, area_ha, produtividade_estimada, data_colheita, maquinas_alocadas, custo_fixo)
            VALUES (:1, :2, :3, TO_DATE(:4, 'DD-MM-YYYY'), :5, :6)
        """
        cursor.execute(sql, (nome.strip(), area_ha, produtividade_estimada, data_colheita.strftime("%d-%m-%Y"), maquinas_alocadas, custo_fixo))
        conexao.commit()
        messagebox.showinfo("Sucesso", f"Campo '{nome}' adicionado ao banco de dados com sucesso!")
        cursor.close()
    except oracledb.DatabaseError as e:
        messagebox.showerror("Erro", f"Erro ao inserir dados no banco de dados: {e}")

    atualizar_resultados()
    limpar_campos()
    salvar_campos_em_arquivo()

# Função para limpar os campos de entrada após adicionar
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_area_ha.delete(0, tk.END)
    entry_produtividade.delete(0, tk.END)
    entry_data_colheita.delete(0, tk.END)
    entry_maquinas.delete(0, tk.END)
    entry_custo_fixo.delete(0, tk.END)

# Função para salvar os dados dos campos em um arquivo JSON
def salvar_campos_em_arquivo():
    """
    Salva os dados dos campos em um arquivo JSON para persistência.
    """
    dados = []
    for campo in campos:
        dados.append({
            "nome": campo['nome'],
            "area_ha": campo['area_ha'],
            "produtividade_estimada": campo['produtividade_estimada'],
            "data_colheita": campo['data_colheita'].strftime('%d-%m-%Y'),
            "maquinas_alocadas": campo['maquinas_alocadas'],
            "custo_fixo": campo['custo_fixo']
        })
    with open('dados_campos.json', 'w') as f:
        json.dump(dados, f, indent=4)

# Função para exibir informações dos campos na área de resultados
def atualizar_resultados():
    """
    Atualiza a área de resultados com os campos registrados no banco Oracle.
    """
    if not conexao:
        conectar_ao_banco()
        if not conexao:
            return

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, area_ha, produtividade_estimada, TO_CHAR(data_colheita, 'DD-MM-YYYY'), maquinas_alocadas, custo_fixo FROM campos_agro")
        rows = cursor.fetchall()
        cursor.close()

        for row in tree.get_children():
            tree.delete(row)
        for campo in rows:
            tree.insert("", "end", values=(campo[0], campo[1], campo[2], campo[3], campo[4], campo[5]))
    except oracledb.DatabaseError as e:
        messagebox.showerror("Erro", f"Erro ao buscar dados do banco de dados: {e}")

# Função para simular custos e previsão de produção para todos os campos
def simular_colheita():
    """
    Simula o custo e a produção esperada para todos os campos registrados.
    """
    if not conexao:
        conectar_ao_banco()
        if not conexao:
            messagebox.showerror("Erro", "Sem conexão com o banco de dados.")
            return

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, area_ha, produtividade_estimada, custo_fixo FROM campos_agro")
        rows = cursor.fetchall()
        cursor.close()

        if not rows:
            messagebox.showinfo("Informação", "Nenhum campo para simular.")
            return

        resultados = ""
        for campo in rows:
            nome, area_ha, produtividade_estimada, custo_fixo = campo
            custo = custo_fixo
            producao = prever_producao(area_ha, produtividade_estimada)
            resultados += f"Campo: {nome} - Custo Total Estimado: R${custo:.2f}, Produção Estimada: {producao:.2f} toneladas\n"

        text_resultados.delete(1.0, tk.END)
        text_resultados.insert(tk.END, resultados)
    except oracledb.DatabaseError as e:
        messagebox.showerror("Erro", f"Erro ao buscar dados do banco de dados: {e}")

# Função para calcular a produção estimada
def prever_producao(area_ha, produtividade_estimada):
    producao = area_ha * produtividade_estimada
    return producao

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("Gestão de Colheita do Agronegócio")
root.geometry("1200x700")

# Frames
frame_left = tk.Frame(root, padx=10, pady=10)
frame_left.pack(side=tk.LEFT, fill=tk.Y)

frame_right = tk.Frame(root, padx=10, pady=10)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Frame Esquerdo - Ações
btn_adicionar = tk.Button(frame_left, text="Adicionar Campo", command=adicionar_campo_interface, width=20)
btn_adicionar.pack(pady=5)

btn_simular = tk.Button(frame_left, text="Simular Colheita", command=simular_colheita, width=20)
btn_simular.pack(pady=5)

btn_sair = tk.Button(frame_left, text="Sair", command=root.quit, width=20)
btn_sair.pack(pady=5)

# Frame Direito - Entrada de Dados e Resultados
tk.Label(frame_right, text="Nome do Campo:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_nome = tk.Entry(frame_right, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_right, text="Área Plantada (ha):").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_area_ha = tk.Entry(frame_right, width=30)
entry_area_ha.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_right, text="Produtividade Estimada (t/ha):").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_produtividade = tk.Entry(frame_right, width=30)
entry_produtividade.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_right, text="Data Estimada de Colheita (dd-mm-yyyy):").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_data_colheita = tk.Entry(frame_right, width=30)
entry_data_colheita.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame_right, text="Máquinas Alocadas (separadas por vírgula):").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
entry_maquinas = tk.Entry(frame_right, width=30)
entry_maquinas.grid(row=4, column=1, padx=10, pady=5)

tk.Label(frame_right, text="Custo Fixo (R$):").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
entry_custo_fixo = tk.Entry(frame_right, width=30)
entry_custo_fixo.grid(row=5, column=1, padx=10, pady=5)

# Frame Direito - Resultados
tree = ttk.Treeview(frame_right, columns=("Nome", "Área (ha)", "Produtividade (t/ha)", "Data de Colheita", "Máquinas", "Custo Fixo"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Área (ha)", text="Área (ha)")
tree.heading("Produtividade (t/ha)", text="Produtividade (t/ha)")
tree.heading("Data de Colheita", text="Data de Colheita")
tree.heading("Máquinas", text="Máquinas")
tree.heading("Custo Fixo", text="Custo Fixo")

tree.column("Nome", width=100)
tree.column("Área (ha)", width=100)
tree.column("Produtividade (t/ha)", width=150)
tree.column("Data de Colheita", width=120)
tree.column("Máquinas", width=200)
tree.column("Custo Fixo", width=100)

tree.grid(row=6, column=0, columnspan=2, pady=20, padx=10, sticky="nsew")

frame_right.grid_rowconfigure(6, weight=1)
frame_right.grid_columnconfigure(1, weight=1)

# Frame Direito - Área de resultados de simulação
tk.Label(frame_right, text="Resultados da Simulação:").grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
text_resultados = tk.Text(frame_right, height=10, width=70)
text_resultados.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

root.mainloop()
