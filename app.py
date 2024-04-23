import streamlit as st

def main():
    st.set_page_config(layout="wide")
    st.title("GI Prep Reminder")

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.subheader("Prep Type")
        option = st.selectbox('Select Prep Type', 
                        ['GoLYTELY One Day', 
                        'MiraLAX One Day', 
                        'MiraLAX Two Day',
                        'SUPREP'], 
                        key='1')
        
    with col2:
        st.subheader("Prep Guides") 
        if option == 'GoLYTELY One Day':
            st.success("Colonoscopy GoLYTELY One Day Quick Guide")
        
        if option == 'MiraLAX One Day':
            st.success("Colonoscopy One Day MiraLAX Quick Guide")

        if option == 'MiraLAX Two Day':
            st.success("Colonoscopy Two Day MiraLAX Quick Guide ")   
        
        if option == 'SUPREP':
            st.success("Colonoscopy SuPrep One day Quick Guide")

    with col3:
        st.subheader("Guides and Videos")
        if option == 'GoLYTELY One Day':
            st.success("Link: https://www.dukehealth.org/sites/default/files/colonoscopy_with_golytely_one_day_preparation_instructions.pdf")
            st.success("Video: https://youtu.be/JoJ8XEm8gN0?feature=shared")
        
        if option == 'MiraLAX One Day':
            st.success("Link: https://www.dukehealth.org/sites/default/files/colonoscopy_with_miralax_one_day_preparation_instructions.pdf")
            st.success("Video: https://youtu.be/JoJ8XEm8gN0?feature=shared")

        if option == 'MiraLAX Two Day':
            st.success("Link: ")
            st.success("Video: https://youtu.be/JoJ8XEm8gN0?feature=shared")    
        
        if option == 'SUPREP':
            st.success("Link: https://www.dukehealth.org/sites/default/files/colonoscopy_with_suprep_one_day_preparation_instructions_2.2019_0.pdf")
            st.success("Video: https://youtu.be/JoJ8XEm8gN0?feature=shared")


if __name__ == "__main__":
    main()

# Display the selected options
#st.write('You selected:', dropdown_1, dropdown_2, dropdown_3, dropdown_4, dropdown_5, dropdown_6, dropdown_7, dropdown_8, dropdown_9, dropdown_10)
