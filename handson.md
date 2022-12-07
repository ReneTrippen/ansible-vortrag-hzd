* adhoc commands
* inventory aufbauen
* simple tasks yaml
  * epel-release, bash-completion, yum-utils
  * einen service prüfen (chrony evtl)
  * fail2ban installieren
    *  konfigurieren -> rollen
* rollen
  * tasks in rollen aufsplitten
    * software installieren
    * user anlegen
        * pub key
        * sudoers
    * software konfigurieren
     * fail2ban config 
     * fail2ban systemd restart
    * immer weiter aufbauen
        * bis zu langsam -> tags
        * bis zu nicht idempotent -> notify -> handlers
    * mehrere user
        * group_vars
            * all
            * einzelne server gruppen

    * templates mit vars 

