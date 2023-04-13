function yk_haskey() {
    local var=$(declare -p "$1")
    local key="$2"
    eval "declare -A _arr="${var#*=}
    for k in "${!_arr[@]}"; do
        if [ "$k" = "$key" ]; then
            echo 1
            return 0
        fi
    done
    echo 0
}