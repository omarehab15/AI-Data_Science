import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Read data 
    # data = pd.read_csv('data\\titanic.csv')
    data = pd.read_csv(r'F:\studying\courses\AI\projects\DEBI1\Tasks\data\titanic.csv')


    # Drop mising data
    data.dropna(subset=['Age' , 'Fare' , 'Embarked'])
    zeros = [f'zero.{i}' for i in range(1,19)]
    data = data.drop(zeros, axis=1, inplace=False)
    data.drop("zero" , axis=1 , inplace=True)
    data.rename(columns={'2urvived':'Survived'}, inplace=True)

    st.dataframe(data)

    #Display a histogram for passengers' ages
    st.write('Histogram for passengers ages')
    fig, ax = plt.subplots()
    sns.histplot(data['Age'], ax=ax)
    st.pyplot(fig)

    # Display a bar chart for the number of passengers who survived and who did not
    st.write('Bar chart for the number of passengers who survived and who did not')
    fig, ax = plt.subplots()
    sns.countplot(data['Survived'], ax=ax)
    st.pyplot(fig)

    #Display a scatter plot for the passengers' ages and the fare they paid
    st.write('Scatter plot for the passengers ages and the fare they paid')
    fig, ax = plt.subplots()
    # sns.scatterplot(data['Age'], data['Fare'], ax=ax)
    sns.scatterplot(x=data['Age'], y=data['Fare'], ax=ax)

    st.pyplot(fig)

    # Add a dropdown list to filter the data based on the passengers survived or not
    st.write('Filter the data based on the passengers survived or not')
    survived = st.selectbox('Survived', data['Survived'].unique())
    filtered_data = data[data['Survived'] == survived]

    st.dataframe(filtered_data)

if __name__ == '__main__':
    main()