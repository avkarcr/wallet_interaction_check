# Wallet Interaction Checker

[Читать на русском](#проверка-взаимодействий-кошельков)

This Python program processes CSV files exported from [Etherscan](https://etherscan.io/) to find all interactions between a base wallet (`wallet_base`) and multiple other wallets (`wallets`). It supports multiple CSV formats from Etherscan, including Ethereum transactions, token transfers, and internal transactions. The program scans all CSV files in a directory, filters relevant transactions, and saves the results in a separate folder.

## Features

- Analyzes wallet interactions through downloaded Etherscan CSV files.
- Supports multiple CSV formats:
  - Ethereum transactions
  - Token transfers
  - Internal transactions
- Processes all CSV files in a directory.
- Automatically filters and outputs transactions between a base wallet (`wallet_base`) and a list of other wallets (`wallets`).
- Deletes old filtered results before each run.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/wallet-interaction-checker.git
    cd wallet-interaction-checker
    ```

2. **Install dependencies**:
    This program requires Python 3 and the pandas library. Install the required package by running:
    ```bash
    pip install pandas
    ```

## Usage

1. **Prepare your CSV files**:
    - Export transaction history from [Etherscan](https://etherscan.io/) for the wallets you want to analyze.
    - Place the CSV files in the same directory as the script or specify the path to a folder containing your CSV files.

2. **Create config.py in the project folder**:
   - In the root folder of your project, create a new file named `config.py`.
   - This file will store your personalized configuration (wallet addresses).
   - Open `config.py` and fill it with your specific variables.
   - Below is an example of what your `config.py` might look like:

   ```python
   # config.py
   wallet_base = '0xYourBaseWalletAddress'
   wallets = [
       '0xWallet1',
       '0xWallet2',
       '0xWallet3'
   ]
   ```

3. **Run the script**:
    - The script will iterate over all wallets in the `wallets` list and compare transactions with `wallet_base`.
    - Run the program:
      ```bash
      python wallet_checker.py
      ```

4. **Output**:
    - The program will create a folder called `filtered_results` where it saves CSV files with filtered transactions between `wallet_base` and each wallet from the `wallets` list.
    - Each output file will contain all transactions between the base wallet and the current wallet in the list for each CSV file.

## Example

If you have a CSV file named `export-0x123.csv` and want to find all transactions between the `wallet_base` and a list of wallets (`0x456`, `0x789`, etc.), the program will filter the transactions and save them in `filtered_results/filtered_export....csv`.

## Configuration

In the script, modify the following variables according to your needs:

- `wallet_base`: The base wallet address that you are checking interactions for.
- `wallets`: A list of wallet addresses to compare with the base wallet.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to submit issues or pull requests to improve the program. Any suggestions are welcome!

---

# Проверка взаимодействий кошельков

Эта программа на Python обрабатывает файлы CSV, экспортированные с [Etherscan](https://etherscan.io/), чтобы найти все взаимодействия между базовым кошельком (`wallet_base`) и несколькими другими кошельками (`wallets`). Программа поддерживает несколько форматов CSV-файлов из Etherscan, включая транзакции Ethereum, переводы токенов и внутренние транзакции. Программа сканирует все CSV-файлы в каталоге, фильтрует соответствующие транзакции и сохраняет результаты в отдельную папку.

## Функции

- Анализирует взаимодействия кошельков через загруженные файлы CSV с Etherscan.
- Поддерживает несколько форматов CSV:
  - Транзакции Ethereum
  - Переводы токенов
  - Внутренние транзакции
- Обрабатывает все CSV файлы в каталоге.
- Автоматически фильтрует и выводит транзакции между базовым кошельком (`wallet_base`) и списком других кошельков (`wallets`).
- Удаляет старые результаты перед каждым запуском.

## Установка

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/yourusername/wallet-interaction-checker.git
    cd wallet-interaction-checker
    ```

2. **Установите зависимости**:
    Для работы программы требуется Python 3 и библиотека pandas. Установите необходимые пакеты командой:
    ```bash
    pip install pandas
    ```

## Использование

1. **Подготовьте CSV файлы**:
    - Экспортируйте историю транзакций с [Etherscan](https://etherscan.io/) для кошельков, которые вы хотите проанализировать.
    - Поместите CSV файлы в ту же директорию, где находится скрипт, или укажите путь к папке, содержащей ваши CSV файлы.

2. **Создайте файл config.py в папке проекта**:
   - В корневой папке вашего проекта создайте новый файл с именем `config.py`.
   - Этот файл будет хранить ваши персонализированные настройки (адреса кошельков).
   - Откройте `config.py` и заполните его своими специфическими переменными.
   - Пример того, как может выглядеть ваш `config.py`:

   ```python
   # config.py
   wallet_base = '0xYourBaseWalletAddress'
   wallets = [
       '0xWallet1',
       '0xWallet2',
       '0xWallet3'
   ]
   ```

3. **Запустите скрипт**:
    - Скрипт будет перебирать все кошельки из списка `wallets` и сравнивать их транзакции с `wallet_base`.
    - Запустите программу:
      ```bash
      python wallet_checker.py
      ```

3. **Результаты**:
    - Программа создаст папку `filtered_results`, где будут сохранены CSV файлы с отфильтрованными транзакциями между `wallet_base` и каждым кошельком из списка `wallets`.
    - Каждый файл вывода будет содержать все транзакции между базовым кошельком и текущим кошельком из списка для каждого CSV файла.

## Пример

Если у вас есть CSV файл с именем `export-0x123.csv`, и вы хотите найти все транзакции между `wallet_base` и списком кошельков (`0x456`, `0x789` и т.д.), программа отфильтрует транзакции и сохранит их в `filtered_results/filtered_export....csv`.

## Настройка

В скрипте вы можете изменить следующие переменные в зависимости от ваших потребностей:

- `wallet_base`: Адрес базового кошелька, для которого проверяются взаимодействия.
- `wallets`: Список адресов кошельков для сравнения с базовым кошельком.

## Лицензия

Этот проект лицензирован на условиях лицензии MIT — см. файл [LICENSE](LICENSE) для подробностей.

## Вклад

Вы можете предложить улучшения через pull request или открыть issue, если нашли ошибку. Любые предложения приветствуются!
