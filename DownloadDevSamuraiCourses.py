import os
import requests
from bs4 import BeautifulSoup
from threading import Thread
from queue import Queue


def get_hrefs_from_page(url):
    # Envia uma solicitação GET para a página da web
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analisa o conteúdo HTML da página
        soup = BeautifulSoup(response.content, 'html.parser')

        hrefs = [a['href']
                 for a in soup.select('ul li a') if 'href' in a.attrs]

        return hrefs
    else:
        print(f"Erro ao acessar a página: {response.status_code}")
        return []


def download_file(url, folder_path):
    local_filename = os.path.join(folder_path, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"{url} baixado com sucesso!")
    return local_filename


def worker(queue, folder_path):
    while not queue.empty():
        url = queue.get()
        print(f"Baixando {url}...")
        download_file(url, folder_path)
        queue.task_done()


if __name__ == '__main__':
    url = 'https://class.devsamurai.com.br'
    download_folder = r'path\to\download_folder'

    hrefs = get_hrefs_from_page(url)

    queue = Queue()
    for href in hrefs:
        queue.put(href)

    # Cria e inicia as threads
    threads = []
    for _ in range(2):  # Número de threads
        thread = Thread(target=worker, args=(queue, download_folder))
        thread.start()
        threads.append(thread)

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()