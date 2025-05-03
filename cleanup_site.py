import os
import subprocess
import shutil

def run(cmd):
    print(f"[+] {cmd}")
    subprocess.run(cmd, shell=True, check=False)

domain = input("Entrez le nom de domaine à supprimer (ex: xcorp.ovh) : ").strip()
www_domain = f"www.{domain}"
web_dir = f"/var/www/{domain}"
vhost_conf = f"/etc/apache2/sites-available/{domain}.conf"
ssl_conf = f"/etc/apache2/sites-available/{domain}-le-ssl.conf"
log_access = f"/var/log/apache2/{domain}_access.log"
log_error = f"/var/log/apache2/{domain}_error.log"

print(f"\n--- 🔥 Nettoyage de l'ancien site : {domain} ---\n")

# 1. Désactiver le site s’il est actif
run(f"a2dissite {domain}.conf")
run(f"a2dissite {domain}-le-ssl.conf")

# 2. Supprimer les fichiers de conf Apache
for path in [vhost_conf, ssl_conf]:
    if os.path.exists(path):
        os.remove(path)
        print(f"[✓] Supprimé : {path}")

# 3. Supprimer les répertoires du site
if os.path.exists(web_dir):
    shutil.rmtree(web_dir)
    print(f"[✓] Dossier supprimé : {web_dir}")

# 4. Supprimer les logs personnalisés
for log in [log_access, log_error]:
    if os.path.exists(log):
        os.remove(log)
        print(f"[✓] Log supprimé : {log}")

# 5. Supprimer les certificats SSL Let's Encrypt (optionnel)
cert_dir = f"/etc/letsencrypt/live/{domain}"
if os.path.exists(cert_dir):
    run(f"certbot delete --cert-name {domain}")

# 6. Recharger Apache
run("systemctl reload apache2")

print(f"\n✅ Le site {domain} a été complètement nettoyé.")
