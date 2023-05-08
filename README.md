# AI-Based-WAF

Nasıl Çalıştırılır?

Öncelikle XAMPP kurmanız gerekmektedir. Daha sonrasında Yaren Şenöz' ün yazmış olduğu Web Uygulamayı sisteminize indirip htdocs klasörünün içine atmanız gerekmektedir. Daha sonrasında istediğiniz bir dizine python_proxy.py dosyasını kurmanız gerekiyor. XAMPP uygulamasını çalıştırıp Apache ayarlarında default HTTP portunu 8080 olarak ayarlamanız gerekmektedir. Daha sonrasında python_proxy.py dosyasının bulunduğu dizine machine_learning_output.txt isimli bir text dosyası oluşturun ve içine 1 veya 0 yazın. Eğer içine 1 yazarsanız proxy bunu saldırı olarak algılar ve search fonksiyonunda arattığınız her şeyden sonra response olarak 403 alırsınız. Eğer dosyanın içine 0 yazarsanız proxy müdahale etmez ve dilediğiniz gibi kullanabilirsiniz.
