import streamlit as st
import ollama

st.title('📢 Sosyal Yankı Filtresi')
st.write('Ham metninizi girin; açık kaynaklı yerel modeliniz metni tüm platformlar için eş zamanlı dönüştürsün.')

ham_metin = st.text_area('Duyuru veya Haber Metniniz:', placeholder='Örn: Yeni sezon el yapımı kahvelerimiz dükkana geldi, bekliyoruz!')

if st.button('Tonlara Dönüştür'):
    if ham_metin.strip():
        try:
            with st.spinner('Yapay zeka metni yeniden biçimlendiriyor...'):
                res_x = ollama.chat(model='gemma', messages=[{'role': 'user', 'content': f'Şu metni Twitter/X için kısa, vurucu ve 280 karakteri geçmeyecek şekilde yaz: {ham_metin}'}])
                res_li = ollama.chat(model='gemma', messages=[{'role': 'user', 'content': f'Şu metni LinkedIn için profesyonel ve kurumsal bir dille yaz: {ham_metin}'}])
                res_ig = ollama.chat(model='gemma', messages=[{'role': 'user', 'content': f'Şu metni Instagram için samimi, enerjik ve bol emojili yaz: {ham_metin}'}])
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.subheader('𝕏 / Twitter')
                    st.write(res_x['message']['content'])
                with col2:
                    st.subheader('💼 LinkedIn')
                    st.write(res_li['message']['content'])
                with col3:
                    st.subheader('📸 Instagram')
                    st.write(res_ig['message']['content'])
        except Exception as e:
            st.error(f'Ollama bağlantı hatası! Arka planda Ollama nın açık olduğundan emin olun. Hata: {e}')
    else:
        st.warning('Lütfen dönüştürülecek bir metin girin!')