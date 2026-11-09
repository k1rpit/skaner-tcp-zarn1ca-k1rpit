# skaner-tcp-zarn1ca-k1rpit
<summary><b>Multi-modular TCP network scanner and banner grabbing tool.</b></summary>
<summary><b>This project focuses on a modular architecture, splitting the logic into an interface dispatcher, a stealth/regular scanning engine, and a banner scraper.</b></summary>
<summary><b>Designed as a structured, multi-file automation tool for local and external network scanning via custom JSON port profiles.</b></summary>

<details>
<summary>About me: </summary>

My Python TG channel:https://t.me/k1rpit718s
My repos:https://github.com/k1rpit?tab=repositories

</details>
---

<summary><b>Мультимодульный сетевой TCP-сканер и инструмент для сбора баннеров.</b></summary>
<summary><b>В проекте реализована модульная структура: разделение на интерфейсный диспетчер, движок сканирования и сборщик баннеров.</b></summary>
<summary><b>Инструмент ориентирован на автоматизацию проверок локальных и внешних сетей с использованием кастомных JSON-профилей портов.</b></summary>

<details>
<summary>Обо мне: </summary>

Мой Python ТГ-канал:https://t.me/k1rpit718s
Мои репозитории:https://github.com/k1rpit?tab=repositories

</details>


## гайд
* **input IP>** — вводим либо айпи пример: 1.1.1.1 или домен
* **input delay scan port>** —  вводим максимальная огранечения у сканера (больше 3 не советую)
* **input timeout>** — вводим время котрой сканер будет ждать на ответ порта (советую не больше 1 не меньше 0.2)
* **name file .json>** —  вводим имя файла понстю напрмер "top_100_ports.json" из деректории json-data-ports/
>**важно**:запускать файл только из орегинальной деректории ,а также толтко файла run.py

---

## Guide
* **input IP>** — enter either an IP address (example: 1.1.1.1) or a domain.
* **input delay scan port>** — enter the maximum delay limit for the scanner (values above 3 are not recommended).
* **input timeout>** — enter the time the scanner will wait for a port response (recommended between 0.2 and 1.0).
* **name file .json>** — enter the full file name, for example "top_100_ports.json", from the json-data-ports/ directory.
>**Important**: The script must be executed strictly from the root directory, and only by running the run.py file without modifying any internal code.
