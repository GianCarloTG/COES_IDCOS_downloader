import wget

# year = '2019'
# month = '11_NOVIEMBRE'
# day = '15'

def download_file(year, month, day):
    url_base = '''https://www.coes.org.pe/portal/browser/download?url=Post%20Operaci%C3%B3n%2FReportes%2FIDCOS%2F'''
    parser_y = '''%2F'''
    parser_m = '''%2FD%C3%ADa%20'''
    parser_d = '''%2F'''

    file = f'Anexo2_Resumen_operacion_{year}{month[:2]}{day}.xlsx'

    url = url_base + year + parser_y + month + parser_m + day + parser_d + file
    filename = wget.download(url)

def main():
    init_year = 2012
    fin_year = 2014

    months = ['01_ENERO','02_FEBRERO','03_MARZO',
              '04_ABRIL','05_MAYO','06_JUNIO',
              '07_JULIO','08_AGOSTO','09_SEPTIEMBRE',
              '10_OCTUBRE','11_NOVIEMBRE', '12_DICIEMBRE']

    for year in range(init_year, fin_year+1):
        for month in months:
            for day in range(1, 32):
                try:
                    download_file(str(year), month, str(day))
                except ValueError as ve:
                    print(f"ValueError on {year}-{month}-{day}: {ve}")

if __name__ == "__main__":
    main()