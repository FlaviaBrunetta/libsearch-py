import pandas as pd
from pathlib import Path

base_livros = Path(__file__).parent / "GoodReads_100k_books.csv"

def buscador(genero: str, num_pag: int, csv_path=base_livros):
    """
        descricao: 
            Função para buscar livros dentro de uma base de dados
            a partir de um genero e numero de páginas. 
            Importante que genero seja passado em inglês. 

        Args:
            genero (string): nome do genero (inglês)
            num_pag (int): numero de paginas do livro
            csv_path: caminho para base de dados

        Returns:
            dataframe: livros encontrados com as colunas: 
            'author', 'bookformat', 'desc', 'genre', 'img', 'isbn', 'isbn13',
            'link', 'pages', 'rating', 'reviews', 'title', 'totalratings'
    """   

    base = pd.read_csv(csv_path, encoding='utf-8')

    base['pages'] = base['pages'].astype(int)
    base['rating'] = base['rating'].astype(float)

    base = base[(base['genre'].str.contains(genero, case=False)) 
                & ((num_pag-20) < base['pages']) 
                & (base['pages'] < (num_pag+20))]
    
    if len(base) > 100:
        base_4 = base[base['rating'] > 4]
        if len(base_4) > 0:
            base = base_4

    base = base.sort_values(by = 'rating', ascending=False)

    resultado = base[['title', 'author', 'pages', 'genre', 'rating', 'desc']].head(10).to_dict(orient='records')

    return resultado

if __name__ == '__main__':
    print(buscador('romance', 250))
