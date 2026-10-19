"""Builds the Aequitas Network site.

Each page body lives in src/<name>.html. This script wraps every body with the
shared header and footer and writes the finished page to the site root.
Run:  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"

PAGES = [
    # file, nav label, <title>, meta description
    ("index.html", "Home", "Aequitas Network | Technology, data, and learning that work for people",
     "Aequitas Network helps HOAs, small businesses, and organizations with community technology, data and learning analytics, and HR and learning consulting."),
    ("community-technology.html", "Community Technology", "Community Technology for HOAs | Aequitas Network",
     "Websites, resident apps, communications, and support for HOAs and community associations, from one partner."),
    ("analytics.html", "Data & Analytics", "Data & Learning Analytics | Aequitas Network",
     "Dashboards, reporting, data governance, and LMS strategy led by a Certified Data Management Professional."),
    ("people-learning.html", "People & Learning", "HR & Learning Consulting for Small Businesses | Aequitas Network",
     "HR and learning and development consulting for small businesses, plus leadership and team workshops and assessments."),
    ("about.html", "About", "About | Aequitas Network",
     "Our mission, how we work, and the team behind Aequitas Network."),
    ("contact.html", "Contact", "Contact | Aequitas Network",
     "Book a free consult or send Aequitas Network a message."),
]

NAV = [p for p in PAGES if p[0] not in ("index.html", "contact.html")]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600&family=Righteous&display=swap" rel="stylesheet">')


def header(current):
    cur = ' aria-current="page"'
    links = "".join(
        f'<a href="{f}"{cur if f == current else ""}>{label}</a>'
        for f, label, *_ in NAV
    )
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="assets/aequitas-network-horizontal.png" alt="Aequitas Network" width="180" height="36"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav">{links}<a class="btn" href="contact.html">Book a free consult</a></nav>
  </div>
</header>"""


FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <p class="tagline">Don't just check the box.</p>
        <p>Aequitas Network LLC: technology, data, and learning that work for people. Home of Aequitas IT Services. Notary services coming soon.</p>
        <p>aequitasnetwork.com &middot; <a href="mailto:info@aequitasnetwork.com">info@aequitasnetwork.com</a></p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="community-technology.html">Community Technology</a></li>
          <li><a href="analytics.html">Data &amp; Learning Analytics</a></li>
          <li><a href="people-learning.html">People &amp; Learning</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:info@aequitasnetwork.com">info@aequitasnetwork.com</a></li>
          <li><a href="contact.html">Book a free consult</a></li>
        </ul>
      </div>
    </div>
    <div class="fine"><span>&copy; 2026 Aequitas Network LLC. All rights reserved.</span><span>Aequitas IT Services is a service of Aequitas Network LLC.</span></div>
  </div>
</footer>
<script>
  const t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
  t.addEventListener('click', () => { const o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o); });
</script>"""


def page(file, title, desc, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="canonical" href="https://www.aequitasnetwork.com/{'' if file == 'index.html' else file}">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:image" content="https://www.aequitasnetwork.com/assets/aequitas-network-horizontal.png">
{FONTS}
<link rel="stylesheet" href="assets/styles.css">
</head>
<body{' class="it"' if file == 'community-technology.html' else ''}>
{header(file)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""


if __name__ == "__main__":
    for file, _label, title, desc in PAGES:
        body = (SRC / file).read_text()
        (ROOT / file).write_text(page(file, title, desc, body))
        print("built", file)
