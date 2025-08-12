import streamlit as st
import yfinance as yf


st.title(f'Цена и объём по тикеру')
col1, col2, col3 = st.columns(3)

tickerSymbol = col1.text_input(label='Введите название тикера', value='AAPL', max_chars=15,
                             placeholder=('AAPL, RUB=X, BTC-USD...')).upper() or 'AAPL'
period = col2.selectbox(label='За какой период показать данные?', options=(
    "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"), index=10)
interval = col3.selectbox(label='Какой шаг данных?', options=(
    "1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"),index=11)

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period=period, interval=interval)

st.header('Цена закрытия')
st.line_chart(tickerDf.Close)
st.header('Объём торгов')
st.line_chart(tickerDf.Volume)


