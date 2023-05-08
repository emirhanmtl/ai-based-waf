# AI-Based-WAF

Nasıl Çalıştırılır?

1) Öncelikle XAMPP uygulamasını kurmanız gerekmektedir. 
2) Yaren Şenöz' ün yazmış olduğu Web Uygulamayı sisteminize indirip htdocs klasörünün içine atmanız gerekmektedir. 
3) Daha sonrasında istediğiniz bir dizine python_proxy.py dosyasını kurmanız gerekiyor.
4) Gerekli kütüphaneleri "pip install requests" yöntemiyle kurun.
4) XAMPP uygulamasında Apache ayarlarında default HTTP portunu 8080 olarak ayarlayıp Apache sunucusunu başlatın.
5) Komut satırını kullanarak "python proxy_server.py" komutunu kullanarak proxy-server' ı başlatın.
5) Son olarak proxy_server.py dosyasının bulunduğu dizine machine_learning_output.txt isimli bir text dosyası oluşturun ve içine 1 veya 0 yazın. Eğer içine 1 yazarsanız proxy bunu saldırı olarak algılar ve search fonksiyonunda arattığınız her şeyden sonra response olarak 403 alırsınız. Eğer dosyanın içine 0 yazarsanız proxy müdahale etmez ve dilediğiniz gibi kullanabilirsiniz.
