# 🛒 Django E-Commerce System

## 📖 Overview
This is a **Django-based E-Commerce system** where users can browse products, add them to their cart, place orders, and view their order history. The system supports **user authentication, cart management, and order processing with "Cash on Delivery"**.

---

## 🚀 Features
✅ **User Authentication** (Login Required)  
✅ **Product Listings** (Image, Price, Description, Category, Brand)  
✅ **Add to Cart** (With Quantity Update)  
✅ **Checkout and Order Management** (Cash on Delivery)  
✅ **View Order History** (With Order ID, Date, Address, and Product Details)  
✅ **Admin Panel** (To Manage Users, Products, and Orders)  

---

## 📂 Project Structure
##  unzip this file

## create virtualenv 
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate  and linux: source env/bin/activate

##next install requirements.txt file
pip install -r requirements.txt

## setup database using this command
python manage.py makemigrations
python manage.py migrate

## createsuper user for this command
python manage.py createsuperuser


## run server
python manage.py runserver


