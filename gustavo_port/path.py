from pathlib import Path

# Exemplo 1: Criar um objeto Path para um arquivo ou diretório
# No exemplo a seguir, criamos um objeto Path para um arquivo chamado "arquivo.txt"
# que está localizado na pasta atual.
caminho_arquivo = Path("arquivo.txt")

# Exemplo 2: Obter o caminho absoluto de um arquivo ou diretório
# O método "resolve()" retorna o caminho absoluto do arquivo ou diretório.
caminho_absoluto = caminho_arquivo.resolve()
print(caminho_absoluto)

# Exemplo 3: Verificar se um arquivo ou diretório existe
# O método "exists()" retorna True se o arquivo ou diretório existe.
existe = caminho_arquivo.exists()
print(existe)

# Exemplo 4: Verificar se é um arquivo ou diretório
# Os métodos "is_file()" e "is_dir()" retornam True se for um arquivo ou diretório, respectivamente.
e_arquivo = caminho_arquivo.is_file()
e_diretorio = caminho_arquivo.is_dir()
print(e_arquivo, e_diretorio)

# Exemplo 5: Juntar caminhos de diretórios
# O método "joinpath()" concatena caminhos para formar um novo caminho.
diretorio_pai = Path("pasta_pai")
novo_caminho = diretorio_pai.joinpath("subpasta", "arquivo.txt")
print(novo_caminho)

# Exemplo 6: Listar arquivos e diretórios em um diretório
# O método "iterdir()" retorna um iterável contendo os caminhos dos arquivos e diretórios no diretório atual.
diretorio_atual = Path(".")
for caminho in diretorio_atual.iterdir():
    print(caminho)

# Exemplo 7: Criar um diretório
# O método "mkdir()" cria um diretório no caminho especificado.
novo_diretorio = Path("nova_pasta")
novo_diretorio.mkdir()

# Exemplo 8: Renomear ou mover um arquivo ou diretório
# O método "rename()" renomeia ou move um arquivo ou diretório.
caminho_arquivo.rename("novo_nome_arquivo.txt")

# Exemplo 9: Deletar um arquivo ou diretório
# O método "unlink()" deleta um arquivo, e o método "rmdir()" deleta um diretório vazio.
# Para deletar um diretório com conteúdo, use o método "rmtree()" do módulo "shutil".
caminho_arquivo.unlink()
novo_diretorio.rmdir()

# Exemplo 10: Obter apenas o nome do arquivo ou diretório
# O atributo "name" retorna apenas o nome do arquivo ou diretório.
nome_arquivo = caminho_arquivo.name
print(nome_arquivo)

# Exemplo 11: Obter apenas o diretório pai do arquivo ou diretório
# O atributo "parent" retorna o diretório pai do arquivo ou diretório.
diretorio_pai = caminho_arquivo.parent
print(diretorio_pai)
