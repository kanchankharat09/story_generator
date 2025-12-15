import streamlit as st


st.title('AI Story Generator From Images')
st.markdown('Upload 1 to 10 images,choose an style and let the AI narrate a story for you')



with st.sidebar:
    st.header("controls")

    # sidebar option to upload images 

    uploaded_files=st.file_uploader(
        'Upload your files...',
        type=['png','jpg','jpeg'],
        accept_multiple_files=True
    )
    

    # selecting an story style

    st.selectbox(
        'Choose a story style',
        ('comedy','Thrillar','Fairy Tale','Sci-Fi','Mystery','Adventure','Morale')
    )



    # generate story  type='primary' if chrom theam is dark button color adjest accoring to that color
    generate_button=st.button('Generate Story and Narration',type='primary')



# main logic

if generate_button:
    if not uploaded_files:#( if no image file upload in upload file)
        st.warning('please upload atlest 1 image!') # then show this 
    elif len(uploaded_files)>10:
        st.warning('please upload an maximum of 10 images')
    else:
         with st.spinner('The AI is writing and narrating your story..... This may take few moments'):
           st.write('hello')