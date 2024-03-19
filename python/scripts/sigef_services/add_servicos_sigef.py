from qgis.PyQt.QtWidgets import QInputDialog, QMessageBox

base_url = "http://acervofundiario.incra.gov.br/i3geo/ogc.php?tema="
temas = [
    "certificada_sigef_particular",
    "certificada_sigef_publico",
    "imoveiscertificados_privado",
    "imoveiscertificados_publico",
    "parcelageo",
    "assentamentos",
    "reconhecimento",
    "quilombolas",
]
# Dicionário de estados brasileiros com siglas em minúsculas
estados_brasileiros = {
    "Acre": "ac",
    "Alagoas": "al",
    "Amapá": "ap",
    "Amazonas": "am",
    "Bahia": "ba",
    "Ceará": "ce",
    "Distrito Federal": "df",
    "Espírito Santo": "es",
    "Goiás": "go",
    "Maranhão": "ma",
    "Mato Grosso": "mt",
    "Mato Grosso do Sul": "ms",
    "Minas Gerais": "mg",
    "Pará": "pa",
    "Paraíba": "pb",
    "Paraná": "pr",
    "Pernambuco": "pe",
    "Piauí": "pi",
    "Rio de Janeiro": "rj",
    "Rio Grande do Norte": "rn",
    "Rio Grande do Sul": "rs",
    "Rondônia": "ro",
    "Roraima": "rr",
    "Santa Catarina": "sc",
    "São Paulo": "sp",
    "Sergipe": "se",
    "Tocantins": "to",
}

servicos = {"WFS": "connections-wfs", "WMS": "connections-wms"}

# Lista de nomes dos estados para exibir no QInputDialog
nomes_estados = list(estados_brasileiros.keys())

# Cria e exibe o QInputDialog para escolha de um estado
estado_escolhido, ok = QInputDialog.getItem(
    None, "Escolha um Estado", "Estados:", nomes_estados, 0, False
)

# Verifica se o usuário pressionou o botão OK e escolheu um estado
if ok and estado_escolhido:
    # Obtém a sigla do estado escolhido
    servico_escolhido, ok_servico = QInputDialog.getItem(
        None, "Escolha o Serviço", "Serviço:", servicos, 0, False
    )
    servico = None
    if ok_servico and servico_escolhido:
        # Obtém a sigla do estado escolhido
        sigla_estado = estados_brasileiros[estado_escolhido]
        # Mensagem final incluindo a escolha do serviço
        servico = servicos[servico_escolhido]
    else:
        QMessageBox.warning(None, "Cancelado", "A escolha do serviço foi cancelada.")
        exit()

    urls = []
    for tema in temas:
        conn_name = f"{tema.replace('_', ' ').title()} {sigla_estado.upper()}"
        conn_type = servico
        url_tema = f"{base_url}{tema}_{sigla_estado}"

        QSettings().setValue(f"qgis/{conn_type}/{conn_name}/authcfg", "")
        QSettings().setValue(f"qgis/{conn_type}/{conn_name}/url", url_tema)
        print("Adicionando:", servico, url_tema)
        urls.append(url_tema)

    iface.reloadConnections()
    sigla_estado = estados_brasileiros[estado_escolhido]
    # Mostra uma mensagem com o estado escolhido e sua sigla
    mensagem = f"Conexões {servico} do Estado {estado_escolhido} ({sigla_estado.upper()}) adicionadas com suscesso.\n  "
    mensagem += "\n  ".join(urls)

    QMessageBox.information(None, "Dados SIGEF", mensagem)
    # Faz o print do estado e sua sigla
else:
    QMessageBox.warning(None, "Cancelado", "Nenhuma seleção foi feita.")
