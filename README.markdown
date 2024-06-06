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

- `python3 app.py`

## Eksik Dosyaları Temin Etme

Projemizde bazı büyük dosyalar ve veri setleri `.gitignore` dosyasında yer aldıkları için bu depoda bulunmamaktadır. Bu dosyalar:

- `yeni_test.csv`
- `yeni_train.csv`
- `my_model_final.pt`
- `early_save.pt`
- `TREMODATA.xml`

Bu dosyaları temin etmek için [bu drive linkini](https://drive.google.com/drive/folders/1lGZ8speGhTuEjSDb2cBmNbIKYtrc3c19?usp=sharing) kullanabilirsiniz.

### Dosyaların Temin Edilmesi

1. **Veri Dosyaları:**
   - `yeni_test.csv` ve `yeni_train.csv`: Bu dosyaları [drive linkinden](https://drive.google.com/drive/folders/1lGZ8speGhTuEjSDb2cBmNbIKYtrc3c19?usp=sharing) indirebilirsiniz.
   
2. **Model Dosyaları:**
   - `my_model_final.pt` ve `early_save.pt`: Bu dosyaları [drive linkinden](https://drive.google.com/drive/folders/1lGZ8speGhTuEjSDb2cBmNbIKYtrc3c19?usp=sharing) temin edebilirsiniz.
   
3. **Diğer Dosyalar:**
   - `TREMODATA.xml`: Bu dosyayı [drive linkinden](https://drive.google.com/drive/folders/1lGZ8speGhTuEjSDb2cBmNbIKYtrc3c19?usp=sharing) indirebilirsiniz.

Eksik dosyaları indirdikten sonra projenizin ilgili klasörlerine yerleştirerek kullanabilirsiniz.
