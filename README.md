# 🔧 AutoApache — Déploiement et Nettoyage Automatisés de Sites Apache2

**AutoApache** est un outil en Python permettant de **déployer automatiquement un site web Apache2** avec certificat SSL Let's Encrypt, et de **nettoyer entièrement** un site web existant sur un serveur Ubuntu.

---

## ✨ Fonctionnalités

- ✅ Installation automatisée d’un site web Apache2
- ✅ Création du VirtualHost avec redirection HTTP → HTTPS
- ✅ Génération automatique du certificat SSL via Certbot
- ✅ Création du dossier `/var/www/` et d’une page d'accueil HTML
- ✅ Nettoyage complet d’un ancien site (VirtualHost, dossier, logs, SSL)

---

## 📁 Structure du projet

| Fichier                | Description |
|------------------------|-------------|
| `setup_webserver.py`   | Script interactif pour déployer un site Apache2 |
| `cleanup_site.py`      | Script interactif pour supprimer un site proprement |

---

## ⚙️ Prérequis

- ✅ Ubuntu 20.04 ou plus
- ✅ Accès sudo
- ✅ Un nom de domaine pointant vers l’IP du VPS (A record)
- Python 3 (installé par défaut sur Ubuntu)
  
---

## 🚀 Utilisation

### ▶️ Déployer un site web

```bash
sudo python3 setup_webserver.py
