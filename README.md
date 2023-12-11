# find_file_true
# Dosya Listeleme Uygulaması

Bu basit Python uygulaması, belirli bir klasördeki dosyaları listeler ve dosyaların gerçek uzantılarına göre renklendirme yapar.
Klasörün içindeki dosyaların gerçek uzantılarını bize gösterir.Eğer dosyanın uzantısı ile programın bize sunduğu uzantı eşleşmiyorsa o sütunu kırmızı yazar.
Her dosya için bir ID kullanarak dosyaları Treeview widgetına ekler.
Programı çalıştıracağınız dizin içinde başka dizin olmamalı sadece dosyalar olmalı.Bunu 2.versiyonda geşitricem


Programda belirlenen bazı dosya türleri ve gerçek uzantıları şunlar :

JPEG dosyaları: .jpeg uzantısı\n
PNG dosyaları: .png uzantısı
GIF dosyaları: .gif uzantısı
MP3 dosyaları: .mp3 uzantısı
PDF dosyaları: .pdf uzantısı
DOCX dosyaları: .docx uzantısı
XLSX dosyaları: .xlsx uzantısı
PPTX dosyaları: .pptx uzantısı
Access dosyaları: .accdb uzantısı
ODT dosyaları: .odt uzantısı
ODS dosyaları: .ods uzantısı
ODP dosyaları: .odp uzantısı
XLS dosyaları: .xls uzantısı
DOC dosyaları: .doc uzantısı
PPT dosyaları: .ppt uzantısı
Metin dosyaları: .txt uzantısı
CSV dosyaları: .csv uzantısı
HTML dosyaları: .html uzantısı
Exe dosyaları: .exe uzantısı


## Başlangıç

Uygulamayı kullanmaya başlamak için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler

- Python (3.x sürümü önerilir)
- Tkinter kütüphanesi
- Magic kütüphanesi

### Kurulum

1. Depoyu klonlayın:

    ```bash
    git clone https://github.com/ozan-B/find_file_true
    cd find_file_true
    ```


    ```

3. Uygulamayı başlatın:

    ```bash
    python3 main.py
    ```

## Kullanım

- "Klasör Seç" düğmesine tıklayarak bir klasör seçin.
- Uygulama, seçilen klasördeki dosyaları listeleyecek ve gerçek uzantılarına göre renklendirme yapacaktır.

## Katkıda Bulunma

1. Bu depoyu forklayın.
2. Yeni bir dal oluşturun (`git checkout -b feature/yenifonksiyon`).
3. Yaptığınız değişiklikleri commit edin (`git commit -am 'Yeni fonksiyon eklendi'`).
4. Dalınıza itme yapın (`git push origin feature/yenifonksiyon`).
5. Bir Pull Request oluşturun.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına göz atabilirsiniz.
