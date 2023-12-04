import os
import binascii                 # Binary verileri ASCII formatına çevirmek için kullanılır.
import tkinter as tk
from tkinter import filedialog  #Dosya ve klasör seçimi için bir pencere sağlar
from tkinter import ttk         #Tkinter için gelişmiş widget'ları içeren bir modüldür.
import magic                    #Dosya türü tespiti için kullanılır.


class DosyaListelemePenceresi:  #Bu sınıf, bir dosya listeleme penceresi oluşturmayı amaçlar.




    def __init__(self, master): #Sınıfın başlatıcı metodu. Tkinter penceresini başlatır ve temel özellikleri ayarlar.
        self.master = master
        master.title("Dosya Listeleme")
        self.master.geometry("900x500")  # Ana pencere boyutu: 600x400


        self.magic = magic.Magic()
        self.tree = ttk.Treeview(master, columns=("ID", "Dosya Adı", "Gerçek Uzantı")) # Tkinter'ın ttk.Treeview widget'ını kullanarak bir ağaç görünümü oluşturur. Bu ağaç görünümü, "ID", "Dosya Adı" ve "Gerçek Uzantı" adlı üç sütunu içerecek şekilde ayarlanır.
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Dosya Adı")
        self.tree.heading("#2", text="Hex Temsil")
        self.tree.pack(expand=True, fill=tk.BOTH) #Ağaç görünümünü pencerenin her iki yönde de genişleyen bir şekilde paketler, yani pencere boyutu değiştirildiğinde ağaç görünümü de genişler.


        


        # ID sütununun genişliğini ayarla
        self.tree.column("#1", width=300)

        dosya_sec_button = tk.Button(master, text="Klasör Seç", command=self.klasor_sec)
        dosya_sec_button.pack()

        self.id_counter = 1  # ID sayacını başlangıç değeri olarak 1 olarak ayarlar. Bu sayaç, her dosyanın bir benzersiz kimliğini temsil eder.

    @staticmethod #: Bu bir özel (static) metodu ifade eder. Bir özel metot, örneğe bağlı olmadan çağrılabilir. Yani, sınıfın bir örneği oluşturulmadan doğrudan sınıf üzerinden çağrılabilir.
    def jaccard_benzerligi(str1, str2): # İki metni karşılaştırarak benzerlik oranını bulmak için kullanılır.
        set1 = set(str1)
        set2 = set(str2)

        kesisim = set1.intersection(set2)
        birlesim = set1.union(set2)

        benzerlik_orani = len(kesisim) / len(birlesim) * 100
        benzerlik_orani = round(benzerlik_orani, 2)

        return benzerlik_orani

    def hex_viewer(self, file_path): #Verilen dosyanın hex temsilini alır ve belirli hex özelliklerine göre dosya türünü tahmin eder.

        try:
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as file:
                    file_content = file.read()
                    hex_representation = binascii.hexlify(file_content).decode('utf-8')
                    hex10 = hex_representation[:16]

                    if self.jaccard_benzerligi("ffd8ffe0", hex10[:6]) > 55:
                        return ".jpeg"
                    if self.jaccard_benzerligi("89504e470d0a1a0a", hex10) > 65:
                        return ".png"
                    if self.jaccard_benzerligi("474946383961", hex10[:12]) >= 75 or self.MIME_kind(file_path)==17:
                        return ".gif"
                    if self.MIME_kind(file_path)==16:
                        return ".mp3"
                    if self.jaccard_benzerligi("25504446", hex10[:8]) >55 and self.MIME_kind(file_path)==14 :
                        return ".pdf"
                            
                    if self.jaccard_benzerligi("504B0304", hex10[:8]) > 55 and self.MIME_kind(file_path)==1:#dosya zip'se ve mime türü docx türüyle aynı ise docx yazdırır.
                            return ".docx"
                    if self.jaccard_benzerligi("504B0304", hex10[:8]) > 55 and self.MIME_kind(file_path)==2:
                            return ".xlsx"
                    if self.jaccard_benzerligi("504B0304", hex10[:8]) > 55 and self.MIME_kind(file_path)==3:
                            return ".pptx"
                    if self.jaccard_benzerligi("00010000    ", hex10[:8]) > 55 and self.MIME_kind(file_path)==4:
                            return ".accdb"
                    if self.jaccard_benzerligi("504B0304", hex10[:8]) > 55 and self.MIME_kind(file_path)==5:
                            return ".odt"
                    if self.jaccard_benzerligi("504B0304", hex10[:8]) > 55 and self.MIME_kind(file_path)==6:
                            return ".ods"
                    if self.jaccard_benzerligi("504B0304", hex10[:8]) > 55 and self.MIME_kind(file_path)==7:
                            return ".odp"
                    if self.jaccard_benzerligi("d0cf11e0", hex10[:8]) > 55 and self.MIME_kind(file_path)==8:
                            return ".xls"
                    if self.jaccard_benzerligi("d0cf11e0", hex10[:8]) > 55 and self.MIME_kind(file_path)==9:
                            return ".doc"
                    if self.jaccard_benzerligi("d0cf11e0", hex10[:8]) > 55 and self.MIME_kind(file_path)==10:
                            return ".ppt"
                    if self.MIME_kind(file_path)==12: #txt'nin sabit bir headerı yoktur
                            return ".txt"
                    if self.MIME_kind(file_path)==13:#sabit bir hex headerı yok 
                            return ".csv"
                    
                    if self.MIME_kind(file_path)==15: #bunun da sabit bir headerı yok 
                        return ".html"
                    if self.jaccard_benzerligi("4d5a", hex10[:4]) > 55:
                        return ".exe"
                    
                    else:
                        return "Diğer"
            else:
                tk.messagebox.showerror("Hata", "Bu bir dosya değil: {}".format(file_path))
        except Exception as e:
            tk.messagebox.showerror("Hata", "Hata oluştu: {}".format(e))






    def MIME_kind(self, file_path_office_file): #magic modülü kullanılarak, bir dosyanın MIME türünü tespit eder.

        
        mime=magic.Magic()
        mime_type = mime.from_file(file_path_office_file)

        
        #application/vnd.openxmlformats-officedocument.wordprocessingml.document
        if mime_type=="application/vnd.openxmlformats-officedocument.wordprocessingml.document" or mime_type.startswith("Microsoft Word"):#docx
            return 1
        elif mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or mime_type.startswith("Microsoft Excel"):#xlsx
            return 2
        elif mime_type == "application/vnd.openxmlformats-officedocument.presentationml.presentation" or mime_type =="Microsoft PowerPoint 2007+":#pptx
            return 3
        elif mime_type == "application/msaccess" or mime_type.startswith("Microsoft Access Database"):#accdb
            return 4
        elif mime_type == "application/vnd.oasis.opendocument.text" or mime_type =="OpenDocument Text":#odt
            return 5
        elif mime_type == "application/vnd.oasis.opendocument.spreadsheet"or mime_type.startswith("OpenDocument Spreadsheet"):#ods
            return 6
        elif mime_type == "application/vnd.oasis.opendocument.presentation" or mime_type.startswith("OpenDocument Presentation"):#odp
            return 7
        elif mime_type == "application/vnd.ms-excel" or "Microsoft Excel" in mime_type:#xls
            return 8
        elif mime_type == "application/msword" or "Microsoft Office Word" in mime_type:#doc
            return 9
        elif mime_type == "application/vnd.ms-powerpoint" or "PowerPoint" in mime_type:#ppt
            return 10
        elif mime_type == "text/plain" or mime_type.startswith("Unicode text") or mime_type.startswith("ASCII text") :#txt
            return 12
        elif mime_type.startswith("CSV") or mime_type == "text/csv" :#csv
            return 13
        elif mime_type.startswith("PDF") or mime_type == "application/pdf" :#pdf
            return 14
        elif mime_type.startswith("HTML document") or mime_type == "text/html" :#html
            return 15
        elif mime_type.startswith("Audio file with") or mime_type == "audio/mpeg" :#mp3
            return 16
        elif mime_type.startswith("GIF") :#gif
            return 17



    def uzanti_bul(self,file_path): #Dosyanın tam yolunu alır ve dosya adı ile uzantısını ayırarak uzantıyı döndürür.
       

        dosya_adı = os.path.basename(file_path)
        dosya_adi_ve_uzanti = os.path.splitext(dosya_adı)

        return dosya_adi_ve_uzanti[1]
                    


    def klasor_sec(self):#Kullanıcıya bir klasör seçme penceresi açar ve seçilen klasördeki dosyaları listeler.

        klasor = filedialog.askdirectory()
        if klasor:
            self.liste_guncelle(klasor)

    def liste_guncelle(self, klasor): #Bu metod, verilen bir klasördeki dosyaları listeleyen ve bu dosyaların gerçek uzantılarına göre bir Tkinter Treeview widget'ına ekleyen bir işlemler dizisini gerçekleştirir
        self.tree.delete(*self.tree.get_children()) # Tkinter Treeview'daki mevcut tüm öğeleri temizler. Bu, yeni dosyaların eklenmeden önce önceki dosyaların temiz bir şekilde görüntülenmesini sağlar.

        dosya_isimleri = os.listdir(klasor)   #Verilen klasördeki dosya isimlerini içeren bir liste oluşturur.

        for dosya in dosya_isimleri:  # Klasördeki her dosya için bir döngü başlatır.
            dosya_yolu = os.path.join(klasor, dosya)   #: Dosyanın tam yolunu oluşturur.
            gercek_uzanti = self.hex_viewer(dosya_yolu)  #hex_viewer metodunu kullanarak dosyanın gerçek uzantısını tespit eder.
            
    
            uzanti = self.uzanti_bul(dosya_yolu)#uzanti bulmetodunu kullanarak dosyanın uzantısını tespit eder.
            

 # Kırmızı renk etiketi oluştur
            self.tree.tag_configure("kirmizi", foreground="red")


            if gercek_uzanti :
                
                
                if uzanti != gercek_uzanti:

                    self.tree.insert("", tk.END, text=self.id_counter, values=(dosya, gercek_uzanti),tags=("kirmizi",))
                
                else:#eğer dosyanın uzantısı ile bulunan gerçek uzantı birbiri ile aynı değilse o sütunu kırmızı yaz
                    self.tree.insert("", tk.END, text=self.id_counter, values=(dosya, gercek_uzanti))
                

                self.id_counter += 1  # Her dosya için ID'yi bir artır

                



def main():#Programın başlatılmasını sağlayan fonksiyonlar.
    root = tk.Tk()
    app = DosyaListelemePenceresi(root)
    root.mainloop()

if __name__ == "__main__": #Bu ifade, Python betiğinin doğrudan çalıştırılması durumunda (import edilmediyse), main() fonksiyonunu çağırmak için kullanılır. Bu, betiğin başka bir betik tarafından import edildiğinde main() fonksiyonunun otomatik olarak çağrılmamasını sağlar.
    main()
