import streamlit as st
import pickle
import numpy as np
import tensorflow.keras
from keras.models import load_model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = load_model('concrete.h5')



def predict_strength(CEMENT, SAND, AGGREGATE, WATER_CEMENT_RATIO, OIL_PALM_FIBRE_LENGTH, PERCENTAGE_ADDITION, WEIGHT_AFTER_CASTING, WEIGHT_AFTER_CURING,):
    input = np.array([[cement, sand, aggregate, water_cement_ratio, oil_palm_fibre_length,
                     percentage_addition, weight_after_casting, weight_after_curing]]).astype(np.float64)
    prediction = model.predict(input)
    return float(prediction)


def main():
    st.title("")
    html_temp = """
    <img src="https://github.com/raj-shyamal/Concrete-Strength-Predictor/blob/master/images/neon.jpg?raw=true" alt="neon" style="display: block;margin-left: auto;margin-right: auto;width: 50%;">
    <h1 style="color:black;text-align:center;">Neon Tech</h1>
    <div style="background-color:#0E0E0F ;padding:10px">
    <h2 style="color:white;text-align:center;">Concrete Strength Predictor</h2>
    <h3 style="color:white;text-align:center;">Artificial Neural Network</h3>
    </div>
   
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    t = 1.0
    cement = st.number_input("CEMENT(kg)")
    sand = st.number_input("SAND(kg)")
    aggregate = st.number_input("AGGREGATE(kg)")
    water_cement_ratio = st.number_input("WATER/CEMENT RATIO")
    oil_palm_fibre_length = st.number_input("OIL PALM FIBRE LENGTH(cm)")
    percentage_addition = st.number_input("PERCENTAGE ADDITION(%)")
    weight_after_casting = st.number_input("WEIGHT AFTER CASTING(kg)")
    weight_after_curing = st.number_input("WEIGHT AFTER CURING(kg)")

    t = float(cement) + float(sand) + float(aggregate) + float(water_cement_ratio) + float(oil_palm_fibre_length) + float(percentage_addition) + float(
        weight_after_casting)

    # safe_html = """  
    #   <div style="background-color:#F4D03F;padding:10px >
    #    <h2 style="color:white;text-align:center;"> Concrete is strong enough!</h2>
    #    </div>
    # """
    # danger_html = """  
    #   <div style="background-color:#F08080;padding:10px >
    #    <h2 style="color:black ;text-align:center;"> Concrete is not strong enough!</h2>
    #    </div>
    # """
    # c = float(cement)
    # w = float(water)
    # aggre = float(slag) + float(ash) + float(superplastic) + \
    #     float(coarseagg) + float(fineagg)
    # if t == 0:
    #     t = 1
    #     c_per = int((100 * c) / t)
    #     w_per = int((100 * w) / t)
    #     aggre_per = int((100 * aggre) / t)
    # else:
    #     c_per = int((100 * c) / t)
    #     w_per = int((100 * w) / t)
    #     aggre_per = int((100 * aggre) / t)

    if st.button("Predict"):
        output = int(predict_strength(cement, sand, aggregate, water_cement_ratio,
                     oil_palm_fibre_length, percentage_addition, weight_after_casting, weight_after_curing))

        if c >= 0.07 * t and c <= .15 * t and w >= 0.14 * t and w <= .21 * t and float(
                age) != 0 and aggre >= 0.6 * t and aggre <= .75 * t:
            st.success('Predicted Concrete Strength is {} Mpa'.format(output))
            # if output < 17:
            #     st.markdown(danger_html, unsafe_allow_html=True)
            # else:
            #     st.markdown(safe_html, unsafe_allow_html=True)

        # if float(age) == 0:
        #     st.success("Age can not be zero!")
        # else:
        #     if c < 0.07 * t:
        #         st.success(
        #             "Add more cement, current cement content is {}%\n\nIdeal cement content in mixture is 7-15%".format(
        #                 c_per))
        #         if c > .01 * t and w > 0.02 * t and aggre > 0.1:
        #             st.success(
        #                 'Predicted Concrete Strength is {} Mpa'.format(output))
        #     elif c > 0.15 * t:
        #         st.success(
        #             "Reduce cement content, current cement content is {}%\n\nIdeal cement content in mixture is 7-15%".format(
        #                 c_per))
        #         if c > .01 * t and w > 0.02 * t and aggre > 0.1:
        #             st.success(
        #                 'Predicted Concrete Strength is {} Mpa'.format(output))

        #     if w < 0.14 * t:
        #         st.success(
        #             "Add more water, current water content is {}%\n\nIdeal water content in mixture is 14-21%".format(
        #                 w_per))
        #         if c > .01 * t and w > 0.02 * t and aggre > 0.1:
        #             st.success(
        #                 'Predicted Concrete Strength is {} Mpa'.format(output))
        #     elif w > .21 * t:
        #         st.success(
        #             "Reduce water, current water content is {}%\n\nIdeal water content in mixture is 14-21%".format(
        #                 w_per))
        #         if c > .01 * t and w > 0.02 * t and aggre > 0.1:
        #             st.success(
        #                 'Predicted Concrete Strength is {} Mpa'.format(output))

        #     if aggre < 0.60 * t:
        #         st.success(
        #             "Add more Aggregate, current Aggregate content is {}%\n\nIdeal Aggregate content in mixture is 60-75%".format(
        #                 aggre_per))
        #         if c > .01 * t and w > 0.02 * t and aggre > 0.1:
        #             st.success(
        #                 'Predicted Concrete Strength is {} Mpa'.format(output))
        #     elif aggre > .75 * t:
        #         st.success(
        #             "Reduce Aggregate content, current Aggregate content is {}%\n\nIdeal Aggregate content in mixture is 60-75%".format(
        #                 aggre_per))
        #         if c > .01 * t and w > 0.02 * t and aggre > 0.1:
        #             st.success(
        #                 'Predicted Concrete Strength is {} Mpa'.format(output))


if __name__ == '__main__':
    main()
