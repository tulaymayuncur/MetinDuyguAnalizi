# Project Setup Guide

Bu rehber, Mac ve Windows işletim sistemleri için nasıl bir Python sanal ortamı oluşturup, gerekli modülleri yükleyeceğinizi adım adım açıklamaktadır.

## Gereksinimler

- Python 3.x
- pip (Python Paket Yöneticisi)

## Sanal Ortam Oluşturma ve Gerekli Modülleri Yükleme

### Mac

1. **Terminali açın.**

2. **Sanal ortam (`myenv`) oluşturun:**
    ```sh
    python3 -m venv myenv
    ```

3. **Sanal ortamı etkinleştirin:**
    ```sh
    source myenv/bin/activate
    ```

4. **pip'i güncelleyin (isteğe bağlı):**
    ```sh
    pip install --upgrade pip
    ```

5. **Gerekli modülleri yükleyin:**
    ```sh
    pip install flask
    pip install torch torchvision torchaudio
    pip install transformers
    ```

### Windows

1. **Komut İstemcisini (Command Prompt) veya PowerShell'i açın.**

2. **Sanal ortam (`myenv`) oluşturun:**
    ```sh
    python -m venv myenv
    ```

3. **Sanal ortamı etkinleştirin:**
    ```sh
    myenv\Scripts\activate
    ```

4. **pip'i güncelleyin (isteğe bağlı):**
    ```sh
    pip install --upgrade pip
    ```

5. **Gerekli modülleri yükleyin:**
    ```sh
    pip install flask
    pip install torch torchvision torchaudio
    pip install transformers
    ```


## Proje Çalıştırma 
    ```sh
    python3 app.py
    ```