import qrcode
import streamlit as st

filename = 'qr_code.png'



def generate_qr_code(url,filename):
    qr =qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color ='black',back_color='white')
    img.save(filename)



st.set_page_config(page_title='QR CODE',layout='centered')
# st.image()
st.title(" :material/qr_code: Generador QR codes ",text_alignment='center')
url = st.text_input("Enter the URL")


if st.button(label='Generate QR Code',icon=":material/draw:"):
     generate_qr_code(url, filename)
     col1, col2, col3 = st.columns(3)
     with col2:
        st.image(filename,width="content", use_column_width=None,)
     with open(filename,"rb") as f:
                  image_data = f.read()
     download = st.download_button(label="Download QR", data=image_data, file_name='qr_generated.png',icon=":material/download:")



