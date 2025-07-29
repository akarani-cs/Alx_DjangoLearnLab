# Django HTTPS and Security Hardening

## Enforced HTTPS
- `SECURE_SSL_REDIRECT`: Redirects all HTTP to HTTPS
- `SECURE_HSTS_SECONDS`: Sets HTTP Strict Transport Security (1 year)
- `SECURE_HSTS_INCLUDE_SUBDOMAINS`: Applies to subdomains
- `SECURE_HSTS_PRELOAD`: Enables browser preload

## Secure Cookies
- `SESSION_COOKIE_SECURE`: Sends cookies only via HTTPS
- `CSRF_COOKIE_SECURE`: CSRF cookie transmitted only via HTTPS

## Secure Headers
- `X_FRAME_OPTIONS = 'DENY'`: Protects against clickjacking
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing
- `SECURE_BROWSER_XSS_FILTER = True`: Enables basic XSS filter

## Nginx HTTPS Setup
- Enforced SSL redirect from port 80
- Uses SSL certificates with Gunicorn reverse proxy

## Notes
- These settings are **enabled only when `DEBUG = False`** to avoid interfering with development.
- Future work: Add CSP headers using `django-csp`.

