import pandas as pd

def transform_float(el:str):
    replace = (el.replace(" ", "").
                  replace(",", ".").
                  replace('\xa0', ''))

    data_form = float(replace)
    return data_form


def main():
    uf = pd.read_html('https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil')[1]
    colunas = ['Área (km²)', 'PIB per capita (R$) (2015)', 'PIB (2015)', 'População (Censo 2022)']

    print(uf[colunas].applymap(transform_float))
    print(uf.dtypes)


if __name__ == '__main__':
    main()
