# Aesthetics Clinic Website

A luxury spa-style aesthetic clinic website built with Django, featuring a clean and elegant design.

## Features

- Responsive design with luxurious aesthetics
- Treatment catalog with detailed information
- Before & After image gallery
- Team member profiles
- Client testimonials
- Blog functionality
- Contact form with Google Maps integration
- Admin panel for content management

## Design Elements

- **Theme**: Clean, luxury spa-style aesthetic with white space and soft colors like rose gold, nude, ivory
- **Typography**: Elegant serif for headers (Playfair Display), modern sans-serif for body text (Montserrat)
- **Animation**: Soft hover effects and subtle fade-ins
- **Tone**: Warm, expert, inviting — focused on empowerment and trust

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/aesthetics-clinic.git
cd aesthetics-clinic
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Apply migrations:
```
python manage.py migrate
```

5. Create a superuser for the admin panel:
```
python manage.py createsuperuser
```

6. Run the development server:
```
python manage.py runserver
```

7. Access the website at `http://127.0.0.1:8000/`

## Admin Access

Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

Use this to:
- Add/edit treatments
- Upload before/after images
- Manage team members
- Add testimonials
- Create blog posts
- View contact form submissions

## Project Structure

- `azfi/` - Main app containing models, views, and forms
- `settings/` - Project settings
- `templates/` - HTML templates
- `static/` - CSS, JavaScript, and image files
- `media/` - User-uploaded content (created at runtime)

## Technologies Used

- Django 5.2
- Bootstrap 5
- Crispy Forms with Bootstrap 5
- CKEditor for rich text editing
- Google Maps API for location display
- Font Awesome icons

## License

This project is licensed under the MIT License - see the LICENSE file for details. 