import pandas as pd
import os
import re

wallet_base = '0x123...'  # wallet A
wallets = [
    '0x456',
    '0x789',
]


def clear_filtered_results_folder():
    folder = 'filtered_results'
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Ошибка при удалении файла {file_path}: {e}")


def identify_csv_format(df):
    if 'Value_IN(ETH)' in df.columns and 'ParentTxFrom' in df.columns:
        return 'internal_transactions'
    elif 'TokenName' in df.columns and 'TokenSymbol' in df.columns:
        return 'token_transfers'
    elif 'Value_IN(ETH)' in df.columns and 'Value_OUT(ETH)' in df.columns:
        return 'eth_transactions'
    else:
        raise ValueError('Неизвестный формат CSV файла')


def process_csv_file(file_path, wallet):
    try:
        df = pd.read_csv(file_path)
        csv_format = identify_csv_format(df)
        if csv_format == 'eth_transactions':
            df['From'] = df['From'].astype(str)
            df['To'] = df['To'].astype(str)
            filtered_transactions = df[
                ((df['From'].str.lower() == wallet_base.lower()) & (df['To'].str.lower() == wallet.lower())) |
                ((df['From'].str.lower() == wallet.lower()) & (df['To'].str.lower() == wallet_base.lower()))]
        elif csv_format == 'token_transfers':
            df['From'] = df['From'].astype(str)
            df['To'] = df['To'].astype(str)
            filtered_transactions = df[
                ((df['From'].str.lower() == wallet_base.lower()) & (df['To'].str.lower() == wallet.lower())) |
                ((df['From'].str.lower() == wallet.lower()) & (df['To'].str.lower() == wallet_base.lower()))]
        elif csv_format == 'internal_transactions':
            df['ParentTxFrom'] = df['ParentTxFrom'].astype(str)
            df['ParentTxTo'] = df['ParentTxTo'].astype(str)
            filtered_transactions = df[((df['ParentTxFrom'].str.lower() == wallet_base.lower()) & (
                        df['ParentTxTo'].str.lower() == wallet.lower())) |
                                       ((df['ParentTxFrom'].str.lower() == wallet.lower()) & (
                                                   df['ParentTxTo'].str.lower() == wallet_base.lower()))]
        else:
            filtered_transactions = None

        if not filtered_transactions.empty:
            new_filename = re.sub(r'0x[a-fA-F0-9]{40}', wallet, f'filtered_{os.path.basename(file_path)}')
            output_file = os.path.join('filtered_results', new_filename)
            filtered_transactions.to_csv(output_file, index=False)
            print(f"Найдены и сохранены транзакции для файла: {output_file}")
        # else:
            # print(f"Транзакции между кошельками A и B не найдены в файле: {file_path}")

    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")


clear_filtered_results_folder()

for wallet in wallets:
    for filename in os.listdir():
        if filename.endswith('.csv'):
            file_path = os.path.join(os.getcwd(), filename)
            process_csv_file(file_path, wallet)
