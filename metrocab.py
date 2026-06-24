import streamlit as st
st.title("Ticket Booking")
name=st.text_input("Name")
mobile=st.text_input("Mobile number")
stations=["select","JNTUH","MYP","KPHB","MGBS","LB NAGAR","AMEERPET","MALAKPET"]
from_station=st.selectbox("from station",stations)
stations.remove(from_station)
to_station=st.selectbox("to station",stations)
tickets=st.number_input("Tickets",min_value=1,value=1)
cab_required=st.radio(
    "Do you need a cab",
    ["YES","NO"],index=None
)
if cab_required=="YES":
    destination=st.text_input("final destination")
if st.button("Book Ticket"):
    if from_station=="select" or to_station=="select":
        st.error("please select valid stations")
    else:
        bill=40*tickets
        st.subheader("Metro Ticket Details")
        st.write("Name:",name)
        st.write("Mobile",mobile)
        st.write("from station:",from_station)
        st.write("to station:",to_station)
        st.write("Tickets:",tickets)
        st.write("Bill Amount For metro=",bill)
        if cab_required=="YES":
            st.subheader("Cab details")
            st.write("Pickup:",to_station)
            st.write("Drop:",destination)
            car_bill=150
            bill+=car_bill
            st.write("car fare Amount=",car_bill)
        else:
            st.write("Cab Not Required")
        st.subheader("TOTAL FARE")
        st.write("total Bill Amount=",bill)
    
