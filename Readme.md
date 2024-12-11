

---

# 📚 Students Management System - Flask Web Application

Welcome to the **Students Management System** built using **Flask**, **MongoDB**, and **Bootstrap**! 🚀 This project allows you to **Create**, **Read**, **Update**, and **Delete** student records through a user-friendly interface. Let's explore the details! 💻✨

## 🚀 Features

- **✨ Beautiful User Interface**: Built with **Bootstrap** and custom styling to ensure a smooth and aesthetic experience.
- **📱 Fully Responsive**: The application looks great on all devices, from desktops to mobile phones.
- **📚 CRUD Operations**: You can **add, view, update**, and **delete** student records in the database.
- **🔙 Home Button**: Go back to the homepage anytime with an easy-to-access button.
- **🛠 Flash Messages**: Alerts are shown on the page for any important actions (like success or errors).
- **❤️ Footer**: Featuring credits and a visit link.

## 🌟 Technologies Used

- **Python**: The backend is powered by **Flask**, a lightweight Python web framework.
- **MongoDB**: All students' data is stored in a **MongoDB** database.
- **Bootstrap**: Provides an attractive and responsive design out of the box.
- **HTML/CSS**: For structuring the page and styling it.

## 🔧 Installation

### Prerequisites

Before you get started, ensure you have the following installed on your machine:

- Python 3.x
- Flask
- MongoDB
- Bootstrap (used via CDN)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/students-management.git
   cd students-management
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure your **MongoDB** server is running locally or remotely.

4. Run the Flask application:

   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000` to see the application in action! 🎉

## 🎨 UI Preview

Here is a preview of how the application looks:

- **Home Page**: With a **Go Back to Home** button that takes you back to the homepage.
- **Students Table**: Displays all students' information in a neat table with hover effects.
- **Footer**: Includes credits and a footer link to a helpful website.

## 🖥 How It Works

This application provides a simple **CRUD** (Create, Read, Update, Delete) functionality for managing student records in a MongoDB database. Here’s a breakdown of each operation:

### 1. **Create** (Add Student)
The application allows you to add new students to the database. The form to add a student includes fields for:
- **Name**
- **Age**
- **Grade**

After submitting the form, a new student is created and added to the database. A success message is displayed to confirm the action.

### 2. **Read** (View Students)
Once a student is added, you can view all student records in a well-structured table. The table shows:
- **Name**
- **Age**
- **Grade**

The table is populated dynamically using data fetched from the MongoDB database. Additionally, you can filter students based on various attributes.

### 3. **Update** (Edit Student)
You can edit an existing student’s details. The application provides an **Edit** button next to each student record in the table. Clicking it allows you to modify the following fields:
- **Name**
- **Age**
- **Grade**

After saving the changes, the updated student data is saved to the database, and a success message is displayed.

### 4. **Delete** (Remove Student)
If you want to delete a student, there is a **Delete** button next to each record. Clicking this button removes the student from the database. A confirmation message will be displayed to confirm the deletion.

## ⚙️ Database Configuration

The application uses **MongoDB** as the database to store student information. The connection URI for MongoDB can be configured in the Flask app.

### Example configuration:

```python
app.config['MONGO_URI'] = 'mongodb://localhost:27017/studentsdb'
```

- The **studentsdb** database stores student records in a collection called **students**.
- Each student document contains the following fields: **name**, **age**, and **grade**.

## 📱 Mobile-Friendly

The app is **fully responsive** and provides a seamless experience on mobile devices. Try resizing your browser window to see how the layout adjusts!

## 📸 Screenshots

### Home Page
![Home Page](https://via.placeholder.com/600x400.png?text=Home+Page+Screenshot)

### Students Table
![Students Table](https://via.placeholder.com/600x400.png?text=Students+Table+Screenshot)

### Add/Edit Student Form
![Add/Edit Student Form](https://via.placeholder.com/600x400.png?text=Add+or+Edit+Student+Form)

## 📝 Contributing

Contributions are welcome! If you find any issues or have ideas for improvement, feel free to open an issue or create a pull request. Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## 🛠️ License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by **Bushra Shahbaz** (BSDSF21M020) 🚀

---

## 💬 Feel Free to Reach Out

If you have any questions or feedback, feel free to reach out to me at [bsdsf21m020@pucit.edu.pk](mailto:bsdsf21m020@pucit.edu.pk). 😊

---

## 🔧 Requirements

### **`requirements.txt`**

Here are the dependencies you need to install:

```txt
Flask==2.2.2
flask-pymongo==2.3.0
pymongo==4.3.3
flask-wtf==1.0.0
```

### How to Install:

1. **Create a Virtual Environment (optional but recommended)**:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - **For Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **For Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   After installing the dependencies, run the Flask application with:

   ```bash
   python app.py
   ```

---