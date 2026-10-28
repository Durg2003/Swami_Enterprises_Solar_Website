# Swami Enterprises — Django Solar Website

A responsive starter website for a solar business, built with Django, SQLite, HTML, CSS and JavaScript. Includes product catalogue, interactive savings estimator, enquiry form, and Django admin for managing products and leads.

## Run locally (Windows)
1. Install Python 3.10+ from python.org.
2. Open Command Prompt in this folder.
3. Create and activate a virtual environment:
   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bat
   pip install -r requirements.txt
   ```
5. Create database tables and admin account:
   ```bat
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Start the site:
   ```bat
   python manage.py runserver
   ```
7. Visit `http://127.0.0.1:8000/` and admin at `http://127.0.0.1:8000/admin/`.

## Admin workflow
- Add verified solar panels, inverters, batteries, complete systems and accessories under Products.
- Add brand, capacity, efficiency, warranty, datasheet URL and price only when verified.
- Customer enquiries submitted through Contact are stored under Enquiries. Update their status as you follow up.

## Important before public launch
- Replace the development `SECRET_KEY`, set `DEBUG=False`, configure `ALLOWED_HOSTS`, HTTPS, database backups, and secure hosting.
- Add verified business phone/email/address/service area, real logo and approved product photography.
- Configure SMTP if email notifications are required; currently the form saves enquiries to the database and displays a success message, but does not send an email.
- Add real product entries in Django admin; the product catalogue intentionally starts empty rather than inventing vendor relationships or specs.
- The calculator is indicative only and is not a quote or engineering design. Validate assumptions with a qualified solar installer; account for local tariffs, shade, roof orientation, losses, applicable scheme rules and net-metering policy.
- Review the privacy policy for the actual business and applicable laws.
- For production, add rate limiting / spam protection and test accessibility, backups, security and form flows.

## Features
- Responsive home page and mobile navigation
- Product catalogue search and category filter
- Live solar estimate: suggested kW, estimated monthly generation, potential bill savings, annual savings, indicative roof area
- Enquiry form with validation and database persistence
- Django admin for products and enquiry status management
- About and privacy pages
