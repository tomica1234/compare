import streamlit as st

st.title('価格比較')
time_per_month = st.slider('回数(月)', 0, 31)
km = st.slider('km(月)', 0, 3000)
nenpi = 10
gasolene = 160
nightpack_price = (2640 + 550)*time_per_month
distance_price = km*20
gasolene_price = int(gasolene*km/nenpi)
maintain = 17000


st.write('走行距離：', km, 'km')
st.write('----------タイムズ----------')
st.write('ナイトパック代：', nightpack_price, '円')
st.write('距離料金：', distance_price, '円')
st.write('合計(月)：', nightpack_price+distance_price, '円')


st.write('----------中古車----------')
st.write('維持費：', maintain, '円')
st.write('ガソリン代：', gasolene_price, '円')
st.write('合計(月)：', maintain+gasolene_price, '円')

if nightpack_price+distance_price < maintain+gasolene_price:
    st.write(f'タイムズの方が{-nightpack_price-distance_price + maintain+gasolene_price}円安い')
else:
    st.write(f'中古車の方が{nightpack_price+distance_price - maintain-gasolene_price}円安い')