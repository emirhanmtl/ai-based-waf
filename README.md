# AI-Based-WAF

## Nasıl Çalıştırılır?

1) Öncelikle XAMPP uygulamasını kurmanız gerekmektedir. 
2) Yaren Şenöz' ün yazmış olduğu [TechZone](https://github.com/snzyrn/TechZone) uygulamasını sisteminize indirip XAMPP/htdocs/ klasörünün içine atmanız gerekmektedir. 
3) Daha sonrasında istediğiniz bir dizine "python_proxy.py" dosyasını kurmanız gerekiyor.
4) Gerekli kütüphaneleri "pip install requests" yöntemiyle kurun.
4) XAMPP uygulamasında Apache ayarlarında HTTP portunu "8080" olarak ayarlayıp Apache sunucusunu başlatın.
5) "proxy_server.py" dosyasının bulunduğu dizine "machine_learning_output.txt" isimli bir text dosyası oluşturun ve içine 1 veya 0 yazın. Eğer içine 1 yazarsanız proxy bunu saldırı olarak algılar ve search fonksiyonunda arattığınız her şeyden sonra response olarak 403 alırsınız. Eğer dosyanın içine 0 yazarsanız proxy müdahale etmez ve dilediğiniz gibi kullanabilirsiniz.
6) Komut satırını kullanarak "python proxy_server.py" komutunu kullanarak proxy-server' ı başlatın.
7) Arama fonksiyonunda arattığınız her kelime "proxy_server.py" dizinindeki "search_query.txt" dosyasına kaydedilir. (Her arama yaptığınızda içeriği sıfırlanıp yeni aramanız içine kaydedilir.) 

![BitirmeFoto](https://user-images.githubusercontent.com/61901730/236849571-2b7686e1-4827-486c-9fbb-cde5de7865aa.png)

## Eklenecekler
1) Makine öğrenme algoritmasının "search_query.txt" dosyasındaki kelimeyi alıp algoritmaya sokup "machine_learning_output.txt" dosyasına 1 veya 0 yazdırması eklenmeli.
