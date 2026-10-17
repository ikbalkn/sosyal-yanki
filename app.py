import streamlit as st
from groq import Groq

# ---------------------------------------------------------

# ---------------------------------------------------------
st.set_page_config(
    page_title="Sosyal Yankı Filtresi",
    page_icon="📡",
    layout="wide"
)

# ---------------------------------------------------------
# Groq API Bağlantısı (Secrets'tan Okur)
# ---------------------------------------------------------
if "GROQ_API_KEY" in st.secrets:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
else:
    GROQ_API_KEY = "BURAYA_GROQ_API_KEYINIZI_YAZIN"

client = Groq(api_key=GROQ_API_KEY)

def ai_yanit_al(prompt, system_prompt="Sen tarafsız ve profesyonel bir asistansın."):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

# ---------------------------------------------------------
# Arayüz ve 3 Modül
# ---------------------------------------------------------
st.title("📡 Sosyal Yankı Filtresi & Medya Dönüştürücü")
st.write("Metinlerinizi sosyal medyaya uyarlayın, 5N1K formatında haberleştirin veya doğruluk kontrolü yapın.")

tab1, tab2, tab3 = st.tabs([
    "📱 Sosyal Medya Dönüştürücü", 
    "📰 5N1K Haber Yazarı", 
    "🔍 Doğruluk & İddia Kontrolörü"
])

with tab1:
    st.header("Sosyal Medya Formatına Dönüştür")
    girdi_metni = st.text_area("Dönüştürülecek Metni Girin:", height=150, key="sm_text")
    platform = st.selectbox("Platform Seçin:", ["X (Twitter)", "LinkedIn", "Instagram Caption"])
    
    if st.button("Dönüştür", key="btn_sm"):
        if girdi_metni:
            with st.spinner("Yapay zeka dönüştürüyor..."):
                sys_msg = f"Sen bir sosyal medya uzmanısın. Verilen metni {platform} formatına en ilgi çekici şekilde dönüştür."
                yanit = ai_yanit_al(girdi_metni, system_prompt=sys_msg)
                st.success("Dönüştürüldü!")
                st.markdown(yanit)
        else:
            st.warning("Lütfen bir metin girin!")

with tab2:
    st.header("5N1K Formatında Haber Taslağı Oluştur")
    haber_konusu = st.text_area("Haber Konusu veya Taslak Notlar:", height=150, key="haber_text")
    
    if st.button("Haber Yaz", key="btn_haber"):
        if haber_konusu:
            with st.spinner("Haber hazırlanıyor..."):
                sys_msg = "Sen deneyimli bir gazetecisin. Verilen bilgileri kullanarak 5N1K kurallarına uygun profesyonel bir haber metni yaz."
                yanit = ai_yanit_al(haber_konusu, system_prompt=sys_msg)
                st.success("Haber Taslağı Hazır!")
                st.markdown(yanit)
        else:
            st.warning("Lütfen haber konusunu girin!")

with tab3:
    st.header("Metin & İddia Doğruluk Analizi")
    iddia_metni = st.text_area("Analiz Edilecek İddia veya Metin:", height=150, key="fact_text")
    
    if st.button("Analiz Et", key="btn_fact"):
        if iddia_metni:
            with st.spinner("İddia analiz ediliyor..."):
                sys_msg = "Sen bir doğruluk kontrolü uzmanısın. Metindeki iddiaları mantık ve bilgi çarpıtmaları açısından kritiğe tabi tut ve raporla."
                yanit = ai_yanit_al(iddia_metni, system_prompt=sys_msg)
                st.success("Analiz Tamamlandı!")
                st.markdown(yanit)
        else:
            st.warning("Lütfen analiz edilecek metni girin!")
