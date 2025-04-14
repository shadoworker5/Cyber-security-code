#!/bin/bash

# @author Kassoum Traore
# @email shadoworker5.dev@gmail.com
# @create date 2025-04-14 09:10:46
# @modify date 2025-04-14 09:20:46

connectServerSSH() {
    # default port 22
    # uncomment if you use private key to connect with ssh
    # ssh -i /path/to/your/key.private $1.domain.com
    ssh username@$1.domain.com
}

PS3="Veuillez choisir un server: "
options=("Phenix" "Poseidon" "Pegase" "Andromede" "Zeus" "Dragon" "Quitter")

select choix in "${options[@]}"; do
    case $REPLY in
        ${#options[@]})
            echo "Aurevoir......"
            break
            ;;
        *)
            if [[ $REPLY -ge 1 && $REPLY -lt ${#options[@]} ]]; then
                connectServerSSH ${options[$REPLY-1]}
                break
            else
                echo "Option invalide ! Veuillez choisir entre 1 et ${#options[@]}"
            fi
            ;;
    esac
done