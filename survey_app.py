# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:54:38 2024

@author: sb0538
"""

import streamlit as st

# Soruları ve seçenekleri tanımlayın
questions = [
    ("Finansal Okuryazarlık:", ['Finansal okuryazarlık seviyem yüksek', 'Finansal okuryazarlık seviyem düşük']),
    ("Yıllık toplam geliriniz aşağıdakilerden hangisinde yer almaktadır?", ['30.000\'den az', '30.000-90.000 aralığında', '90.000-150.000 aralığında', '150.000 ve üzeri']),
    ("Uzun vadeli yatırımlarınızın bugünkü değeri nedir?", st.number_input("Yatırım Değeri:", min_value=0.0)),
    ("Lütfen yaş aralığınızı seçiniz.", ['40 veya daha az', '41-55 aralığında', '55-65 aralığında', '65 ve üzeri']),
    ("Yatırım hedefinize ulaşmanın önemini daha iyi açıklayan ifadeyi seçiniz:", [
        'Önemli, ancak kritik değil. Amacım için olabildiğince çok miktar biriktirmek isterim ancak aklımdaki hedefi gerçekleştiremezsem başka finansal kaynaklarım da mevcut.',
        'Çok önemli. Kazanım hedefime ulaşamazsam, gelecek ödemelerim için aksaklık olacağından daha fazla borçlanmam gerekebilir.'
    ]),
    ("Geçen haftaki doğum günü partimi:", [
        'İş yerinden benim gibi bekar arkadaşlarımla bir gece kulübünde bir parti ile',
        'Eşimi geçen yıl evlilik yıl dönümü için götürdüğüm restoranda bir yemek eşliğinde',
        'Eşim ve çocuklarımla birlikte evde pasta keserek',
        'Çocuklarım ve torunlarımın benim için düzenlediği partide pasta keserek kutladım.'
    ]),
    ("Bir sonraki büyük yatırımım:", ['Araba almak', 'Gayrimenkul almak', 'Yeni bir iş girişimini sermayeye dönüştürmek', 'Emeklilik hayallerimi gerçekleştirmek']),
    ("Beklemediğiniz bir anda 500.000TL'lik bir ödeme alacağınızı öğrendiniz. Bu ödemeyi hangi şekilde değerlendirirsiniz?", [
        'Tamamını çocuklarımın eğitim masrafları için kullanırım.',
        '100.000TL\'sini iş için kullanıp, kalanını banka hesabıma yatırırım.',
        'Kendim ve eşim için hediyeler alıp kalanını çeşitli yatırımlar ile değerlendiririm.',
        'Tamamını harcayabilirim bu ödeme benim için büyük bir miktar değil.'
    ]),
    ("Birikimimi yatırım fonlarında değerlendirmek için planladığım süre:", ['1 yıldan az', '1 - 3 yıl aralığında', '3 - 10 yıl aralığında', '10 yıl ve üzeri']),
    ("Yatırım fonlarındaki birikimimi nakide çevirmeyi planladığım süre:", ['2 yıldan az', '2 - 5 yıl aralığında', '5 - 10 yıl aralığında', '10 yıl ve üzeri']),
    ("Haberlerde yarın kar yağacağı ihtimalinin çok yüksek olduğu bilgilendirmesi yapıldı:", ['Kesinlikle evden çıkmam', 'Gerekli önlemlerimi alıp, plan yaparım', 'Yarınki şartlara göre karar veririm', 'Gerekli donanımım yok ama şansımı denerim']),
    ("Risk kelimesi size hangisini çağrıştırır?", ['Kayıp', 'Belirsizlik', 'Fırsat', 'Heyecan']),
    ("Planladığın tatile çıkmadan iki hafta önce maalesef işini kaybettin, ne yaparsın?", ['İptal ederim', 'Daha az lüks bir tatil yaparım', 'Planladığım gibi tatile giderim', 'Tatilimi uzatırım'])
]

# Finansal okuryazarlığı olanlar için ek sorular
high_literacy_risk_questions = [
    "Piyasalar hakkındaki öngörülerime göre hareket ederim.",
    "Yakın zamanda olumlu haber akışına sahip şirketleri tercih ederim.",
    "Geçmişte istikrarlı büyüme göstermiş şirketleri tercih ederim."
]

# Finansal okuryazarlığı olmayanlar için ek sorular
low_literacy_risk_questions = [
    "Para kaybetmemek öncelikli hedefimdir.",
    "Kâr etmek öncelikli hedefimdir.",
    "Yatırım danışmanımın görüşünü dikkate alırım."
]

# Anketi başlat
st.title("Yatırımcı Risk Profili Anketi")

# Anket sorularını göster
answers = {}
for question, options in questions:
    if isinstance(options, list):
        answer = st.radio(question, options)
    else:
        answer = options
    answers[question] = answer

# Ek sorular
literacy_level = answers.get("Finansal Okuryazarlık:")
if literacy_level == 'Finansal okuryazarlık seviyem yüksek':
    st.write("Ek Sorular:")
    for question in high_literacy_risk_questions:
        st.write(f"- {question}")
else:
    st.write("Ek Sorular:")
    for question in low_literacy_risk_questions:
        st.write(f"- {question}")

# Sonuçları göster
if st.button("Gönder"):
    st.write("Anket Sonuçları:")
    for question, answer in answers.items():
        st.write(f"{question} {answer}")
