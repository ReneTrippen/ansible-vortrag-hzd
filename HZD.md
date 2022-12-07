# Intro
 * Vorstellung
    * Hinweise zur Aufzeichnung
    * Fragen bitte gerne während des Vortrages
    * Rene Trippen - Selbstständiger - IT Berater / Freelancer 
        * Linux seit über 20 Jahren / DevOps 
        * Angefangen in kleinen Unternehmen - FLS, Netzwerk, Rechenzentrum, Storage, Softwareentwicklung, Endkundenbetreuung
        * Überwiegend tätig im Rhein Main Gebiet, Finanzsektor / Versicherungen etc (große Kunden)

# Ansible
* Täglich wiederkehrende Todos
* Automatisierung evtl. schon vorhanden mit eigenen Scripten (Bash, Python, Perl, Korn Shell) 
* Andere Automatisierungstools wie Puppet(2005), Saltstack (Vmware/2011), Chef - Master/Agent
* Ansible braucht keinen Agent - Nur SSH
* Ansible hat eine großartige Dokumentation!
* Ansible ist Infrastructure as Code - Bevor man in Clouds startet, sollte man Infrastructure as Code in den Griff bekommen. Auch in der Cloud benötigt man Infrastruktur ;) 

# Handson
* frische Server geliefert - erst einmal die dailys
* inventory bauen / erweitern
* Ad Hocs
  * ansible command module kann einfache befehle
    * hostname
    * df -h /
    * free -m
    * uname -a
  * -m shell -a 
    * journalctl | grep ansible | wc -l

* facts zeigen (brauchen zeit)
* user erstellen / ssh key
* software aktualisieren
* needs-restarting yum-utils
* epel installieren

* Beispiel dynamic inventory (inventory.py)
* Beispiel Vault?
* Beispiel Vars

# Gui / Management
* Ansible Tower (ehemals) -> Automation Platform
* Ansible AWX (Upstream Project)
    * Installations mittels minikube
    * Bis Version 17 geht es mit lokalen Docker und ansible install.yaml

# Module
* Builtin & Community (Collection / Galaxy)


# Buchempfehlung
- Ansible for Devops - Jeff Geerling - 2te Auflage von 2020 (20€) oder auf Leanpub, dort aktualisiert er das Buch regelmäßig
  - Codebeispiele sind auf github geerlingguy


