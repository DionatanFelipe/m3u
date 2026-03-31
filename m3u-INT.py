import os

# ============================
# Seletor de idioma
# ============================
print("Escolha o idioma / Choose language / Elige idioma:")
print("1 - Português (Brasil)")
print("2 - English (International)")
print("3 - Español (Latam)")

idioma = input("Digite o número do idioma / Enter the number / Ingrese el número: ").strip()

# ============================
# Definindo mensagens de acordo com o idioma
# ============================
if idioma == "1":
    titulo = "=== Conversor de Playlists M3U ==="
    msg_origem = "Digite o caminho da pasta de origem (onde estão os .m3u): "
    msg_destino = "Digite o caminho da pasta de destino: "
    msg_antigo = "Digite o caminho ANTIGO (que será substituído): "
    msg_novo = "Digite o caminho NOVO (substituto): "
    msg_processando = "\nProcessando arquivos...\n"
    msg_ok = "[OK] {arquivo} atualizado"
    msg_sem_alteracao = "[--] {arquivo} sem alterações"
    msg_finalizado = "\n=== Finalizado ==="
    msg_verificados = "Arquivos verificados: {qtd}"
    msg_modificados = "Arquivos modificados: {qtd}"
    msg_pasta_invalida = "❌ Pasta de entrada inválida."

elif idioma == "2":
    titulo = "=== M3U Playlist Converter ==="
    msg_origem = "Enter the source folder path (where the .m3u files are): "
    msg_destino = "Enter the destination folder path: "
    msg_antigo = "Enter the OLD path (to be replaced): "
    msg_novo = "Enter the NEW path (replacement): "
    msg_processando = "\nProcessing files...\n"
    msg_ok = "[OK] {arquivo} updated"
    msg_sem_alteracao = "[--] {arquivo} unchanged"
    msg_finalizado = "\n=== Finished ==="
    msg_verificados = "Files checked: {qtd}"
    msg_modificados = "Files modified: {qtd}"
    msg_pasta_invalida = "❌ Invalid input folder."

else:  # Espanhol Latam como padrão
    titulo = "=== Convertidor de Playlists M3U ==="
    msg_origem = "Ingrese la ruta de la carpeta de origen (donde están los .m3u): "
    msg_destino = "Ingrese la ruta de la carpeta de destino: "
    msg_antigo = "Ingrese la RUTA ANTIGUA (que será reemplazada): "
    msg_novo = "Ingrese la RUTA NUEVA (reemplazo): "
    msg_processando = "\nProcesando archivos...\n"
    msg_ok = "[OK] {arquivo} actualizado"
    msg_sem_alteracao = "[--] {arquivo} sin cambios"
    msg_finalizado = "\n=== Finalizado ==="
    msg_verificados = "Archivos verificados: {qtd}"
    msg_modificados = "Archivos modificados: {qtd}"
    msg_pasta_invalida = "❌ Carpeta de entrada inválida."

# ============================
# Cabeçalho
# ============================
print("\n" + titulo + "\n")

# ============================
# Entradas do usuário
# ============================
pasta_origem = input(msg_origem).strip()
pasta_destino = input(msg_destino).strip()
caminho_antigo = input(msg_antigo).strip()
caminho_novo = input(msg_novo).strip()

print(msg_processando)

# ============================
# Validações e criação de pasta
# ============================
if not os.path.isdir(pasta_origem):
    print(msg_pasta_invalida)
    exit()

os.makedirs(pasta_destino, exist_ok=True)

arquivos_processados = 0
arquivos_modificados = 0

# ============================
# Processamento dos arquivos
# ============================
for arquivo in os.listdir(pasta_origem):
    if arquivo.endswith('.m3u'):
        arquivos_processados += 1
        
        caminho_arquivo_origem = os.path.join(pasta_origem, arquivo)

        with open(caminho_arquivo_origem, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        modificado = False

        for i in range(len(linhas)):
            if caminho_antigo in linhas[i]:
                linhas[i] = linhas[i].replace(caminho_antigo, caminho_novo)
                modificado = True

        if modificado:
            caminho_arquivo_destino = os.path.join(pasta_destino, arquivo)
            with open(caminho_arquivo_destino, 'w', encoding='utf-8') as f:
                f.writelines(linhas)

            arquivos_modificados += 1
            print(msg_ok.format(arquivo=arquivo))
        else:
            print(msg_sem_alteracao.format(arquivo=arquivo))

# ============================
# Relatório final
# ============================
print(msg_finalizado)
print(msg_verificados.format(qtd=arquivos_processados))
print(msg_modificados.format(qtd=arquivos_modificados))