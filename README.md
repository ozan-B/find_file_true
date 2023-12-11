<h1>Dosya Listeleme Uygulaması</h1>

<p>Bu basit Python uygulaması, belirli bir klasördeki dosyaları listeler ve dosyaların gerçek uzantılarına göre renklendirme yapar. Klasörün içindeki dosyaların gerçek uzantılarını gösterir ve eğer dosyanın uzantısı ile programın bize sunduğu uzantı eşleşmiyorsa o sütunu kırmızı renkte belirtir. Her dosya için bir ID kullanarak dosyaları Treeview widget'ına ekler. Programı çalıştıracağınız dizin içinde başka dizin olmamalı, sadece dosyalar olmalı. Bu özellik 2. versiyonda eklenmiştir.</p>

<h2>Belirlenen Dosya Türleri ve Gerçek Uzantılar</h2>

<ul>
  <li>JPEG dosyaları: <code>.jpeg</code> uzantısı</li>
  <li>PNG dosyaları: <code>.png</code> uzantısı</li>
  <li>GIF dosyaları: <code>.gif</code> uzantısı</li>
  <li>MP3 dosyaları: <code>.mp3</code> uzantısı</li>
  <li>PDF dosyaları: <code>.pdf</code> uzantısı</li>
  <li>DOCX dosyaları: <code>.docx</code> uzantısı</li>
  <li>XLSX dosyaları: <code>.xlsx</code> uzantısı</li>
  <li>PPTX dosyaları: <code>.pptx</code> uzantısı</li>
  <li>Access dosyaları: <code>.accdb</code> uzantısı</li>
  <li>ODT dosyaları: <code>.odt</code> uzantısı</li>
  <li>ODS dosyaları: <code>.ods</code> uzantısı</li>
  <li>ODP dosyaları: <code>.odp</code> uzantısı</li>
  <li>XLS dosyaları: <code>.xls</code> uzantısı</li>
  <li>DOC dosyaları: <code>.doc</code> uzantısı</li>
  <li>PPT dosyaları: <code>.ppt</code> uzantısı</li>
  <li>Metin dosyaları: <code>.txt</code> uzantısı</li>
  <li>CSV dosyaları: <code>.csv</code> uzantısı</li>
  <li>HTML dosyaları: <code>.html</code> uzantısı</li>
  <li>Exe dosyaları: <code>.exe</code> uzantısı</li>
  
</ul>

<h2>Başlangıç</h2>

<p>Uygulamayı kullanmaya başlamak için aşağıdaki adımları takip edebilirsiniz.</p>

<h3>Gereksinimler</h3>

<ul>
  <li>Python (3.x sürümü önerilir)</li>
  <li>Tkinter kütüphanesi</li>
  <li>Magic kütüphanesi</li>
</ul>

<h3>Kurulum</h3>

<ol>
  <li>Depoyu klonlayın:</li>
</ol>

<pre>
<code>git clone https://github.com/ozan-B/find_file_true
cd find_file_true</code>
</pre>

<ol start="2">
  <li>Uygulamayı başlatın:</li>
</ol>

<pre>
<code>python3 main.py</code>
</pre>

<h2>Kullanım</h2>

<p>"Klasör Seç" düğmesine tıklayarak bir klasör seçin. Uygulama, seçilen klasördeki dosyaları listeleyecek ve gerçek uzantılarına göre renklendirme yapacaktır.</p>

<h2>Katkıda Bulunma</h2>

<ol>
  <li>Bu depoyu forklayın.</li>
  <li>Yeni bir dal oluşturun (<code>git checkout -b feature/yenifonksiyon</code>).</li>
  <li>Yaptığınız değişiklikleri commit edin (<code>git commit -am 'Yeni fonksiyon eklendi'</code>).</li>
  <li>Dalınıza itme yapın (<code>git push origin feature/yenifonksiyon</code>).</li>
  <li>Bir Pull Request oluşturun.</li>
</ol>

<h2>Lisans</h2>

<p>Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için <a href="LICENSE">LICENSE</a> dosyasına göz atabilirsiniz.</p>
