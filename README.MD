
# Createx: Dynamic LaTeX Rendering Application

Createx is a Django-based web application that simplifies the process of generating PDF documents. You can templatize frequently used documents, so you do not need to think of their appearance, focus on content. LaTeX-based templates. Whether you're a LaTeX expert or a beginner, Createx provides a user-friendly platform to create professional documents without the hassle of manual LaTeX editing.

**Open [Createx](http://createx.a10na.space)**.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## <a name="features">Features</a>

### 1. Template Library

Browse and choose from a variety of templates for different document types. The template repository ensures a diverse selection to meet your document creation needs.

### 2. Preview of Document

See the preview of how the filled template looks both as image and as PDF document.
Explore examples of how the rendered document may look, providing a visual representation of the final document's layout and style.
### 3. Real-Time Rendering

Experience real-time rendering as Createx generates your document. You can see the impact of your changes and adjustments, ensuring a polished final result.

### 4. Download as PDF

Download your document as a high-quality PDF file once you are satisfied with the preview. Createx ensures that the final output is professional and ready for sharing or printing.

### 5. Templates available only to you

Take command of your templates by designating them as private for personal use or shareable via link with select individuals, offering tailored control over template accessibility.

## <a name="installation">Installation</a>

Follow these steps to get Createx up and running on your local machine:

#### Using Docker Compose:

##### 1. **Clone the Repository:**
```bash
git clone https://github.com/al3nka/createx.git
```
##### 2. **Navigate to the Project Directory:**
```bash
cd createx
```
##### 3. **Build Images:**
```bash
docker-compose build
```
##### 4. **Start the Application:**
```bash
docker-compose up -d
```
##### 5. **Access Createx:**
Visit `http://localhost:8000` in your web browser to start using Createx.

#### Using Helm Chart:

##### 1. **Clone the Repository:**
```bash
git clone https://github.com/al3nka/createx.git
```
##### 2. **Navigate to the Directory with Helm Chart:**
```bash
cd createx/helm
```

##### 3. **Install Createx Helm Chart:**
```bash
helm install createx . --namespace=createx --create-namespace
```
##### 4. **Access Createx:** Determine the service's IP address and port using:
```bash
kubectl get svc
```
Then visit `http://<service-ip>:<service-port>` in your web browser to start using Createx.

## <a name="usage">Usage</a>

##### Create Superuser:
If you are deploying with Helm, by default, the superuser is created with username `admin` and random password. You can see the password in kubernetes secret named 'createx-secret'. You also can define superuser credentials in file 'values.yaml':
```
createx:
  adminUser:  
    enabled: false  
    password: superuser_password 
    username: superuser_username
    email: superuser_email
```

Visit `http://localhost:8000/admin` in your web browser and log in using the superuser credentials you created.
If you are deploying with docker-compose, you can define superuser credentials in `.env` file like this:
```
CREATE_SUPERUSER=true
DJANGO_SUPERUSER_USERNAME=superuser_username
DJANGO_SUPERUSER_PASSWORD=superuser_password
DJANGO_SUPERUSER_EMAIL=superuser_email
```
##### Log in to Admin Site:
Visit `http://localhost:8000/admin` in your web browser and log in using the superuser credentials you created.

On admin site you can manage application:
- **Create User Registration Invitations:** the app supporots only invitation-based registration. So if you want to invite a friend to app, simply create a "Registration invitation" object, press "view on site" button and share a link.
- **Manage Templates:** In the admin site, you can also manage templates. Here, you can create new templates or modify existing ones to suit your needs.
##### Start Using Createx:
After setting up admin user and templates, you and users you invited can access Createx using the provided invitations. They can then log in and start creating documents using the available templates.

## <a name="contributing">Contributing</a>

Createx is an open-source project, and we welcome contributions from the community. Whether it's adding new templates, improving the user interface, or fixing bugs, your contributions make Createx better for everyone.

## <a name="license">License</a>

This project is licensed under the MIT License.