# m3u
Editor de playlist m3u criadas no computador para rodar no android ou para ajuste de caminho.

--- # PT-BR - ENG - ESP
-
## **1️⃣ Guia em Português (Brasil)**

###  Descrição

Este script foi criado para permitir que você **use suas playlists M3U criadas no computador em outros dispositivos**, como celulares Android, quando os caminhos das pastas mudam ou diferem entre dispositivos. Antes, não era possível transferir diretamente as playlists porque os caminhos antigos não funcionavam. Depois que criei este script, consegui ajustar facilmente os caminhos e usar minhas playlists em qualquer lugar.

---

### 🧾 Tipos de arquivo e modos de execução

Existem **duas versões do script**:

1. **Modo Jupyter Notebook** (`.ipynb`)

   * Executado no Jupyter Notebook.
   * Possui instruções **internas passo a passo**, ideal para iniciantes.

2. **Modo Script Python** (`.py`)

   * Executado no terminal: `python3 corrigir_playlist.py`.
   * Solicita **via terminal**:

     * Pasta de origem (onde estão os arquivos `.m3u`)
     * Pasta de destino (onde salvar os arquivos corrigidos)
     * Caminho antigo (trecho a substituir)
     * Caminho novo (trecho substituto)

---

###  Como identificar os caminhos dentro da M3U

1. Abra o arquivo `.m3u` com um editor de texto simples (Bloco de Notas, Gedit, TextEdit etc.).
2. Observe como estão os caminhos dos arquivos, por exemplo:

```
/home/usuario/Musicas/minha-musica.mp3
/home/usuario/Musicas/playlist2/outro-arquivo.mp3
```

3. Esse trecho inicial (`/home/usuario/Musicas/`) é o **caminho antigo**, que será substituído.
4. Determine qual será o **caminho novo**, por exemplo, no celular Android:

   * `/storage/emulated/0/Music/`
   * Ou qualquer pasta que você criou para armazenar suas músicas.

> Dica: O script **não altera o arquivo original**, apenas cria cópias corrigidas na pasta de destino.

---

###  Configuração no script

No script Python (`.py`) ou notebook, ajuste:

```python
# Pasta onde estão suas playlists originais
pasta_origem = '/home/usuario/Musicas/Playlist/'

# Pasta para salvar os arquivos corrigidos
pasta_destino = '/home/usuario/Musicas/Playlist/Celular/'

# Caminho antigo encontrado na M3U
caminho_antigo = '/home/usuario/Musicas/'

# Novo caminho para substituir
caminho_novo = '/storage/emulated/0/Music/'
```

---

###  Como executar

**Modo Notebook:**

1. Abra o `MudarCorM3U.ipynb` no Jupyter Notebook.
2. Siga as instruções internas para preencher os caminhos e executar.

**Modo Script Python:**

1. Salve o arquivo como `corrigir_playlist.py`.
2. Abra o terminal e rode:

```
python3 corrigir_playlist.py
```

3. Responda às perguntas solicitadas pelo script:

   * Pasta de origem
   * Pasta de destino
   * Caminho antigo
   * Caminho novo

4. O script exibirá mensagens indicando quais arquivos foram atualizados:

```
[OK] playlist1.m3u atualizado
[--] playlist2.m3u sem alterações
```

5. No final, verá o resumo:

```
Arquivos verificados: 5
Arquivos modificados: 3
```

---

### Quando usar

* Transferir playlists entre dispositivos.
* Ajustar caminhos quando você muda pastas de música.
* Usar playlists criadas no computador em celulares ou outros dispositivos.

---

###  Dicas importantes

* Confira se os caminhos antigos são exatamente iguais aos das playlists.
* Funciona apenas com arquivos `.m3u`.
* Arquivos sem alterações não serão copiados.

----------------------------------------------------------------------------------------------------------------------------

## **2️⃣ Guide in English (International)**

###  Description

This script allows you to **use your M3U playlists created on a computer on other devices**, such as Android phones, when folder paths change or differ between devices. Previously, playlists could not be used directly because the old paths didn’t work. This script lets you **easily fix the paths** and use your playlists anywhere.

---

### 🧾 File types and execution modes

There are **two versions of the script**:

1. **Jupyter Notebook mode** (`.ipynb`)

   * Run in Jupyter Notebook.
   * Contains **step-by-step internal instructions**, ideal for beginners.

2. **Python Script mode** (`.py`)

   * Run from the terminal: `python3 fix_playlist.py`.
   * Requests via terminal:

     * Source folder (where `.m3u` files are)
     * Destination folder (where corrected files will be saved)
     * Old path (to replace)
     * New path (replacement path)

---

###  How to identify paths in the M3U

1. Open the `.m3u` file with a simple text editor (Notepad, Gedit, TextEdit, etc.).
2. Check the file paths, for example:

```
/home/user/Music/my-song.mp3
/home/user/Music/playlist2/another-song.mp3
```

3. This initial part (`/home/user/Music/`) is the **old path**, which will be replaced.
4. Determine the **new path**, for example on Android:

   * `/storage/emulated/0/Music/`
   * Or your custom folder for music.

> Tip: The script **does not modify the original file**, it only creates corrected copies in the destination folder.

---

###  Script configuration

Set the following variables in the script or notebook:

```python
# Folder with original playlists
source_folder = '/home/user/Music/Playlist/'

# Folder to save corrected files
destination_folder = '/home/user/Music/Playlist/Phone/'

# Old path found in the M3U
old_path = '/home/user/Music/'

# New path to replace it
new_path = '/storage/emulated/0/Music/'
```

---

###  How to run

**Notebook mode:**

1. Open `FixM3UPaths.ipynb` in Jupyter Notebook.
2. Follow internal instructions to fill paths and run cells.

**Python Script mode:**

1. Save the file as `fix_playlist.py`.
2. Open a terminal and run:

```
python3 fix_playlist.py
```

3. Provide the requested information:

   * Source folder
   * Destination folder
   * Old path
   * New path

4. The script will show which files were updated:

```
[OK] playlist1.m3u updated
[--] playlist2.m3u unchanged
```

5. Summary at the end:

```
Files checked: 5
Files modified: 3
```

---

###  When to use

* Transfer playlists between devices.
* Adjust paths when you move music folders.
* Use playlists created on the computer on phones or other devices.

---

###  Tips

* Ensure the old paths exactly match the ones in the playlists.
* Works **only with `.m3u` files**.
* Files with no changes will not be copied.

----------------------------------------------------------------------------------------------------------------------------
## **3️⃣ Guía en Español **

###  Descripción

Este script permite **usar tus playlists M3U creadas en la computadora en otros dispositivos**, como celulares Android, cuando las rutas de las carpetas cambian o son diferentes entre dispositivos. Antes no se podían transferir directamente porque las rutas antiguas no funcionaban. Con este script, puedes **ajustar fácilmente las rutas** y usar tus playlists en cualquier lugar.

---

### 🧾 Tipos de archivo y modos de ejecución

Hay **dos versiones del script**:

1. **Modo Jupyter Notebook** (`.ipynb`)

   * Ejecutado en Jupyter Notebook.
   * Contiene instrucciones **internas paso a paso**, ideal para principiantes.

2. **Modo Script Python** (`.py`)

   * Ejecutado desde terminal: `python3 corregir_playlist.py`.
   * Solicita por terminal:

     * Carpeta de origen (donde están los `.m3u`)
     * Carpeta de destino (donde guardar los archivos corregidos)
     * Ruta antigua (a reemplazar)
     * Ruta nueva (ruta sustituta)

---

###  Cómo identificar las rutas dentro de la M3U

1. Abre el archivo `.m3u` con un editor de texto simple (Bloc de notas, Gedit, TextEdit, etc.).
2. Observa cómo están las rutas de los archivos, por ejemplo:

```
/home/usuario/Musica/mi-cancion.mp3
/home/usuario/Musica/playlist2/otra-cancion.mp3
```

3. Esta parte inicial (`/home/usuario/Musica/`) es la **ruta antigua**, que será reemplazada.
4. Determina la **ruta nueva**, por ejemplo en Android:

   * `/storage/emulated/0/Music/`
   * O la carpeta que hayas creado para música.

> Consejo: El script **no modifica los archivos originales**, solo crea copias corregidas en la carpeta de destino.

---

###  Configuración en el script

Ajusta estas variables en el script o notebook:

```python
# Carpeta con playlists originales
carpeta_origen = '/home/usuario/Musica/Playlist/'

# Carpeta para guardar archivos corregidos
carpeta_destino = '/home/usuario/Musica/Playlist/Celular/'

# Ruta antigua encontrada en la M3U
ruta_antigua = '/home/usuario/Musica/'

# Nueva ruta para reemplazar
ruta_nueva = '/storage/emulated/0/Music/'
```

---

### Cómo ejecutar

**Modo Notebook:**

1. Abre `CorregirM3UPaths.ipynb` en Jupyter Notebook.
2. Sigue las instrucciones internas para completar las rutas y ejecutar.

**Modo Script Python:**

1. Guarda el archivo como `corregir_playlist.py`.
2. Abre terminal y ejecuta:

```
python3 corregir_playlist.py
```

3. Ingresa la información solicitada:

   * Carpeta de origen
   * Carpeta de destino
   * Ruta antigua
   * Ruta nueva

4. El script mostrará cuáles archivos fueron actualizados:

```
[OK] playlist1.m3u actualizado
[--] playlist2.m3u sin cambios
```

5. Al final, verás un resumen:

```
Archivos verificados: 5
Archivos modificados: 3
```

---

### 📱 Cuándo usar

* Transferir playlists entre dispositivos.
* Ajustar rutas cuando se cambian carpetas de música.
* Usar playlists creadas en la computadora en celulares u otros dispositivos.

---

###  Consejos

* Verifica que las rutas antiguas coincidan exactamente con las de las playlists.
* Funciona **solo con archivos `.m3u`**.
* Los archivos sin cambios no serán copiados.

---

