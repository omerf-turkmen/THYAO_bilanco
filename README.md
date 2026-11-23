# THYAO bilanço tahmini

Ridge_100 modeli, THYAO'nun bir sonraki çeyrekteki toplam varlıklarını tahmin eder. Bu depo, eğitilmiş modelin ham özelliklere dönüştürülmüş katsayılarını ve sabit 2026Ç3 girdisiyle çalışan bir Python demosunu içerir.

```bash
python ridge_demo.py
```

Python 3 yeterlidir. Beklenen 2026Ç4 tahmini **2.760.712,77 milyon TL**. Model önce log büyümeyi hesaplar, ardından son toplam varlığı exp(log büyüme) ile çarpar.

Dokuz girdi, son dört çeyreğin toplam varlık log büyümeleri, dönen varlık ve kısa/uzun vadeli yükümlülüklerin toplam varlığa oranları ve hedef çeyreğin sinüs/kosinüs kodlarıdır.

Ridge_100 doğrulamada seçildi. Son model 58 örnekle eğitildi. 2024Ç1–2026Ç3 arasındaki 11 çeyreklik sıralı testte MAPE %1,6748, son dört büyümenin medyanıyla yapılan kıyasta %1,7913 idi. 54 KAP yayın tarihi ve ilk yayın sürümleri tam teyit edilmedi. Sonuçlar çeyrek sıralı deney kapsamında yorumlanmalıdır. SHAP katkıları model çıktısını açıklar ve nedensellik veya doğruluk garantisi vermez.

Bu sürüm doğrudan kayıtlı denklemi uygular. Orijinal joblib dosyası, Excel ve sunum raporları bu depoya dahil edilmemiştir.
