def show_columns():
    import pandas as pd

    # Mostra todas as colunas
    pd.set_option('display.max_columns', None)

    # (Opcional) Mostra todas as linhas também
    pd.set_option('display.max_rows', None)

    # (Opcional) Ajusta a largura da coluna para não quebrar linhas
    pd.set_option('display.width', None)
