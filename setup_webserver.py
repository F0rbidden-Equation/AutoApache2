import os
import subprocess

# === 1. Demander le nom de domaine à l'utilisateur ===
domain = input("Entrez votre nom de domaine (ex: xcorp.ovh) : ").strip()
www_domain = f"www.{domain}"
web_dir = f"/var/www/{domain}"

# === 2. Installer Apache2 et Certbot ===
print("\n[+] Installation d'Apache2 et Certbot...")
subprocess.run(["apt", "update"])
subprocess.run(["apt", "install", "-y", "apache2", "certbot", "python3-certbot-apache"])

# === 3. Créer le répertoire du site web ===
print(f"[+] Création du dossier {web_dir}...")
os.makedirs(web_dir, exist_ok=True)

# === 4. Créer une page index.html simple ===
index_path = os.path.join(web_dir, "index.html")
with open(index_path, "w") as f:
    f.write(f"""<html>
  <head><title>{domain}</title></head>
  <body><h1>Bienvenue sur {domain}</h1></body>
</html>""")

# === 5. Créer le VirtualHost Apache ===
vhost_conf_path = f"/etc/apache2/sites-available/{domain}.conf"
print(f"[+] Création du fichier VirtualHost : {vhost_conf_path}")
with open(vhost_conf_path, "w") as f:
    f.write(f"""<VirtualHost *:80>
    ServerName {domain}
    ServerAlias {www_domain}
    DocumentRoot {web_dir}
    <Directory {web_dir}>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    ErrorLog ${{{{APACHE_LOG_DIR}}}}/{domain}_error.log
    CustomLog ${{{{APACHE_LOG_DIR}}}}/{domain}_access.log combined
</VirtualHost>""")

# === 6. Activer le site ===
print("[+] Activation du site...")
subprocess.run(["a2ensite", f"{domain}.conf"])
subprocess.run(["systemctl", "reload", "apache2"])

# === 7. Obtenir un certificat SSL avec Certbot ===
print("[+] Obtention du certificat SSL avec Certbot...")
subprocess.run(["certbot", "--apache", "-d", domain, "-d", www_domain])

print("\n✅ Installation terminée. Le site est en ligne en HTTPS.")
