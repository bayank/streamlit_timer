
import streamlit as st
import time


def timer():

    col1, col2= st.columns([1,1])
    st.markdown("<ol><li>Press start button to start timer.</li><li>Press start button again to reset timer.</li><li>Press stop button to stop timer.</li></ol>", unsafe_allow_html=True)
    start = col1.button("Start")
    stop = col1.button("Stop")


    elapsed_time_placeholder = st.empty()
    elapsed_time_placeholder.markdown("# Elapsed Time: 0.00")
    if start:
        start_time = time.time()
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            elapsed_time_placeholder.markdown(f'# Elapsed Time: {elapsed_time:.2f}')
            time.sleep(.01)



if __name__ == '__main__':
    st.title("Very Simple Timer App")
    st.markdown("Built with Streamlit, by Bayan Khalighi")
    st.markdown("Find me on [GitHub](https://www.github.com/bayank)")
    timer = timer()



