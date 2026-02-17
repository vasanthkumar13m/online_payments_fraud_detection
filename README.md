# Online Payments Fraud Detection using Machine Learning

## Introduction

With the rapid growth of digital payment systems, online transactions have become an essential part of daily life. However, this growth has also led to an increase in online payment fraud, causing significant financial losses to individuals and organizations. Detecting fraudulent transactions manually is challenging due to the large volume of transactions generated every second.
Machine Learning provides an effective solution by analyzing transaction patterns and identifying suspicious activities automatically. This project focuses on building a machine learning–based fraud detection system that predicts whether an online payment transaction is fraudulent or legitimate. The system is deployed using Flask as a web application, enabling users to receive real-time fraud predictions.

## Project Overview
Online payment fraud is a major concern in digital financial systems. This project uses Machine Learning techniques to classify transactions as fraudulent or legitimate. A Flask-based web interface allows users to enter transaction details and instantly view prediction results, making the system practical and user-friendly.
## Objectives
Detect fraudulent online payment transactions

Reduce financial loss caused by fraud

Provide a simple and user-friendly web interface

Apply machine learning classification techniques

## Machine Learning Approach
Algorithm Used: Random Forest Classifier

Problem Type: Binary Classification

Target Variable:
isFraud = 1 → Fraudulent transaction
isFraud = 0 → Legitimate transaction
## Dataset Description
Dataset Name: PaySim Dataset

Source: Kaggle

The PaySim dataset is a synthetic dataset that simulates real-world mobile money transactions.
## Features Used
step – Time step of the transaction

type – Type of transaction

amount – Transaction amount

oldbalanceOrg – Sender balance before transaction

newbalanceOrig – Sender balance after transaction

oldbalanceDest – Receiver balance before transaction

newbalanceDest – Receiver balance after transaction
## Technologies Used
Python

Flask

Scikit-learn

HTML, CSS

Git & GitHub

## Application Workflow
1.User opens the Home page

2.Clicks on Start Prediction

3.Enters transaction details

4.Machine Learning model processes the input

5.Prediction result (Fraud / Legitimate) is displayed
## Results
The Random Forest Classifier achieves good accuracy in detecting fraudulent transactions. The system provides reliable real-time predictions through a simple and intuitive web interface, helping improve transaction security and reduce financial risks.
